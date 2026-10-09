```{=html}
<section class="capa">
  <div>
    <div class="selo">Material 02 · Reforma Tributária na Prática</div>
    <h1>15 Prompts Prontos para Contadores</h1>
    <div class="sub">Comandos prontos para tirar dúvidas, diagnosticar clientes e organizar o escritório para a transição de 2026 a 2033, direto no Claude.</div>
  </div>
  <div class="rodape">Use dentro do Projeto com o agente "Especialista em Reforma Tributária 2026" instalado</div>
</section>
```

# Como usar este material

1. Abra o **Projeto** em que você instalou o agente especialista (veja o guia *Comece Aqui*).
2. Copie o prompt, cole no Claude e **troque tudo o que estiver entre `[colchetes]`**.
3. Nunca cole nome, CNPJ ou CPF do cliente. Use "Cliente A", "Cliente B".
4. Confira a base legal citada antes de enviar qualquer conclusão ao cliente.

| Bloco | Prompts |
|---|---|
| **Entender e explicar** | 1 · Explicar a reforma ao cliente leigo · 2 · Linha do tempo personalizada · 3 · Responder dúvida com fundamentação |
| **Diagnosticar o cliente** | 4 · Diagnóstico de impacto por regime · 5 · Enquadramento em alíquota reduzida ou zero · 6 · Mapa de créditos na cadeia · 7 · Simples: DAS ou regime regular · 8 · Exposição ao Imposto Seletivo · 9 · Benefícios de ICMS até 2032 |
| **Agir** | 10 · Revisão de preços · 11 · Contratos de longo prazo · 12 · Split payment e caixa · 13 · Checklist do ano-teste 2026 |
| **Organizar o escritório** | 14 · Triagem da carteira · 15 · Roteiro de reunião com o cliente |

<div class="aviso">

**Lembrete profissional:** os prompts aceleram a análise, mas a conclusão é sua. Confirme dispositivos legais, alíquotas e prazos na legislação vigente (EC 132/2023, LC 214/2025 e regulamentação posterior) antes de orientar o cliente.

</div>

```{=html}
<div class="quebra"></div>
```

::: ficha
## 1 · Explicar a reforma para um cliente leigo

[Entender e explicar]{.tag} **Quando usar:** primeira conversa com um cliente que "ouviu falar" da reforma e está preocupado.

```
Explique a Reforma Tributária do consumo para um empresário sem formação
contábil, dono de [TIPO DE NEGÓCIO, ex.: uma loja de materiais de construção]
optante pelo [REGIME TRIBUTÁRIO].

Regras:
- No máximo 12 frases curtas, sem siglas sem explicação.
- Use uma analogia do dia a dia do negócio dele.
- Diga o que muda em 2026, em 2027 e até 2033, só no que afeta esse tipo de negócio.
- Termine com 3 coisas que ele precisa fazer agora junto com o contador.
```

**Dica:** peça em seguida "transforme isso em uma mensagem de WhatsApp" ou "em um roteiro de áudio de 1 minuto".
:::

::: ficha
## 2 · Linha do tempo personalizada do cliente

[Entender e explicar]{.tag} **Quando usar:** para mostrar ao cliente, ano a ano, quais tributos ele paga hoje e quais pagará.

```
Monte uma linha do tempo de 2026 a 2033 para uma empresa com este perfil:
- Regime: [REGIME]
- Atividade: [ATIVIDADE / CNAE]
- Tributos sobre o consumo que paga hoje: [ex.: PIS, Cofins, ICMS]
- Vende para: [empresas / consumidor final / ambos, com %]

Formato: tabela com as colunas Ano | Tributos que paga | O que muda |
Ação recomendada. Destaque em negrito os anos de maior mudança para esse
perfil e explique por quê em 3 linhas após a tabela.
```
:::

::: ficha
## 3 · Responder a uma dúvida com fundamentação

[Entender e explicar]{.tag} **Quando usar:** um cliente (ou colega) fez uma pergunta técnica e você precisa de uma resposta segura.

```
Pergunta recebida: "[COLE A PERGUNTA]"

Responda em 4 partes:
1. Resposta direta (até 3 linhas).
2. Fundamentação: cite os dispositivos da EC 132/2023 e/ou da LC 214/2025
   que se aplicam. Se não tiver certeza do número do artigo, diga isso.
3. Exceções e pontos ainda dependentes de regulamentação.
4. O que eu devo conferir no texto oficial antes de responder ao cliente.
```

**Dica:** abra o texto da LC 214/2025 e confira cada artigo citado. Se você enviou a lei no conhecimento do Projeto, peça "cite o trecho literal".
:::

::: ficha
## 4 · Diagnóstico de impacto por regime

