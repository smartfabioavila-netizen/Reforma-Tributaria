"""Gera simulador.html (Simulador de Impacto por Regime) a partir do texto original + correções."""
import html, json, pathlib

AQUI = pathlib.Path(__file__).parent
BLOCOS = [b["lines"] for b in json.loads((AQUI / "_simulador_original.json").read_text())]


def troca(idx, antigas, novas):
    """Substitui uma sequência exata de linhas do bloco original (falha se não existir)."""
    antigas = antigas if isinstance(antigas, list) else [antigas]
    novas = novas if isinstance(novas, list) else [novas]
    linhas = BLOCOS[idx]
    for i in range(len(linhas)):
        if linhas[i:i + len(antigas)] == antigas:
            linhas[i:i + len(antigas)] = novas
            return
    raise ValueError(antigas)


# ---- Correções técnicas (revisão de out/2026) ----
troca(0, "- Nome da empresa: [NOME]",
      "- Identificação: [Cliente A — não use nome, CNPJ ou CPF]")
troca(0, ["2. Creditamento pleno de IBS/CBS sobre aquisições tributáveis no Lucro Real e",
          "Presumido que optar pelo regime regular."],
      ["2. Creditamento pleno de IBS/CBS sobre aquisições tributáveis no Lucro Real, no",
       "Lucro Presumido e no Simples que optar pelo regime regular de IBS/CBS."])
troca(0, "5. Ignore variações municipais específicas do IBS nesta simulação.",
      ["5. Ignore variações municipais específicas do IBS nesta simulação.",
       "6. IBS/CBS são cobrados por fora: calcule-os sobre a receita líquida dos tributos",
       "atuais (PIS, Cofins, ICMS, ISS, IPI), e não sobre o faturamento bruto.",
       "7. Folha de salários não gera crédito de IBS/CBS.",
       "8. As alíquotas de referência ainda serão fixadas: rotule os números como",
       "estimativa."])
troca(1, "- Nome da empresa: Clínica Sorriso Ltda",
      "- Identificação: Cliente A (clínica odontológica)")

assert max(len(l) for b in BLOCOS for l in b) <= 85, "linha de prompt longa demais"

e = html.escape
pre = lambda i: f"<pre>{e(chr(10).join(BLOCOS[i]))}</pre>"

PASSOS = [
    ("Abra o Claude.ai", 'Acesse <code>claude.ai</code> e entre no Project "Especialista Reforma Tributária 2026" (se você já configurou o agente do kit). Se não configurou, use o chat padrão mesmo.'),
    ("Reúna os dados do cliente", "Você vai precisar de 7 informações básicas. A lista completa está na próxima página."),
    ("Copie o prompt completo", 'Copie o bloco "PROMPT DO SIMULADOR" integralmente. Cole no Claude. Substitua os campos entre colchetes pelos dados do cliente, sem nome, CNPJ ou CPF (use "Cliente A").'),
    ("Receba o relatório pronto", "O Claude devolve o relatório em formato executivo. Revise os números, ajuste premissas se necessário e envie para o cliente."),
]
DADOS = [
    ("Regime tributário atual", "Contrato social / Simples / último DAS / DCTF"),
    ("Atividade principal e CNAE", "Cartão CNPJ"),
    ("Faturamento anual (últimos 12 meses)", "DRE ou extrato de NFs emitidas"),
    ("% de vendas para pessoa física vs jurídica", "Relatório de faturamento por cliente"),
    ("Total de aquisições tributáveis (insumos/serviços)", "Contas a pagar + NFs de entrada"),
    ("Estado e município da sede", "Cartão CNPJ"),
    ("Margem bruta estimada", "DRE do último exercício"),
]
COMPLEMENTARES = [
    ("🔁", "Prompt 1 · Gerar versão para o cliente leigo", 2),
    ("📧", "Prompt 2 · Gerar e-mail de apresentação", 3),
    ("💰", "Prompt 3 · Gerar proposta comercial de consultoria", 4),
    ("🔄", "Prompt 4 · Refazer com premissa diferente", 5),
]
REGRAS = [
    ("Nunca rode sem os 7 dados básicos.", 'Se faltar alguma informação, peça ao cliente antes. Simulação com "chute" compromete toda a recomendação.'),
    ("Confira as alíquotas que o Claude usou.", "No relatório, sempre revise a seção de premissas. A alíquota combinada de referência pode variar por setor — especialmente saúde, educação, transporte e agro."),
    ("Rode 2 cenários para clientes do Simples.", 'Sempre simule "manter no Simples" vs "regime regular híbrido". A decisão aqui pode representar dezenas de milhares de reais ao ano.'),
    ("Valide com o texto da LC 214/2025.", "Antes de apresentar ao cliente, confira artigos citados. O Claude erra menos que o Google, mas erra. A responsabilidade técnica é sua."),
    ("Transforme a simulação em venda.", "Toda simulação vira oportunidade de consultoria paga. Use o Prompt 3 (Proposta comercial) imediatamente depois do diagnóstico."),
]
FAQ = [
    ("Posso usar no Claude gratuito?", "Sim. O prompt funciona no plano gratuito, mas com limite de mensagens. Para uso profissional intenso, considere um plano pago (veja os planos atuais em claude.ai), que libera mais uso e os modelos mais recentes."),
    ("O Claude faz o cálculo sozinho ou eu preciso ter planilha?", "O Claude calcula sozinho, no próprio chat. Você não precisa de Excel. Se quiser, peça também uma tabela em formato CSV e cole na sua planilha depois."),
    ("E se o cliente tiver várias atividades / CNAEs?", 'Rode uma simulação por atividade principal e depois peça ao Claude para consolidar: <i>"consolide os dois resultados em um relatório único com o impacto total da empresa"</i>.'),
    ("A simulação vale como parecer oficial?", "Não. É uma ferramenta de planejamento e apoio à decisão. O parecer oficial, com carimbo e responsabilidade técnica, continua sendo seu."),
]


