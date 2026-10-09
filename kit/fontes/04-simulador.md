```{=html}
<section class="capa">
  <div>
    <div class="selo">Material 04 · Direto no Claude.ai</div>
    <h1>Simulador de Impacto por Regime</h1>
    <div class="sub">Um roteiro que transforma o Claude em calculadora guiada: compare a carga dos tributos sobre o consumo de hoje com a carga do IBS/CBS, cliente a cliente.</div>
  </div>
  <div class="rodape">Simples Nacional · Lucro Presumido · Lucro Real · Exemplos resolvidos incluídos</div>
</section>
```

# Como o simulador funciona

Você cola o **prompt-mestre** (página seguinte) no Projeto do agente especialista. O Claude passa a conduzir a simulação: pergunta os dados do cliente **um a um**, aplica a metodologia abaixo e entrega um comparativo **carga atual × carga após a reforma**, com premissas visíveis.

**O que entra na comparação:** apenas os tributos sobre o consumo que serão substituídos: PIS, Cofins, ICMS, ISS e IPI hoje; CBS e IBS depois. IRPJ, CSLL e contribuições sobre a folha **não mudam** com esta reforma e ficam de fora.

## Metodologia (resumo)

1. **Carga atual** = tributos sobre o consumo apurados hoje (débitos − créditos).
2. **Receita líquida (RL)** = receita bruta − tributos sobre o consumo embutidos no preço. É o que a empresa efetivamente "fica" antes de custos.
3. **Carga nova** = alíquota de IBS/CBS × RL − alíquota × compras com direito a crédito (valores sem tributo).
   - O IBS/CBS é cobrado **por fora**: para manter a mesma receita líquida, o preço ao comprador passa a ser RL + IBS/CBS.
4. **Diferença** = carga nova − carga atual, em R$ e em %.
5. Para o **Simples Nacional**, compara-se o resultado do fornecedor e o custo efetivo do comprador em dois cenários (IBS/CBS dentro do DAS × regime regular).

## Premissas padrão (altere sempre que tiver dados melhores)

| Premissa | Valor padrão | Observação |
|---|---|---|
| Alíquota de referência CBS | 8,8% | Estimativa; será fixada por resolução do Senado |
| Alíquota de referência IBS | 17,7% | Estimativa; soma estadual + municipal |
| **Total IBS + CBS** | **26,5%** | Estimativa ilustrativa |
| Redução de 30% (profissões regulamentadas) | 18,55% | Sujeita às condições da LC 214/2025 |
| Redução de 60% (saúde, educação etc.) | 10,60% | Conforme enquadramento |
| Parcela de IBS/CBS dentro do DAS (Anexo III) | 48% do DAS | Aproximação pela partilha atual de PIS, Cofins e ISS |

<div class="aviso">

Os resultados são **estimativas para orientar a conversa com o cliente e priorizar a carteira**. Não substituem o planejamento tributário formal. Alíquotas, reduções e regras de crédito devem ser confirmadas na legislação vigente.

</div>

```{=html}
<div class="quebra"></div>
```

# Prompt-mestre do simulador

Copie **tudo** e cole no Projeto do agente. Depois é só responder às perguntas.

