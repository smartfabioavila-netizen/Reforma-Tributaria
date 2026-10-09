"""Gera prompts.html (15 Prompts Prontos) a partir do texto original + correções."""
import html, json, pathlib

AQUI = pathlib.Path(__file__).parent
BLOCOS = [b["lines"] for b in json.loads((AQUI / "_prompts_original.json").read_text())]


def troca(idx, antiga, nova):
    """Substitui uma linha exata do prompt original (falha se não existir)."""
    linhas = BLOCOS[idx]
    i = linhas.index(antiga)
    linhas[i:i + 1] = nova if isinstance(nova, list) else [nova]


# ---- Correções técnicas (revisão de out/2026) ----
troca(1, "2. Alíquota média",
      "2. Alíquota média (se ainda não definida, use estimativa e rotule)")
troca(2, "1. O QUE É: definição em 2 frases.",
      "1. O QUE É: definição em 2 frases + o que ainda depende de regulamento.")
troca(4, "2. Carga tributária com IBS + CBS na alíquota padrão de referência",
      ["2. Carga tributária com IBS + CBS na alíquota padrão de referência",
       "(estimativa; IBS/CBS calculados por fora; folha não gera crédito)"])
troca(6, "4. Prazo e forma de formalizar a opção",
      ["4. Prazo e forma de formalizar a opção (cite o dispositivo legal e",
       "sinalize o que ainda depende de regulamentação)"])
troca(12, "1. CADASTROS (produtos, CFOP, NCM, CST)",
      "1. CADASTROS (produtos, CFOP, NCM/NBS, CST e cClassTrib de IBS/CBS)")
troca(12, "3. LAYOUT DA NOTA (novos campos obrigatórios)",
      "3. LAYOUT DA NOTA (novos campos de IBS/CBS na NF-e e na NFS-e nacional)")

assert max(len(l) for b in BLOCOS for l in b) <= 75, "linha de prompt longa demais"

PROMPTS = [
    ("A · Entendimento da Reforma", "CBS explicado em linguagem de cliente",
     'cliente pergunta "o que é essa tal CBS?"',
     "peça para o Claude adaptar a explicação ao setor do seu cliente (comércio, serviço, indústria)."),
    (None, "IBS vs ICMS e ISS — o que muda",
     "cliente quer entender a diferença dos impostos antigos e o novo",
     "peça a saída em formato Markdown para colar direto em relatórios."),
    (None, "Split Payment descomplicado",
     'cliente não entende como vai pagar imposto "dividido"',
     "guarde a resposta — serve como roteiro de reunião."),
    (None, "Cronograma de transição 2026–2033",
     "cliente quer saber quando tudo isso começa de verdade",
     "transforme o resultado em infográfico no Canva para enviar aos clientes."),
    ("B · Impacto no Cliente", "Simulação de carga tributária comparativa",
     "cliente quer saber se vai pagar mais ou menos imposto",
     "use esse prompt como serviço pago — consultoria de impacto tributário."),
    (None, "Análise por setor de atuação",
     "cliente quer saber como o setor dele será afetado",
     "crie um relatório por setor e ofereça como brinde na captação."),
    (None, "Simples Nacional — aderir ao IBS/CBS?",
     "cliente no Simples precisa decidir se opta pelo regime regular do IBS/CBS",
     "esse é um dos prompts que mais gera receita de consultoria."),
    (None, "Aproveitamento de créditos no Lucro Real",
     "cliente do Lucro Real quer maximizar créditos no período de transição",
     "transforme esse plano em proposta de consultoria recorrente."),
    ("C · Comunicação com Cliente", "E-mail explicativo para clientes",
     "disparo em massa para a base do escritório",
     "peça 3 versões com tons diferentes (formal, próximo, urgente)."),
    (None, "FAQ de dúvidas recorrentes",
     "criar material de apoio para enviar aos clientes",
     "esse FAQ pode virar lead magnet na sua captação."),
    (None, "Post de LinkedIn posicionando autoridade",
     "publicar conteúdo que gere confiança e atraia clientes",
     "rode esse prompt 1x por semana com temas diferentes e alimente seu feed por meses."),
    (None, "Roteiro de reunião com o cliente",
     "cliente aceitou a reunião — você precisa conduzir com segurança",
     "use o mesmo prompt como base para oferecer consultoria paga de diagnóstico."),
    ("D · Operacional do Escritório", "Ajustes no sistema emissor de NF-e",
     "chegou a hora de parametrizar o ERP do cliente",
     "esse checklist é ouro — cobre por projeto de adaptação."),
    (None, "Revisão de cláusulas contratuais",
     "contratos antigos precisam de cláusula de reajuste tributário",
     "ofereça esse serviço em parceria com um advogado — divide honorários."),
    (None, "Checklist de adaptação do escritório",
     "o SEU escritório precisa estar pronto antes de atender clientes",
     "esse é o único prompt que o contador usa em si mesmo. Priorize."),
]
CATEGORIAS = ["Entendimento"] * 4 + ["Impacto"] * 4 + ["Comunicação"] * 4 + ["Operacional"] * 3
TITULOS_INDICE = [
    "CBS explicado em linguagem de cliente", "IBS vs ICMS e ISS — o que muda",
    "Split Payment descomplicado", "Cronograma de transição 2026–2033",
    "Simulação de carga tributária comparativa", "Análise por setor de atuação do cliente",
    "Simples Nacional — aderir ao IBS/CBS?", "Aproveitamento de créditos no Lucro Real",
    "E-mail explicativo para clientes", "FAQ de dúvidas recorrentes",
    "Post de LinkedIn posicionando autoridade", "Roteiro de reunião com o cliente",
    "Ajustes no sistema emissor de NF-e", "Revisão de cláusulas contratuais",
    "Checklist de adaptação do escritório",
]
DICAS_FINAIS = [
    ("1. Personalize sempre",
     "Troque as informações entre colchetes pelos dados do cliente (sem nome, CNPJ ou CPF). "
     "Quanto mais específico, melhor o Claude responde."),
    ("2. Use o modelo certo",
     "No Claude.ai, use o <b>modelo mais recente disponível</b> para respostas longas e analíticas. "
     "Para tarefas rápidas, <b>um modelo mais leve</b> é suficiente."),
    ("3. Peça o formato de saída",
     "Sempre que quiser tabela, checklist, e-mail ou relatório, <b>peça explicitamente no final do prompt</b>. "
     "Isso muda totalmente a qualidade da resposta."),
    ("4. Valide antes de enviar ao cliente",
     "O Claude é excelente, mas <b>o julgamento técnico é sempre seu</b>. "
     "Revise números, alíquotas e prazos antes de qualquer envio oficial."),
    ("5. Combine com os Agentes",
     "Estes prompts ficam ainda mais poderosos quando usados junto ao "
     "<b>Agente Especialista em Reforma Tributária</b> incluído no seu kit."),
]

