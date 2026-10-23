
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json

ROOT = Path(__file__).resolve().parent.parent
ARQUIVO = ROOT / "data" / "cota_slideshows.json"
FUSO = ZoneInfo("America/Sao_Paulo")
LIMITE_DIARIO = 5


def hoje():
    return datetime.now(FUSO).date().isoformat()


def carregar():
    if not ARQUIVO.exists():
        return {"data": hoje(), "quantidade": 0}

    try:
        dados = json.loads(ARQUIVO.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        raise ValueError(f"{ARQUIVO} é um JSON inválido: {erro}") from erro

    if not isinstance(dados, dict):
        dados = {}
    quantidade = dados.get("quantidade")
    if (
        not isinstance(dados.get("data"), str)
        or not isinstance(quantidade, int)
        or isinstance(quantidade, bool)
        or quantidade < 0
    ):
        raise ValueError(
            f"{ARQUIVO} precisa ter 'data' (texto) e 'quantidade' (inteiro >= 0). "
            "Corrija manualmente; o script não altera esse valor."
        )

    if dados["data"] != hoje():
        return {"data": hoje(), "quantidade": 0}

    return dados


def verificar():
    dados = carregar()
    restante = max(0, LIMITE_DIARIO - dados["quantidade"])

    print(f"Apresentações hoje: {dados['quantidade']}/{LIMITE_DIARIO}")
    print(f"Restantes hoje: {restante}")

    return restante > 0


def registrar():
    dados = carregar()

    if dados["quantidade"] >= LIMITE_DIARIO:
        raise RuntimeError("Limite diário de apresentações atingido.")

    dados["quantidade"] += 1
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)

    temporario = ARQUIVO.with_suffix(".tmp")
    temporario.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporario.replace(ARQUIVO)

    print(f"Cota atualizada: {dados['quantidade']}/{LIMITE_DIARIO}")


if __name__ == "__main__":
    verificar()