def cartoes(itens):
    return "\n".join(
        f'<div class="passo"><div class="cab"><span class="num">{i}</span><span class="tit">{t}</span></div><div class="x">{x}</div></div>'
        for i, (t, x) in enumerate(itens, 1))


partes = [f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Simulador de Impacto por Regime Tributário</title>
<link rel="stylesheet" href="base.css"><link rel="stylesheet" href="simulador.css"></head><body>
<section class="capa">
  <div class="selo">Kit Reforma Tributária 2026</div>
  <h1>Simulador de <span>Impacto</span><br>por Regime<br>Tributário.</h1>
  <p class="sub">Um prompt. Três regimes. Estimativa completa em minutos — direto no Claude.ai.</p>
  <div class="linha"></div>
  <div class="meta">Ferramenta · 100% dentro do <b>Claude.ai</b><br>
  Sem planilha · Sem instalar nada · Sem saber Excel avançado<br>
  Base: <b>LC 214/2025</b> · Edição 2026</div>
</section>

<h2 class="secao">O que é este simulador</h2>
<p>Este material te entrega <b>um único prompt estruturado</b> que transforma o Claude em um simulador completo de impacto tributário. Você cola o prompt, preenche os dados do seu cliente e o Claude devolve:</p>
<ul class="lista">
  <li>Carga tributária ATUAL (regime vigente)</li>
  <li>Carga tributária PÓS-REFORMA (com IBS + CBS)</li>
  <li>Diferença em R$ e em %</li>
  <li>Recomendação estratégica (manter regime, migrar, antecipar investimentos)</li>
  <li>Alertas de risco específicos do caso</li>
</ul>
<div class="destaque"><b>Importante:</b> o simulador usa alíquotas de referência da LC 214/2025 e premissas conservadoras. O resultado é uma <b>estimativa de planejamento</b>, não substitui análise caso a caso com documentos reais na mão.</div>

<h2 class="secao">Como usar em 4 passos</h2>
{cartoes(PASSOS)}

<div class="faixa">Dados que você precisa ter em mãos</div>
<p>Antes de rodar o simulador, reúna estas 7 informações do cliente. Sem elas, a simulação perde precisão:</p>
<table class="dados"><tr><th>#</th><th>Informação</th><th>Onde encontrar</th></tr>
{"".join(f"<tr><td>{i}</td><td>{e(a)}</td><td>{e(b)}</td></tr>" for i, (a, b) in enumerate(DADOS, 1))}
</table>
<div class="dica"><b>Dica prática:</b> <i>crie um formulário simples no Google Forms com essas 7 perguntas e envie para o cliente antes da reunião. Em 5 minutos você tem tudo que precisa para rodar o simulador.</i></div>

<div class="faixa">Prompt do simulador · copiar e colar</div>
<p>Este é o prompt completo. <b>Copie tudo</b>, do início ao fim, e cole no Claude.ai.</p>
<div class="etiqueta">PROMPT · SIMULADOR COMPLETO</div>
{pre(0)}

<div class="faixa">Exemplo de uso · caso real preenchido</div>
<p>Para você ver como fica na prática, aqui está o mesmo prompt preenchido com dados de um cliente fictício — basta adaptar a estrutura para seus próprios clientes:</p>
<div class="etiqueta">EXEMPLO · CLÍNICA ODONTOLÓGICA SP</div>
{pre(1)}
<div class="dica"><b>Observação:</b> <i>serviços de saúde, como os odontológicos, têm redução de 60% nas alíquotas de IBS/CBS (LC 214/2025, conforme o enquadramento na NBS). Com 26,5% de referência, a alíquota efetiva fica em torno de 10,6%. Informe o setor corretamente e confira, na seção de premissas, se o Claude aplicou a redução.</i></div>

<div class="faixa">Prompts complementares · aprofundamentos</div>
<p>Depois de rodar a simulação principal, use estes prompts curtos para gerar materiais derivados — todos dentro da mesma conversa no Claude:</p>
"""]
for emoji, titulo, idx in COMPLEMENTARES:
    partes.append(f'<div class="comp"><h3><span class="emoji">{emoji}</span> {e(titulo)}</h3>{pre(idx)}</div>')
partes.append(f"""
<div class="faixa">5 regras de ouro para simulações precisas</div>
{cartoes(REGRAS)}

<div class="faixa">Perguntas rápidas</div>
{"".join(f'<div class="faq"><h3>{e(q)}</h3><p>{a}</p></div>' for q, a in FAQ)}

<div class="cta"><div class="t">Agora é rodar.</div>
<div class="l">Copie o prompt · Preencha os dados · Receba o relatório.<br>3 minutos do seu tempo = 1 cliente mais bem atendido.</div></div>
<div class="rodape">© 2026 Claude para Contadores · Kit Reforma Tributária 2026<br>
Uso individual e intransferível · Material baseado na LC 214/2025<br>
Não substitui o julgamento profissional do contador habilitado · Sem vínculo com a Anthropic.</div>
</body></html>""")
(AQUI / "simulador.html").write_text("\n".join(partes))
