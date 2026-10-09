#!/usr/bin/env bash
# Gera os PDFs corrigidos do kit a partir de kit-corrigido/fontes.
# Requisitos: WeasyPrint 66 (mesma versão dos originais) e as fontes
# Nimbus Sans/Roman (pacote fonts-urw-base35), Liberation Serif/Mono e Noto Color Emoji.
set -euo pipefail
cd "$(dirname "$0")"
WEASY=${WEASYPRINT:-weasyprint}
PY=${PYTHON:-python3}
$PY prompts.py
$PY simulador.py
$WEASY prompts.html   ../kit_reforma_tributaria_15_prompts.pdf
$WEASY simulador.html ../simulador_impacto_reforma_tributaria.pdf
$WEASY mapa.html      ../mapa_visual_transicao_reforma_2026_2033.pdf
ls -la ../*.pdf