e = html.escape
partes = ["""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>15 Prompts Prontos</title>
<link rel="stylesheet" href="base.css"><link rel="stylesheet" href="prompts.css"></head><body>
<section class="capa">
  <div class="selo">Kit Reforma Tributária 2026</div>
  <h1>15 Prompts <span>Prontos</span><br>para o Contador<br>na Nova Era.</h1>
  <p class="sub">Responda qualquer dúvida sobre CBS, IBS e Split Payment em 30 segundos —<br>sem estudar 400 páginas de lei.</p>
  <div class="linha"></div>
  <div class="meta">Material exclusivo · Uso no <b>Claude.ai</b><br>
  Baseado na <b>Lei Complementar 214/2025</b><br>
  Edição 2026 · Atualizado para o período de transição</div>
</section>
<section class="intro">
  <h2 class="secao">Antes de começar</h2>
  <p>Este material foi desenhado para contadores que <b>não têm tempo de estudar a Reforma Tributária do zero</b> — mas precisam responder clientes com segurança desde já.</p>
  <p>Cada prompt foi testado no Claude e gera respostas prontas para você copiar, adaptar ao seu cliente e enviar.</p>
  <div class="destaque"><b>Como usar:</b> Copie o prompt, cole no Claude.ai, substitua as informações entre colchetes <b>[assim]</b> pelos dados do seu cliente e pronto. Não cole nome, CNPJ ou CPF do cliente: use "Cliente A" (LGPD).</div>
  <div class="faixa">Índice dos 15 prompts</div>
  <table class="indice">"""]
for i, (t, c) in enumerate(zip(TITULOS_INDICE, CATEGORIAS), 1):
    partes.append(f'<tr><td class="n">{i:02d}</td><td class="c">{c}</td><td>{e(t)}</td></tr>')
partes.append("</table></section>")

for i, ((bloco, titulo, quando, dica), linhas) in enumerate(zip(PROMPTS, BLOCOS), 1):
    if bloco:
        partes.append(f'<div class="faixa bloco">Bloco {e(bloco)}</div>')
    partes.append(f"""<div class="card">
  <div class="cab"><span class="num">{i}</span><span class="tit">{e(titulo)}</span></div>
  <div class="quando">Quando usar: {e(quando)}</div>
  <div class="rot">Prompt</div>
  <pre>{e(chr(10).join(linhas))}</pre>
  <div class="dica"><b>Dica:</b> {e(dica)}</div>
</div>""")

partes.append('<h2 class="secao final">Como extrair o máximo destes prompts</h2>')
for t, txt in DICAS_FINAIS:
    partes.append(f'<div class="dfinal"><div class="t">{t}</div><div class="x">{txt}</div></div>')
partes.append("""<div class="cta"><div class="t">Agora é com você.</div>
<div class="l">15 prompts · 4 blocos · 1 reforma · Infinitas respostas.<br>Copie. Cole. Feche o mês com segurança.</div></div>
<div class="rodape">© 2026 Claude para Contadores · Uso individual e intransferível<br>
Material baseado na LC 214/2025 · Não substitui o julgamento profissional do contador habilitado<br>
Alíquotas de referência de CBS e IBS ainda serão fixadas por resolução do Senado Federal · valores usados são estimativas<br>
Este material não possui vínculo com a Anthropic.</div>
</body></html>""")
(AQUI / "prompts.html").write_text("\n".join(partes))
