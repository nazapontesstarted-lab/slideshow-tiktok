
import os
import sys
import base64
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from cota import verificar, registrar

load_dotenv(ROOT / ".env")


def gerar_imagem(prompt: str, seed: int, saida: str) -> None:
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
    token = os.getenv("CLOUDFLARE_API_TOKEN")
    modelo = os.getenv(
        "CF_IMAGE_MODEL",
        "@cf/black-forest-labs/flux-1-schnell",
    )

    if not account_id or not token:
        raise RuntimeError(
            "Configure CLOUDFLARE_ACCOUNT_ID e "
            "CLOUDFLARE_API_TOKEN no arquivo .env."
        )

    # Verifica a cota antes de chamar a API.
    if not verificar():
        raise RuntimeError(
            "Limite diário local atingido. Tente novamente amanhã."
        )

    url = (
        "https://api.cloudflare.com/client/v4/accounts/"
        f"{account_id}/ai/run/{modelo}"
    )

    print(f"Modelo: {modelo}")
    print("Enviando prompt para a Cloudflare...")

    resposta = requests.post(
        url,
        headers={"Authorization": f"Bearer {token}"},
        json={"prompt": prompt, "steps": 4},
        timeout=180,
    )

    if not resposta.ok:
        raise RuntimeError(
            f"Cloudflare HTTP {resposta.status_code}: "
            f"{resposta.text[:1000]}"
        )

    content_type = resposta.headers.get("content-type", "")

    if "image/" in content_type:
        dados_imagem = resposta.content
    else:
        dados = resposta.json()
        resultado = dados.get("result") or {}
        imagem_b64 = resultado.get("image")

        if not imagem_b64:
            raise RuntimeError(
                "A resposta não contém result.image. "
                f"Campos recebidos: {list(dados.keys())}"
            )

        dados_imagem = base64.b64decode(imagem_b64)

    destino = Path(saida)
    if not destino.is_absolute():
        destino = ROOT / destino

    destino.parent.mkdir(parents=True, exist_ok=True)

    try:
        with Image.open(BytesIO(dados_imagem)) as imagem:
            imagem.load()
            imagem = imagem.convert("RGB")
            imagem.save(destino, format="PNG")
    except Exception as erro:
        raise RuntimeError(
            f"Não foi possível validar a imagem: {erro}"
        ) from erro

    # Registra somente depois de salvar a imagem.
    registrar()

    print(f"Imagem salva: {destino}")
    print(f"Dimensões: {imagem.width} x {imagem.height}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            'Uso: python scripts/gerar_imagem.py '
            '"PROMPT" SEED "ARQUIVO.png"'
        )
        sys.exit(2)

    try:
        gerar_imagem(
            prompt=sys.argv[1],
            seed=int(sys.argv[2]),
            saida=sys.argv[3],
        )
    except (
        ValueError,
        RuntimeError,
        requests.RequestException,
    ) as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        sys.exit(1)
