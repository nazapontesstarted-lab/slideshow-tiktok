
import json
import os
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
ARQUIVO = ROOT / "data" / "cota_diaria.json"
FUSO = ZoneInfo("America/Sao_Paulo")


def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return {}


def salvar(dados):
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    temporario = ARQUIVO.with_suffix(".tmp")
    temporario.write_text(
        json.dumps(dados, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporario.replace(ARQUIVO)


def limite():
    return max(0, int(os.getenv("DAILY_IMAGE_LIMIT", "5")))


def verificar():
    hoje = datetime.now(FUSO).date().isoformat()
    dados = carregar()
    registro = dados.get(hoje, {"geradas": 0})
    usadas = int(registro.get("geradas", 0))
    maximo = limite()

    print(f"Data (São Paulo): {hoje}")
    print(f"Imagens registradas: {usadas}")
    print(f"Limite local diário: {maximo}")
    print(f"Restantes no limite local: {max(0, maximo - usadas)}")

    return usadas < maximo


def registrar():
    hoje = datetime.now(FUSO).date().isoformat()
    dados = carregar()
    registro = dados.setdefault(hoje, {"geradas": 0})

    if int(registro.get("geradas", 0)) >= limite():
        raise RuntimeError("Limite local diário atingido.")

    registro["geradas"] = int(registro.get("geradas", 0)) + 1
    salvar(dados)
    print(f"Imagem registrada. Total hoje: {registro['geradas']}")


if __name__ == "__main__":
    comando = sys.argv[1] if len(sys.argv) > 1 else "verificar"

    if comando == "verificar":
        sys.exit(0 if verificar() else 1)
    elif comando == "registrar":
        registrar()
    else:
        print("Uso: python scripts/cota.py [verificar|registrar]")
        sys.exit(2)
