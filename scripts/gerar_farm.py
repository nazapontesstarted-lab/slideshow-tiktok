from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import sys
from PIL import Image
from modelo_slideshow import carregar_temas, gerar_slideshow, pasta_do_tema, slug
import cota_slideshows

ROOT = Path(__file__).resolve().parent.parent
ARQUIVO_HISTORICO = ROOT / "data" / "historico.json"
FUSO = ZoneInfo("America/Sao_Paulo")
STATUS_CONCLUIDO = ("sucesso", "gerado")


class Divergencia(Exception):
    """Histórico, pastas e cota não batem; nada deve ser gerado."""


def carregar_historico():
    if not ARQUIVO_HISTORICO.exists():
        return {"temas_usados": [], "execucoes": []}

    try:
        dados = json.loads(ARQUIVO_HISTORICO.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        raise ValueError(
            f"{ARQUIVO_HISTORICO} é um JSON inválido: {erro}. "
            "Nada foi alterado; corrija o arquivo manualmente."
        ) from erro

    if not isinstance(dados, dict):
        raise ValueError(f"{ARQUIVO_HISTORICO} deve conter um objeto JSON.")

    dados.setdefault("temas_usados", [])
    dados.setdefault("execucoes", [])
    if not isinstance(dados["temas_usados"], list) or not isinstance(dados["execucoes"], list):
        raise ValueError(
            "'temas_usados' e 'execucoes' em historico.json devem ser listas."
        )
    return dados


def salvar_historico(historico):
    ARQUIVO_HISTORICO.parent.mkdir(parents=True, exist_ok=True)
    temporario = ARQUIVO_HISTORICO.with_suffix(".tmp")
    temporario.write_text(
        json.dumps(historico, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporario.replace(ARQUIVO_HISTORICO)


def temas_usados(historico):
    """Slugs (sem acento/caixa) dos temas já concluídos segundo o histórico."""
    usados = {slug(t) for t in historico["temas_usados"] if isinstance(t, str)}
    for execucao in historico["execucoes"]:
        if (
            isinstance(execucao, dict)
            and execucao.get("status") in STATUS_CONCLUIDO
            and isinstance(execucao.get("tema"), str)
        ):
            usados.add(slug(execucao["tema"]))
    return usados


def pastas_de_hoje():
    saida = ROOT / "output"
    if not saida.exists():
        return []
    prefixo = f"{datetime.now(FUSO):%Y-%m-%d}_"
    return sorted(p for p in saida.iterdir() if p.is_dir() and p.name.startswith(prefixo))


def execucoes_de_hoje(historico):
    hoje = f"{datetime.now(FUSO):%Y-%m-%d}"
    return [
        e for e in historico["execucoes"]
        if isinstance(e, dict) and str(e.get("data", "")).startswith(hoje)
    ]


def checar_consistencia(historico):
    """Compara pastas, histórico e cota de hoje. Não corrige nada.

    Levanta Divergencia se há mais pastas do que a cota registra.
    """
    cota = cota_slideshows.carregar()["quantidade"]
    pastas = pastas_de_hoje()
    execucoes = execucoes_de_hoje(historico)

    if len(pastas) > cota:
        detalhes = "\n".join(f"  - {p.name}" for p in pastas)
        raise Divergencia(
            f"Divergência: há {len(pastas)} pasta(s) de hoje em output/, "
            f"mas a cota registra {cota}.\n{detalhes}\n"
            f"O histórico tem {len(execucoes)} execução(ões) hoje.\n"
            "Nada foi gerado nem alterado. Confira manualmente quais pastas são "
            "apresentações reais (e quais são testes) e, se necessário, ajuste "
            "data/cota_slideshows.json e data/historico.json você mesmo."
        )

    if len(pastas) != cota or len(execucoes) != cota:
        print(
            f"AVISO: pastas hoje={len(pastas)}, histórico hoje={len(execucoes)}, "
            f"cota={cota}. Os valores não coincidem; nada foi corrigido automaticamente."
        )


def validar_apresentacao(pasta, quantidade_esperada):
    pasta = Path(pasta)
    if not pasta.is_dir():
        raise RuntimeError(f"Pasta de saída não existe: {pasta}")

    esperados = {f"slide_{n:02}.png" for n in range(1, quantidade_esperada + 1)}
    encontrados = {p.name for p in pasta.glob("slide_*.png")}

    ausentes = sorted(esperados - encontrados)
    extras = sorted(encontrados - esperados)
    if ausentes or extras:
        raise RuntimeError(
            f"Slides esperados: {quantidade_esperada}; encontrados: {len(encontrados)}. "
            f"Ausentes: {ausentes or 'nenhum'}. Inesperados: {extras or 'nenhum'}."
        )

    for nome in sorted(esperados):
        arquivo = pasta / nome
        try:
            with Image.open(arquivo) as imagem:
                imagem.verify()
            with Image.open(arquivo) as imagem:
                imagem.load()
                tamanho = imagem.size
        except Exception as erro:
            raise RuntimeError(f"Slide inválido: {nome}: {erro}") from erro

        if tamanho != (1080, 1920):
            raise RuntimeError(f"{nome} tem dimensões {tamanho}, não 1080x1920.")

    return len(esperados)


def temas_disponiveis(temas, historico):
    usados = temas_usados(historico)
    existentes = {slug(p.name) for p in pastas_de_hoje()}
    prefixo = f"{datetime.now(FUSO):%Y-%m-%d}_"

    disponiveis = []
    vistos = set()
    for tema in temas:
        s = slug(tema["tema"])
        if s in vistos:
            continue
        vistos.add(s)

        if s in usados:
            continue
        if slug(prefixo + s) in existentes:
            print(f"Tema já gerado hoje; ignorando: {tema['tema']}")
            continue
        disponiveis.append(tema)
    return disponiveis


def escolher_por_argumento(disponiveis, termo):
    alvo = slug(termo)
    exatos = [t for t in disponiveis if slug(t["tema"]) == alvo]
    parciais = exatos or [t for t in disponiveis if alvo in slug(t["tema"])]

    if len(parciais) == 1:
        return parciais[0]

    if not parciais:
        print(f"Nenhum tema disponível encontrado para: {termo}")
    else:
        print(f"Mais de um tema corresponde a '{termo}'. Seja mais específico:")
        disponiveis = parciais

    print("\nTemas disponíveis:")
    for tema in disponiveis:
        print(f"- {tema['tema']}")
    return None


def escolher_interativo(disponiveis):
    print("\nTemas disponíveis para gerar:\n")
    for indice, tema in enumerate(disponiveis, start=1):
        print(f"{indice}. {tema['tema']}")

    try:
        escolha = input("\nDigite o número do tema desejado (Enter cancela): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nCancelado. Nada foi gerado.")
        return None

    if not escolha:
        print("Cancelado. Nada foi gerado.")
        return None
    if not escolha.isdigit():
        print("Escolha inválida. Digite o número de um tema. Nada foi gerado.")
        return None

    indice = int(escolha)
    if indice < 1 or indice > len(disponiveis):
        print("Número fora da lista de temas. Nada foi gerado.")
        return None
    return disponiveis[indice - 1]


def registrar_sucesso(historico, tema):
    """Grava o histórico primeiro e só então incrementa a cota."""
    if slug(tema) not in temas_usados(historico):
        historico["temas_usados"].append(tema)
    historico["execucoes"].append({
        "tema": tema,
        "data": datetime.now(FUSO).isoformat(),
        "status": "sucesso",
    })
    salvar_historico(historico)

    try:
        cota_slideshows.registrar()
    except Exception as erro:
        raise RuntimeError(
            f"A apresentação foi validada e o histórico foi salvo, mas a cota NÃO foi "
            f"atualizada: {erro}. Ajuste data/cota_slideshows.json manualmente."
        ) from erro


def executar(argv=None):
    argv = sys.argv[1:] if argv is None else argv

    temas = carregar_temas()
    if not temas:
        print("Não há temas em data/temas.json. Adicione temas para gerar.")
        return 0

    if not cota_slideshows.verificar():
        print("Limite diário atingido. Tente novamente amanhã.")
        return 0

    historico = carregar_historico()
    checar_consistencia(historico)

    disponiveis = temas_disponiveis(temas, historico)
    if not disponiveis:
        print("Não há temas novos disponíveis hoje.")
        print("Adicione novos temas em data/temas.json.")
        return 0

    if argv:
        escolhido = escolher_por_argumento(disponiveis, " ".join(argv))
    else:
        escolhido = escolher_interativo(disponiveis)

    if escolhido is None:
        return 0

    print(f"\nTema escolhido: {escolhido['tema']}")
    print("Gerando apresentação...")

    pasta = pasta_do_tema(escolhido)
    try:
        pasta = gerar_slideshow(escolhido)
        validados = validar_apresentacao(pasta, len(escolhido["slides"]))
    except Exception as erro:
        print(f"\nFALHA: {erro}", file=sys.stderr)
        print(
            f"Nada foi registrado no histórico nem na cota. "
            f"Se a pasta existir, ela é parcial: {pasta}\n"
            "Revise-a e mova ou apague manualmente antes de tentar de novo.",
            file=sys.stderr,
        )
        return 1

    registrar_sucesso(historico, escolhido["tema"])

    dados_cota = cota_slideshows.carregar()
    print("\nApresentação gerada e validada com sucesso!")
    print(f"Pasta: {pasta}")
    print(f"Slides validados: {validados} (1080x1920)")
    print(
        f"Cota diária: {dados_cota['quantidade']}/{cota_slideshows.LIMITE_DIARIO}"
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(executar())
    except KeyboardInterrupt:
        print("\nCancelado.", file=sys.stderr)
        sys.exit(130)
    except Divergencia as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        sys.exit(2)
    except (ValueError, OSError, RuntimeError) as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        sys.exit(1)
