# Kit Reforma Tributária 2026 · versão corrigida

Versão revisada dos 4 materiais originais do kit (out/2026). O visual, a estrutura e o texto foram mantidos; mudaram apenas os pontos técnicos listados abaixo.

| Arquivo | Páginas | Como foi corrigido |
|---|---|---|
| `kit_reforma_tributaria_15_prompts.pdf` | 16 (igual ao original) | Recriado a partir do HTML (`fontes/`) |
| `mapa_visual_transicao_reforma_2026_2033.pdf` | 5 (igual) | Recriado a partir do HTML (`fontes/`) |
| `simulador_impacto_reforma_tributaria.pdf` | 8 (igual) | Recriado a partir do HTML (`fontes/`) |
| `emails_prontos_reforma_tributaria_2026.docx` | — | Editado direto no .docx original (formatação preservada) |

Os originais estão em `../originais/v1/`.

## O que mudou

### 🔴 Correções críticas
- **Split payment não é obrigatório em 2027.** A lei prevê o mecanismo com implantação gradual, conforme regulamentação. Ajustado no Mapa (visão geral, ano de 2027, quadro de ações e caixa de atenção) e nos E-mails 2 e 4. O título do E-mail 4 passou a ser "Atenção ao seu fluxo de caixa com o Split Payment".
- **LGPD.** Foram incluídos avisos para não colar nome, CNPJ ou CPF do cliente: em "Como usar" e na dica final dos Prompts, e no passo 3 do Simulador. No prompt do Simulador, o campo `Nome da empresa` virou `Identificação: [Cliente A …]`, e o exemplo da clínica foi anonimizado.
- **Modelo e preço do Claude.** Foram retiradas as menções a "Sonnet 4.5", "Haiku" e "Plano Pro US$ 20/mês". Agora o texto diz "modelo mais recente disponível" e "veja os planos atuais em claude.ai".

### 🟡 Correções técnicas
**Mapa Visual**
- 2026: o texto agora diz que quem cumpre as obrigações acessórias fica dispensado do recolhimento. Novo item: "Simples Nacional fora do ano-teste".
- 2027: novos itens sobre o **IPI zerado** (exceto ZFM) e sobre a **opção do Simples** pelo regime regular de IBS/CBS.
- 2028: "começam a acumular créditos de CBS" virou "consolidam a gestão dos créditos". Os créditos começam em 2027.
- 2030 a 2032: o percentual do IBS agora traz "do pleno" (ex.: "IBS a 20% do pleno").
- 2032: novo item sobre o **fim dos benefícios fiscais de ICMS**.
- 2033: "encerramento de créditos residuais" virou "habilitar saldos credores de ICMS (compensação com IBS ou ressarcimento)".

**Simulador**
- Capa: "Números precisos em 30 segundos" virou "Estimativa completa em minutos".
- Premissa 2: o Lucro Presumido já está no regime regular. Só o Simples opta.
- Novas premissas no prompt: **6.** IBS/CBS calculados por fora, sobre a receita líquida dos tributos atuais; **7.** folha de salários não gera crédito; **8.** alíquotas rotuladas como estimativa.
- Exemplo da clínica: a observação agora explica a **redução de 60%** para saúde, com alíquota efetiva de cerca de 10,6%.

**15 Prompts**
- Prompt 2: a "alíquota média" deve vir rotulada como estimativa.
- Prompt 3: o prompt passa a pedir o que ainda depende de regulamento.
- Prompt 5: premissas de cálculo por fora e de que a folha não gera crédito.
- Prompt 7: pede o dispositivo legal e sinaliza o que depende de regulamentação.
- Prompt 13: inclui NCM/NBS, CST e cClassTrib de IBS/CBS e a NFS-e nacional.

**E-mails**
- E-mails 1 e 2: o que o escritório "já fez" virou campo editável, para o modelo não prometer trabalho que não foi feito.
- Dicas sem fonte foram suavizadas: "abertura 30% maior" e "taxa de resposta cai pela metade".

## Como gerar os PDFs de novo

```bash
kit-corrigido/fontes/gerar.sh
```

Requisitos: **WeasyPrint 66** (a mesma versão dos originais) e as fontes Nimbus Sans/Roman (`fonts-urw-base35`), Liberation Serif/Mono e Noto Color Emoji. O texto dos prompts fica em `fontes/_*_original.json` e as correções aparecem como chamadas `troca(...)` em `prompts.py` e `simulador.py`.
