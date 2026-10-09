# KIT · Claude para Reforma Tributária 2026

Materiais do kit, recriados a partir da estrutura do curso.

## Entregáveis (`entregaveis/`)

| Módulo | Arquivo | Conteúdo |
|---|---|---|
| 1 · Comece Aqui | `guia_comece_aqui_claude_reforma_tributaria.pdf` | Configuração do Claude, ordem de uso, cuidados profissionais e plano de 7 dias |
| Agente | `agente_especialista_reforma_tributaria_2026.md` | Instruções de Projeto do Claude: "Especialista em Reforma Tributária 2026" |
| 02 · 15 Prompts Prontos | `kit_reforma_tributaria_15_prompts.pdf` | 15 prompts em 4 blocos: explicar, diagnosticar, agir e organizar |
| 03 · 5 E-mails Prontos | `emails_prontos_reforma_tributaria_2026.docx` | Comunicado geral, ano-teste 2026, convite para diagnóstico, Simples Nacional e proposta de serviço |
| 04 · Simulador de Impacto | `simulador_impacto_reforma_tributaria.pdf` | Prompt-mestre, metodologia e 3 exemplos resolvidos (Presumido, Real e Simples) |
| 05 · Mapa Visual | `mapa_visual_transicao_reforma_2026_2033.pdf` | Linha do tempo 2026 → 2033 e ações por fase (A4 paisagem) |

## Como editar e gerar de novo

Os textos ficam em `fontes/` (Markdown e, no caso do mapa, HTML). Depois de editar, rode:

```bash
kit/build/gerar.sh
```

Requisitos: `pandoc`, Node.js com o pacote `playwright` (local ou global) e as fontes Inter e DejaVu.
Se o Chromium não estiver no caminho padrão do Playwright, informe-o em `CHROMIUM_PATH`.

## Base técnica

Os conteúdos seguem a EC 132/2023 e a LC 214/2025. As alíquotas de referência (CBS ≈ 8,8% + IBS ≈ 17,7% = 26,5%) são **estimativas ilustrativas**. Revise os materiais sempre que sair nova regulamentação.