```
Você agora é o SIMULADOR DE IMPACTO DA REFORMA TRIBUTÁRIA.

OBJETIVO: comparar a carga atual de tributos sobre o consumo (PIS, Cofins,
ICMS, ISS, IPI) com a carga estimada de IBS/CBS no modelo completo (2033)
e mostrar o efeito intermediário em 2027 (CBS no lugar de PIS/Cofins).

ETAPA 1 · COLETA. Pergunte UM item por vez, esperando minha resposta:
 1. Regime: Simples Nacional, Lucro Presumido ou Lucro Real.
 2. Atividade principal e se é comércio, indústria ou serviço.
 3. Receita bruta mensal média (R$).
 4. Alíquotas atuais aplicáveis (ICMS, ISS, IPI; PIS/Cofins cumulativo
    ou não cumulativo; no Simples, a alíquota efetiva do DAS e o anexo).
 5. Compras mensais que darão direito a crédito de IBS/CBS (mercadorias,
    insumos, serviços de terceiros, aluguel, energia, software etc.),
    em R$ e SEM tributos. Lembre-me de que folha de salários não gera crédito.
 6. Se for regime regular hoje: créditos atuais de ICMS/PIS/Cofins/IPI.
 7. Percentual das vendas para empresas do regime regular (B2B).
 8. Se há possível enquadramento em redução de 30%, 60% ou alíquota zero.
 9. Se quero usar as alíquotas padrão (CBS 8,8% + IBS 17,7% = 26,5%)
    ou informar outras.

ETAPA 2 · CÁLCULO. Mostre fórmula e números de cada passo:
 a) Carga atual = débitos − créditos dos tributos sobre o consumo.
 b) Receita líquida (RL) = receita bruta − tributos embutidos no preço.
 c) Carga nova = alíquota efetiva IBS/CBS × RL − alíquota × compras
    com crédito.
 d) Efeito 2027: CBS × RL − CBS × compras, comparado a PIS/Cofins atuais.
 e) Diferença em R$/mês, R$/ano e em %.
 f) Simples Nacional: compare o cenário A (IBS/CBS no DAS, crédito ao
    comprador ≈ parcela de IBS/CBS do DAS) com o cenário B (IBS/CBS pelo
    regime regular), mostrando o resultado do fornecedor e o custo
    efetivo do comprador, para clientes B2B e B2C.

ETAPA 3 · RESULTADO:
 - Tabela-resumo: Item | Hoje | 2027 | 2033 | Diferença.
 - Leitura em 5 linhas para o contador.
 - Leitura em 5 linhas para o cliente leigo.
 - 3 alavancas para reduzir o impacto (preço, créditos, fornecedores,
   contratos, opção de regime).
 - Lista de premissas e do que precisa ser confirmado.

Regras: use R$ com 2 casas decimais; rotule estimativas; não invente
alíquotas específicas do cliente; se faltar dado, pergunte.
Comece agora pela pergunta 1.
```

**Atalho:** com o agente especialista instalado, basta digitar `/simulador`.

```{=html}
<div class="quebra"></div>
```

# Exemplo 1 · Serviços no Lucro Presumido

**Perfil:** empresa de serviços, receita bruta de **R$ 100.000,00/mês**, ISS de 5%, PIS/Cofins cumulativos (0,65% + 3%). Compras com direito a crédito (software, aluguel, energia, terceiros): **R$ 12.000,00/mês** sem tributos. A folha de salários é o principal custo e não gera crédito.

| Passo | Cálculo | Valor |
|---|---|---|
| Carga atual | 100.000 × (5% + 0,65% + 3%) | **R$ 8.650,00** |
| Receita líquida (RL) | 100.000 − 8.650 | R$ 91.350,00 |
| Débito IBS/CBS | 26,5% × 91.350 | R$ 24.207,75 |
| Crédito | 26,5% × 12.000 | R$ 3.180,00 |
| **Carga nova (2033)** | 24.207,75 − 3.180 | **R$ 21.027,75** |
| **Diferença** | | **+ R$ 12.377,75/mês (+143,1%)** |

**Se houver redução de 30% (profissão intelectual regulamentada, alíquota de 18,55%):** débito de 18,55% × 91.350 = R$ 16.945,43; crédito de R$ 3.180,00 (o crédito segue a alíquota cobrada do fornecedor); carga nova de **R$ 13.765,43**, ou seja, **+ R$ 5.115,43/mês (+59,1%)**.

**Efeito em 2027 (só a CBS no lugar de PIS/Cofins; o ISS continua):** CBS de 8,8% × 91.350 = R$ 8.038,80, menos o crédito de 8,8% × 12.000 = R$ 1.056,00, resulta em **R$ 6.982,80**, contra PIS/Cofins de R$ 3.650,00. São **+ R$ 3.332,80/mês já em 2027**.

> **Leitura:** prestadores de serviço do Presumido com poucos insumos estão entre os mais afetados. Se os clientes forem **empresas do regime regular**, eles recuperam o IBS/CBS como crédito, e o preço "por fora" pode ser repassado sem perda de competitividade. Se forem **consumidores finais**, o impacto recai sobre preço ou margem. Prioridade: enquadramento em reduções, revisão de preços e contratos.

```{=html}
<div class="quebra"></div>
```

# Exemplo 2 · Comércio varejista no Lucro Real

**Perfil:** loja que vende ao consumidor final, receita bruta de **R$ 500.000,00/mês**, compras de mercadorias de **R$ 300.000,00/mês** (valor com tributos). ICMS de 18% (por dentro) nas vendas e nas compras; PIS/Cofins não cumulativos (9,25%), com o ICMS excluído da base.

