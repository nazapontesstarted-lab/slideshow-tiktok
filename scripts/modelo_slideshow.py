
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
LARGURA, ALTURA = 1080, 1920
FUSO = ZoneInfo("America/Sao_Paulo")

FUNDO = "#F7F1E8"
TEXTO = "#202020"
DESTAQUE = "#E87532"
SECUNDARIA = "#6B625A"


def carregar_fonte(tamanho):
    for caminho in (
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
    ):
        if Path(caminho).exists():
            return ImageFont.truetype(caminho, tamanho)
    return ImageFont.load_default()


def quebrar_linhas(texto, fonte, largura_maxima, desenho):
    linhas = []
    linha = ""

    for palavra in texto.split():
        tentativa = f"{linha} {palavra}".strip()
        caixa = desenho.textbbox((0, 0), tentativa, font=fonte)

        if caixa[2] - caixa[0] <= largura_maxima:
            linha = tentativa
        else:
            if linha:
                linhas.append(linha)
            linha = palavra

    if linha:
        linhas.append(linha)

    return linhas


def desenhar_texto(desenho, texto, y, fonte, largura, cor, espacamento=18):
    linhas = quebrar_linhas(texto, fonte, largura, desenho)

    for linha in linhas:
        caixa = desenho.textbbox((0, 0), linha, font=fonte)
        altura_linha = caixa[3] - caixa[1]
        largura_linha = caixa[2] - caixa[0]
        x = (LARGURA - largura_linha) // 2
        desenho.text((x, y), linha, font=fonte, fill=cor)
        y += altura_linha + espacamento

    return y


def criar_slide(slide, numero, total, pasta_saida, tema):
    imagem = Image.new("RGB", (LARGURA, ALTURA), FUNDO)
    desenho = ImageDraw.Draw(imagem)

    margem = 100
    desenho.text(
        (margem, 95),
        "GUIA PRÁTICO",
        font=carregar_fonte(30),
        fill=DESTAQUE,
    )
    desenho.rounded_rectangle(
        (margem, 155, margem + 100, 166),
        radius=5,
        fill=DESTAQUE,
    )

    desenhar_texto(
        desenho, slide["titulo"], 330,
        carregar_fonte(76), LARGURA - 2 * margem,
        TEXTO, 20,
    )

    desenhar_texto(
        desenho, slide["texto"], 650,
        carregar_fonte(43), LARGURA - 2 * margem,
        SECUNDARIA, 22,
    )

    desenho.text(
        (margem, ALTURA - 125),
        "SALVE PARA CONSULTAR DEPOIS",
        font=carregar_fonte(27),
        fill=SECUNDARIA,
    )
    desenho.text(
        (LARGURA - margem - 100, ALTURA - 125),
        f"{numero:02}/{total:02}",
        font=carregar_fonte(27),
        fill=DESTAQUE,
    )

    destino = pasta_saida / f"slide_{numero:02}.png"
    imagem.save(destino, "PNG")
    print(f"Criado: {destino}")


def slug(texto):
    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ascii", "ignore").decode("ascii")
    texto = re.sub(r"[^a-zA-Z0-9]+", "_", texto.lower())
    return texto.strip("_") or "slideshow"


def carregar_temas():
    arquivo = ROOT / "data" / "temas.json"

    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo}")

    dados = json.loads(arquivo.read_text(encoding="utf-8"))

    if not isinstance(dados, list):
        raise ValueError("temas.json precisa conter uma lista de temas.")

    for item in dados:
        if not isinstance(item, dict):
            raise ValueError("Cada tema em temas.json precisa ser um objeto.")
        if not item.get("tema") or not isinstance(item.get("slides"), list):
            raise ValueError("Cada tema precisa de 'tema' e uma lista 'slides'.")
        if len(item["slides"]) < 6:
            raise ValueError(f"O tema '{item['tema']}' precisa de pelo menos 6 slides.")
        for slide in item["slides"]:
            if not isinstance(slide, dict):
                raise ValueError("Cada slide precisa ser um objeto.")
            if not slide.get("titulo") or not slide.get("texto"):
                raise ValueError("Cada slide precisa de 'titulo' e 'texto'.")

    return dados


def pasta_do_tema(item):
    return (
        ROOT / "output" /
        f"{datetime.now(FUSO):%Y-%m-%d}_{slug(item['tema'])}"
    )


def gerar_slideshow(item):
    pasta_saida = pasta_do_tema(item)

    if pasta_saida.exists():
        raise FileExistsError(
            f"Este tema já tem uma pasta de saída: {pasta_saida}\n"
            "Escolha outro tema ou mova a pasta existente."
        )

    pasta_saida.mkdir(parents=True)

    slides = item["slides"]

    for numero, slide in enumerate(slides, start=1):
        criar_slide(slide, numero, len(slides), pasta_saida, item["tema"])

    (pasta_saida / "conteudo.json").write_text(
        json.dumps(item, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\nApresentação criada em: {pasta_saida}")
    return pasta_saida


if __name__ == "__main__":
    try:
        temas = carregar_temas()

        if not temas:
            raise ValueError("temas.json não contém nenhum tema.")

        if len(sys.argv) > 1:
            termo = " ".join(sys.argv[1:]).casefold()
            encontrados = [
                item for item in temas
                if termo in item["tema"].casefold()
            ]
            if not encontrados:
                raise ValueError(f"Nenhum tema encontrado para: {termo}")
            selecionado = encontrados[0]
        else:
            selecionado = temas[0]

        gerar_slideshow(selecionado)

    except (ValueError, FileNotFoundError, FileExistsError, json.JSONDecodeError) as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        sys.exit(1)
