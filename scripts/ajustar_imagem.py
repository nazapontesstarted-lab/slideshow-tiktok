
import sys
from pathlib import Path
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
LARGURA = 1080
ALTURA = 1920


def ajustar(entrada: str, saida: str) -> None:
    origem = Path(entrada)
    destino = Path(saida)

    if not origem.is_absolute():
        origem = ROOT / origem
    if not destino.is_absolute():
        destino = ROOT / destino

    if not origem.is_file():
        raise FileNotFoundError(f"Imagem não encontrada: {origem}")

    destino.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(origem) as original:
        imagem = original.convert("RGB")
        proporcao_alvo = LARGURA / ALTURA
        proporcao_original = imagem.width / imagem.height

        # Recorte central para 9:16, sem distorcer a imagem.
        if proporcao_original > proporcao_alvo:
            nova_largura = round(imagem.height * proporcao_alvo)
            esquerda = (imagem.width - nova_largura) // 2
            imagem = imagem.crop(
                (esquerda, 0, esquerda + nova_largura, imagem.height)
            )
        else:
            nova_altura = round(imagem.width / proporcao_alvo)
            topo = (imagem.height - nova_altura) // 2
            imagem = imagem.crop(
                (0, topo, imagem.width, topo + nova_altura)
            )

        imagem = imagem.resize(
            (LARGURA, ALTURA),
            Image.Resampling.LANCZOS,
        )

        imagem.save(destino, "PNG", optimize=True)

    print(f"Imagem ajustada: {destino}")
    print(f"Resolução final: {LARGURA} x {ALTURA}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            'Uso: python scripts/ajustar_imagem.py '
            '"entrada.png" "saida.png"'
        )
        sys.exit(2)

    try:
        ajustar(sys.argv[1], sys.argv[2])
    except Exception as erro:
        print(f"ERRO: {erro}", file=sys.stderr)
        sys.exit(1)