[Diagnosticar]{.tag} **Quando usar:** para priorizar quais clientes precisam de atenção imediata.

```
Faça um diagnóstico preliminar do impacto da reforma para:
- Regime: [SIMPLES / LUCRO PRESUMIDO / LUCRO REAL]
- Atividade: [ATIVIDADE]
- Faturamento mensal médio: R$ [VALOR]
- % das vendas para empresas (B2B): [%]
- Principais custos: [ex.: folha 45%, mercadorias 30%, aluguel 5%]

Entregue:
a) Nível de impacto (baixo / médio / alto) e justificativa.
b) Quais custos devem gerar crédito de IBS/CBS e quais não.
c) Riscos e oportunidades (3 de cada).
d) Dados adicionais que preciso levantar para uma simulação precisa.
Use premissas de alíquota explícitas e rotuladas como estimativa.
```
:::

::: ficha
## 5 · Enquadramento em alíquota reduzida ou zero

[Diagnosticar]{.tag} **Quando usar:** cliente de saúde, educação, alimentos, agro, profissões regulamentadas e outros setores com tratamento diferenciado.

```
Verifique se os produtos/serviços abaixo podem ter tratamento diferenciado
de IBS/CBS (alíquota zero, redução de 60%, redução de 30% ou regime
específico) pela LC 214/2025:

[LISTE: descrição + NCM ou NBS de cada item]

Para cada item, responda em tabela: Item | Tratamento provável |
Condições exigidas | Dispositivo legal | Grau de certeza (alto/médio/baixo).
Depois liste o que preciso confirmar no anexo correspondente da lei.
```

**Dica:** o enquadramento depende da classificação fiscal exata. Revise o cadastro de produtos (NCM/NBS) do cliente antes.
:::

::: ficha
## 6 · Mapa de créditos na cadeia de fornecedores

[Diagnosticar]{.tag} **Quando usar:** para empresas do regime regular que querem maximizar créditos.

```
Analise a lista de fornecedores/despesas abaixo de uma empresa do [REGIME]
e classifique o potencial de crédito de IBS/CBS a partir de 2027:

[LISTE: tipo de gasto | regime do fornecedor (se souber) | valor mensal]

Tabela: Gasto | Gera crédito? | Crédito integral ou limitado
(ex.: fornecedor do Simples) | Observação.
Ao final: estimativa de crédito mensal (com premissa de alíquota) e
3 recomendações de negociação com fornecedores.
```
:::

::: ficha
## 7 · Simples Nacional: ficar no DAS ou optar pelo regime regular de IBS/CBS

[Diagnosticar]{.tag} **Quando usar:** clientes do Simples que vendem para outras empresas.

```
Cliente optante do Simples Nacional, [ANEXO], atividade [ATIVIDADE].
- Faturamento mensal: R$ [VALOR]
- Vendas para empresas do regime regular: [%]
- Compras mensais que gerariam crédito: R$ [VALOR]
- Alíquota efetiva atual do DAS: [%]

Compare dois cenários a partir de 2027:
A) Continuar recolhendo IBS/CBS dentro do DAS.
B) Optar pelo recolhimento de IBS/CBS pelo regime regular.
Mostre: custo tributário mensal em cada cenário, crédito transferido ao
cliente comprador, efeito na competitividade de preço e recomendação
com as condições que mudariam a decisão. Explique as premissas.
```
:::

::: ficha
## 8 · Exposição ao Imposto Seletivo

[Diagnosticar]{.tag} **Quando usar:** indústria, distribuição e comércio de bebidas, fumo, veículos, mineração, combustíveis ou apostas.

```
A empresa [ATIVIDADE] produz/comercializa: [PRODUTOS].
1. Algum desses itens está sujeito ao Imposto Seletivo pela LC 214/2025?
2. Em qual etapa da cadeia o IS incide (produção, importação, extração)?
3. Como o IS interage com o IBS/CBS (base de cálculo)?
4. Quais pontos dependem de lei ordinária (alíquotas) ainda a confirmar?
Responda em tópicos e indique o grau de certeza de cada resposta.
```
:::

::: ficha
## 9 · Benefícios fiscais de ICMS até 2032

[Diagnosticar]{.tag} **Quando usar:** clientes com crédito presumido, redução de base ou outros incentivos estaduais.

```
O cliente usufrui hoje de: [DESCREVA O BENEFÍCIO DE ICMS e o estado].
Explique:
1. Até quando o benefício pode ser usado na transição.
2. Como a redução gradual do ICMS de 2029 a 2032 afeta o valor do benefício.
3. O que é o fundo de compensação de benefícios fiscais e quem pode ter
   direito.
4. Um plano de ação para o cliente não ser surpreendido em 2033.
Sinalize o que depende de regulamentação ou de ato estadual.
```
:::