| Passo | Cálculo | Valor |
|---|---|---|
| ICMS a recolher | 18% × 500.000 − 18% × 300.000 | R$ 36.000,00 |
| PIS/Cofins a recolher | 9,25% × 410.000 − 9,25% × 246.000 | R$ 15.170,00 |
| **Carga atual** | 36.000 + 15.170 | **R$ 51.170,00** |
| Receita líquida (RL) | 500.000 − 90.000 − 37.925 | R$ 372.075,00 |
| Compras líquidas de tributos | 300.000 − 54.000 − 22.755 | R$ 223.245,00 |
| Débito IBS/CBS | 26,5% × 372.075 | R$ 98.599,88 |
| Crédito IBS/CBS | 26,5% × 223.245 | R$ 59.159,93 |
| **Carga nova (2033)** | 98.599,88 − 59.159,93 | **R$ 39.439,95** |
| **Diferença** | | **− R$ 11.730,05/mês (−22,9%)** |

> **Leitura:** nem todo mundo perde. Neste perfil, a carga atual sobre o valor agregado (R$ 148.830,00) é de cerca de 34,4%, acima dos 26,5% estimados. O resultado depende muito da alíquota de ICMS do estado, do mix de produtos (itens com redução ou alíquota zero mudam tudo) e de benefícios fiscais atuais. Atenção também ao **fim dos benefícios de ICMS até 2032** e ao **split payment** no caixa.

```{=html}
<div class="quebra"></div>
```

# Exemplo 3 · Simples Nacional vendendo para empresas

**Perfil:** prestadora de serviços do Anexo III, receita de **R$ 60.000,00/mês**, alíquota efetiva do DAS de **10%**. Compras de **R$ 8.000,00/mês** sem tributos (R$ 10.120,00 com IBS/CBS de 26,5%). Premissa: 48% do DAS corresponde a IBS/CBS.

**Cenário A · IBS/CBS dentro do DAS**

| Item | Cálculo | Valor |
|---|---|---|
| DAS | 10% × 60.000 | R$ 6.000,00 |
| Crédito transferido ao comprador | 6.000 × 48% | R$ 2.880,00 |
| Custo efetivo para o comprador | 60.000 − 2.880 | R$ 57.120,00 |
| Resultado do fornecedor | 60.000 − 6.000 − 10.120 (sem crédito nas compras) | **R$ 43.880,00** |

**Cenário B · IBS/CBS pelo regime regular, mesmo custo efetivo para o comprador B2B**

| Item | Cálculo | Valor |
|---|---|---|
| Preço sem tributo (P) | igual ao custo efetivo do cenário A | R$ 57.120,00 |
| DAS sem a parcela de IBS/CBS | 10% × 52% × 57.120 | R$ 2.970,24 |
| IBS/CBS cobrado do comprador (crédito integral para ele) | 26,5% × 57.120 | R$ 15.136,80 |
| Resultado do fornecedor | 57.120 − 2.970,24 − 8.000 (compras com crédito) | **R$ 46.149,76** |
| **Diferença para o fornecedor** | | **+ R$ 2.269,76/mês** |

**Mesmo cenário B, mas vendendo para consumidor final (B2C)** e mantendo o preço final de R$ 60.000,00: o preço sem tributo cai para 60.000 ÷ 1,265 = R$ 47.430,83; o DAS reduzido fica em R$ 2.466,40; o resultado do fornecedor cai para **R$ 36.964,43**, ou seja, **− R$ 6.915,57/mês** em relação ao cenário A.

> **Leitura:** a opção pelo regime regular de IBS/CBS tende a compensar quando a maior parte das vendas é **B2B para empresas do regime regular** e há compras relevantes com crédito. Para quem vende ao **consumidor final**, permanecer com o IBS/CBS dentro do DAS costuma ser melhor. A decisão é semestral: simule de novo sempre que o perfil de clientes mudar.

```{=html}
<div class="quebra"></div>
```

# Checklist de dados para levar à reunião

- [ ] Receita bruta mensal dos últimos 12 meses, separada por atividade
- [ ] Alíquotas atuais (ICMS por estado, ISS por município, IPI, regime de PIS/Cofins)
- [ ] Créditos atuais de ICMS, PIS/Cofins e IPI
- [ ] Principais compras e despesas, com o regime tributário dos fornecedores
- [ ] Percentual das vendas para empresas × consumidor final
- [ ] Classificação fiscal (NCM/NBS) dos principais produtos e serviços
- [ ] Benefícios fiscais de ICMS em uso
- [ ] Contratos de longo prazo com clientes e fornecedores
