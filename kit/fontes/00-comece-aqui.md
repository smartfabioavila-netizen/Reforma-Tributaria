```{=html}
<section class="capa">
  <div>
    <div class="selo">Módulo 1 · Comece aqui</div>
    <h1>Claude para Reforma Tributária 2026</h1>
    <div class="sub">Guia de início: como configurar o Claude e usar cada material do kit no dia a dia do escritório contábil.</div>
  </div>
  <div class="rodape">Leia antes de tudo · Leva cerca de 15 minutos</div>
</section>
```

# Antes de tudo: o que você tem em mãos

Este kit transforma o Claude, a IA da Anthropic, em um assistente especializado na Reforma Tributária do consumo (EC 132/2023 e LC 214/2025). O objetivo é simples: **responder dúvidas mais rápido, comunicar melhor com os clientes e mostrar o impacto da reforma em números**, sem você precisar aprender tecnologia.

| # | Material | Formato | Para que serve |
|---|---|---|---|
| 1 | Este guia (Comece Aqui) | PDF | Configurar o Claude e entender a ordem de uso |
| 2 | Agente "Especialista em Reforma Tributária 2026" | .md | Instruções que deixam o Claude especialista no assunto |
| 3 | 15 Prompts Prontos · Reforma Tributária na Prática | PDF | Comandos prontos para as situações mais comuns |
| 4 | 5 E-mails Prontos · Comunicação com Clientes | .docx | Textos editáveis para avisar e orientar a carteira |
| 5 | Simulador de Impacto por Regime | PDF | Roteiro para comparar a carga atual com a futura |
| 6 | Mapa Visual da Transição 2026 → 2033 | PDF | Linha do tempo para imprimir ou mostrar em reunião |

**Ordem recomendada:** este guia → configurar o agente → testar 3 prompts → mapa visual → simulador com um cliente real → e-mails para a carteira.

# Passo 1: crie sua conta no Claude

1. Acesse **claude.ai** e clique em *Sign up* (cadastro). Você pode entrar com uma conta Google ou com e-mail.
2. O plano gratuito permite testar. Para uso diário no escritório, o **Claude Pro** libera os *Projetos*, mais mensagens e o envio de arquivos maiores. É nele que o agente do kit funciona melhor.
3. A interface aceita português normalmente. Escreva como escreveria para um colega.

# Passo 2: instale o agente especialista (5 minutos)

O arquivo `agente_especialista_reforma_tributaria_2026.md` contém as *instruções do projeto*: um texto que define como o Claude deve pensar, o que considerar e como responder sobre a reforma.

1. No menu lateral do Claude, clique em **Projects (Projetos)** → **Create project (Criar projeto)**.
2. Dê um nome, por exemplo: `Reforma Tributária · Escritório`.
3. Clique em **Set project instructions (Definir instruções)**, abra o arquivo `.md` do agente em qualquer editor de texto (Bloco de Notas serve), **copie todo o conteúdo e cole** no campo de instruções. Salve.
4. *(Opcional, recomendado)* Em **Project knowledge (Conhecimento do projeto)**, envie:
   - o PDF do Mapa Visual da Transição;
   - o texto da LC 214/2025 (disponível no site do Planalto);
   - materiais internos do escritório (tabela de clientes por regime, sem dados sensíveis).
5. A partir de agora, **toda conversa iniciada dentro desse projeto** já começa com o Claude no papel de especialista.

> **Teste rápido:** dentro do projeto, pergunte: *"O que muda para uma empresa do Lucro Presumido prestadora de serviços em 2026 e em 2027?"* A resposta deve citar o ano-teste, a CBS substituindo PIS/Cofins em 2027 e o fim da cumulatividade.

# Passo 3: como usar os prompts

Cada prompt do PDF tem campos entre colchetes, como `[REGIME TRIBUTÁRIO]` ou `[ATIVIDADE]`. Para usar:

1. Copie o prompt inteiro.
2. Cole dentro do projeto do agente.
3. Substitua os colchetes pelas informações do cliente (sem nome, CNPJ ou CPF; veja o Passo 5).
4. Envie. Se a resposta vier genérica, **dê mais contexto** ("faturamento mensal médio de R$ 180 mil, 70% das vendas para outras empresas") e peça para refazer.

**Três hábitos que melhoram muito as respostas:**

- **Peça o formato:** "responda em tabela", "em até 10 linhas", "em linguagem para o cliente leigo".
- **Peça a base legal:** "indique o dispositivo da LC 214/2025 que fundamenta cada ponto". Depois **confira** no texto da lei.
- **Continue a conversa:** "agora transforme isso em um e-mail", "refaça considerando que o cliente é do Simples".

# Passo 4: como usar o simulador e o mapa

- **Simulador de Impacto:** o PDF traz um prompt-mestre que transforma o Claude em uma calculadora guiada. Ele pergunta os dados do cliente um a um, monta a comparação **carga atual × carga após a reforma** e explica as premissas. Use os exemplos resolvidos do PDF para conferir se o resultado faz sentido.
- **Mapa Visual:** imprima em A4 paisagem ou mostre na tela durante reuniões. Ele resume, ano a ano, o que entra e o que sai entre 2026 e 2033.

# Passo 5: cuidados profissionais (leia com atenção)

<div class="aviso">

**A IA acelera o seu trabalho, mas a responsabilidade técnica continua sendo do profissional.**

- **Confira a base legal.** O Claude pode errar ou citar um dispositivo de forma imprecisa. Valide no texto oficial da EC 132/2023, da LC 214/2025 e das normas posteriores.
- **Alíquotas ainda serão fixadas.** As alíquotas de referência da CBS e do IBS serão definidas por resolução do Senado. Os percentuais usados nos exemplos (cerca de 26,5% somados) são **estimativas ilustrativas**.
- **A regulamentação continua mudando.** Leis complementares, regulamentos, atos do Comitê Gestor do IBS e da Receita Federal ainda podem alterar detalhes. Confirme sempre a versão vigente.
- **Proteja os dados dos clientes (LGPD).** Não envie nome, CNPJ, CPF, endereços nem documentos com dados pessoais. Use descrições como "Cliente A, comércio varejista, Lucro Real".
- **Simulação não é parecer.** Os números do simulador servem para orientar a conversa e priorizar clientes, não substituem o planejamento tributário formal.

</div>

# Seu plano para os primeiros 7 dias

| Dia | Ação | Material |
|---|---|---|
| 1 | Criar a conta e instalar o agente no Projeto | Este guia + agente .md |
| 2 | Testar os prompts 1, 2 e 3 com um cliente fictício | 15 Prompts |
| 3 | Imprimir o mapa e estudar o ano de 2026 e o de 2027 | Mapa Visual |
| 4 | Separar a carteira por regime (Simples, Presumido, Real) | Prompt 14 |
| 5 | Rodar o simulador para os 3 clientes de maior faturamento | Simulador |
| 6 | Enviar o e-mail 1 (comunicado geral) para toda a carteira | 5 E-mails |
| 7 | Agendar reuniões de diagnóstico com os clientes mais impactados | E-mail 3 + Prompt 15 |

Bom trabalho. Agora abra o arquivo do agente e configure seu projeto.
