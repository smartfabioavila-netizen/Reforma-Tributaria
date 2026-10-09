#!/usr/bin/env bash
# Gera os entregáveis do kit a partir de kit/fontes.
set -euo pipefail
cd "$(dirname "$0")"
FONTES=../fontes
SAIDA=../entregaveis
TMP=$(mktemp -d)
export NODE_PATH=$(npm root -g)

pdf_md() { # fonte.md saida.pdf titulo
  pandoc "$FONTES/$1" -f markdown -t html5 --template template.html \
    --metadata title="$3" -o "$TMP/${1%.md}.html"
  cp estilo.css "$TMP/"
  node pdf.cjs "$TMP/${1%.md}.html" "$SAIDA/$2"
}

pdf_md 00-comece-aqui.md          guia_comece_aqui_claude_reforma_tributaria.pdf "Comece Aqui"
pdf_md 02-15-prompts.md           kit_reforma_tributaria_15_prompts.pdf          "15 Prompts Prontos"
pdf_md 04-simulador.md            simulador_impacto_reforma_tributaria.pdf       "Simulador de Impacto por Regime"

cp estilo.css "$TMP/" && cp "$FONTES/05-mapa-transicao.html" "$TMP/"
node pdf.cjs "$TMP/05-mapa-transicao.html" "$SAIDA/mapa_visual_transicao_reforma_2026_2033.pdf" paisagem

pandoc "$FONTES/03-emails.md" -f markdown -t docx --reference-doc=referencia.docx \
  -o "$SAIDA/emails_prontos_reforma_tributaria_2026.docx"

cp "$FONTES/01-agente-especialista.md" "$SAIDA/agente_especialista_reforma_tributaria_2026.md"

rm -rf "$TMP"
ls -la "$SAIDA"