::: ficha
## 10 · Revisão de preços com tributo "por fora"

[Agir]{.tag} **Quando usar:** para ajudar o cliente a recalcular a tabela de preços na transição.

```
Produto/serviço: [DESCRIÇÃO]
- Preço de venda atual: R$ [VALOR]
- Tributos sobre o consumo embutidos hoje: [ex.: ICMS 18%, PIS/Cofins 9,25%]
- Custo de aquisição: R$ [VALOR], com tributos recuperáveis de R$ [VALOR]
- Margem de contribuição desejada: [%]

Calcule o preço líquido de tributos e o novo preço com IBS/CBS "por fora"
(use [ALÍQUOTA, ex.: 26,5%] como premissa). Mostre a fórmula passo a passo
e explique como apresentar o novo preço ao comprador (preço + tributo
destacado). Compare margem antes e depois.
```
:::

::: ficha
## 11 · Contratos de longo prazo

[Agir]{.tag} **Quando usar:** contratos de prestação de serviços, locação, fornecimento ou obras que atravessam 2027 a 2033.

```
Tenho um contrato de [TIPO] com vigência até [DATA], preço de R$ [VALOR]
[com/sem] cláusula de revisão por alteração tributária.
1. Como a substituição de PIS/Cofins/ISS/ICMS por IBS/CBS afeta o
   equilíbrio do contrato?
2. Existem regras de transição na LC 214/2025 para contratos firmados antes
   da reforma? Cite e indique o grau de certeza.
3. Redija uma cláusula-modelo de reequilíbrio econômico-financeiro por
   alteração da carga tributária, em linguagem contratual.
Recomende validação por advogado.
```
:::

::: ficha
## 12 · Split payment e fluxo de caixa

[Agir]{.tag} **Quando usar:** para preparar o caixa do cliente para a retenção do tributo no pagamento.

```
Empresa [REGIME], faturamento mensal de R$ [VALOR], prazo médio de
recebimento de [X] dias, prazo médio de pagamento de [Y] dias, recebe
[%] por cartão/PIX/boleto.
Explique como o split payment funciona na prática e estime o efeito no
capital de giro quando estiver implantado (premissa de alíquota: [%]).
Liste 5 providências de tesouraria e de cadastro bancário/ERP.
Deixe claro o que ainda depende de regulamentação e do cronograma oficial.
```
:::

::: ficha
## 13 · Checklist do ano-teste 2026

[Agir]{.tag} **Quando usar:** para garantir que o cliente esteja emitindo documentos fiscais corretamente em 2026.

```
Monte um checklist de adequação ao ano-teste de 2026 para uma empresa
[REGIME] que emite [NF-e / NFC-e / NFS-e / CT-e], usando o sistema
[NOME DO ERP OU EMISSOR, se souber].
Inclua: cadastro de produtos e serviços (NCM/NBS, classificação tributária
de IBS/CBS), novos campos dos documentos fiscais, destaque de CBS 0,9% e
IBS 0,1%, obrigações acessórias, testes com o fornecedor do sistema e
responsáveis. Formato: tabela com Item | Responsável | Prazo | Status.
```
:::

::: ficha
## 14 · Triagem da carteira do escritório

[Organizar]{.tag} **Quando usar:** para decidir por onde começar quando a carteira é grande.

```
Minha carteira tem [N] clientes. Segue a lista anonimizada:
[Cliente | Regime | Atividade | Faturamento mensal aprox. | % B2B]

Classifique cada cliente em prioridade (alta, média, baixa) de atenção
para a reforma, com o motivo em uma linha. Depois sugira:
- a ordem de atendimento nas próximas 8 semanas;
- quais clientes são oportunidade para um serviço de consultoria de
  transição (e por quê).
```

**Dica:** exporte a lista da sua planilha, troque os nomes por códigos e cole como texto.
:::

::: ficha
## 15 · Roteiro de reunião com o cliente

[Organizar]{.tag} **Quando usar:** antes de uma reunião de diagnóstico ou de apresentação da reforma.

```
Prepare um roteiro de reunião de [30/45/60] minutos com um cliente
[REGIME], [ATIVIDADE], cujo principal ponto de atenção é [PONTO].
Inclua:
1. Abertura (objetivo da reunião em 2 frases).
2. Explicação visual da transição (o que mostrar no Mapa 2026 → 2033).
3. Resultado do diagnóstico em linguagem simples.
4. 5 perguntas para levantar dados que ainda faltam.
5. Proposta de próximos passos e de acompanhamento pelo escritório.
6. Respostas curtas para as 3 objeções mais prováveis do cliente.
```
:::
