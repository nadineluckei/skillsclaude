---
name: pesquisador-temas
description: Pesquisa temas em duas frentes distintas — Temas Rápidos (notícias em alta, trends em IA/tools/mercado prontos para social media) e Temas Robustos (dores específicas citadas em pesquisas de consultorias + temas em alta baseados em fontes executivas como Deloitte, HBR, McKinsey). Use esta skill sempre que precisar de tendências atuais para social media, identificar dores reais do mercado em marketing/vendas/processos/IA/dados, ou planejar conteúdo editorial baseado em pesquisa confiável.
---

# Pesquisador de Temas — Rápidos e Robustos

## Visão Geral

Esta skill pesquisa temas em duas frentes completamente distintas, cada uma com propósito, fonte e formato próprio:

1. **Temas Rápidos**: Notícias em alta, trends virais, novidades de IA, ferramentas emergentes — tudo pronto para chamar atenção em social media com hooks e ângulos de engajamento.

2. **Temas Robustos**: Pesquisa de qualidade editorial em duas editorias separadas:
   - **Dores Específicas**: O que consultoras e executivos reportam como problemas reais nas operações de marketing, vendas, processos, IA e dados
   - **Temas em Alta**: Tendências identificadas além das consultorias (publicações tech, pesquisas de mercado, relatórios setoriais)

## Entrada esperada

O usuário pode pedir de três formas:

- **"Pesquisa rápida sobre [tema]"** → Temas Rápidos apenas
- **"Pesquisa robusta sobre [tema]"** → Temas Robustos apenas (ambas editorias)
- **"Pesquisa completa sobre [tema]"** → Ambas as frentes

Se o pedido for ambíguo ("pesquise trends em IA", "quero temas em alta"), confirme qual(is) frente(s) o usuário quer antes de pesquisar.

### Intake Interview (Antes de Pesquisar)

Antes de começar qualquer pesquisa, pergunte ao usuário:

1. **Timeframe esperado?** (será pré-configurado, mas confirme)
   - Temas Rápidos: últimas 2 semanas (social trending)
   - Temas Robustos: últimos 6 meses (executive-level research)
   - Customizado? (usuário quer outro período)

2. **Profundidade desejada?** (Quick / Standard / Deep-dive)
   - Quick: 3-5 temas/dores, fontes principais
   - Standard: 5-8 temas/dores, validação cruzada
   - Deep-dive: 10+ temas/dores, análise detalhada

3. **Público-alvo?** (Startup / Mid-market / Enterprise / C-Level)

4. **Output desejado?** (Inline / .docx / JSON / Markdown)

Adapte escopo e profundidade baseado nas respostas antes de pesquisar.

## Pillar 1: Temas Rápidos

### O que pesquisar

Notícias, trends, lançamentos, curiosidades em alta **agora** sobre:
- IA (modelos, ferramentas, aplicações práticas)
- SaaS/startups em crescimento
- Ferramentas emergentes
- Tendências de mercado (marketing, vendas, dados)
- Eventos/anúncios relevantes

Foco: **o que tá em alta agora**, não "evergreen" — busque por datas recentes.

### Fontes recomendadas

- **Notícias tech**: Product Hunt, Hacker News, TechCrunch, The Verge
- **IA específica**: Papers with Code, Hugging Face trending, ArXiv recent
- **Negócios**: LinkedIn trending, newsletters de tech (Ben Evans, Every, etc)
- **Social media**: Twitter/X trending, TikTok creator economy trends
- **Pesquisa rápida**: Google News, Google Trends

### Timeframe Padrão

**Temas Rápidos: Últimas 2 Semanas**
- Busque notícias/trends publicadas nos últimos 14 dias
- Portais: Product Hunt, Hacker News, TechCrunch, MundoMarketing, PropMark, LinkedIn trending, Twitter/X, Google Trends
- Descarte notícias de "1 mês atrás" mesmo que legais — rápido = agora

### Como estruturar

Cada tema rápido deve ter:

- **Título**: A notícia/trend em si, no máximo 1 frase curta
- **Por que tá em alta**: 1-2 frases explicando o contexto (quem lançou, quem tá usando, o hype)
- **Ângulo para social**: A frase de gancho pronta para chamar atenção (tipo manchete de Reel, post viral) — diferente do título, mais provocador/curiosidade/urgência
- **Fonte**: Onde você viu a notícia (com data exata)
- **Confiança**: 🟢 Alta (3+ portais concordam) / 🟡 Média (2 portais) / 🔴 Baixa (1 fonte isolada)

**Exemplo:**
- **Título**: OpenAI anuncia novo modelo com custos 70% menores
- **Por que tá em alta**: Startup e enterprise querem IA barata; redução de custo operacional é trend do momento
- **Ângulo para social**: "Enquanto isso, seu concorrente já está usando IA por 1/3 do preço"
- **Fonte**: OpenAI blog, jan/2026

## Pillar 2: Temas Robustos

Este pillar tem **duas editorias distintas**, ambas com foco em marketing, vendas, processos, IA e dados.

### Timeframe Padrão

**Temas Robustos: Últimos 6 Meses**
- Busque pesquisas, relatórios e estudos publicados entre últimos 6 meses (jan-ago 2026)
- Consultorias, HBR, LinkedIn executive posts, relatórios setoriais
- Descarte dados de 2+ anos atrás (a menos que contexto histórico seja relevante)
- Priorize dados numéricos (estatísticas) sobre opinião isolada

### Editoria A: Dores Específicas

Identificar **problemas reais** que consultoras, analistas e executivos citam frequentemente em pesquisas recentes (últimos 6 meses).

#### Fontes prioritárias

- **Consultorias**: Deloitte Insights, McKinsey, BCG, Bain, Gartner
- **Análise**: Harvard Business Review, MIT Sloan Management Review, Stanford GSB
- **Pesquisa setorial**: Forrester, IDC, Gartner reports
- **Executivos**: LinkedIn posts de CFOs/CMOs/COOs discutindo problemas

#### Como identificar dores

Ao ler uma pesquisa, procure por:
- Estatísticas sobre falhas ("68% dos projetos de transformação digital falham")
- Frases sobre desafios ("maior barreira é falta de talent", "silagem de dados impede decisão")
- Feedback direto de executivos ("o que mais me tira o sono é...")
- Estudos de caso sobre o que deu errado

#### Estrutura de uma Dor

- **Dor (problema)**: Nome curto e específico (ex: "Execução falha em projetos de transformação")
- **Citação/dado**: A frase ou número da pesquisa que comprova (ex: "McKinsey 2025 reporta que 60% dos projetos não atingem ROI")
- **Por que é dor agora**: Contexto de por que é urgente (ex: "pressão por ROI em IA força decisões rápidas")
- **Quem sofre**: Que cargo/função (CMO, CIO, VP de dados, etc)
- **Fonte**: Deloitte, McKinsey, HBR, etc + data

**Exemplo:**
- **Dor**: Ceticismo com IA por falta de ROI claro
- **Dado**: "Gartner 2025: 74% dos líderes de marketing têm dúvida se investimento em IA compensa"
- **Por que agora**: Pressão acionária força justificativa de gasto; muitos pilotos não viraram negócio
- **Quem sofre**: CMOs, CFOs, CTOs
- **Fonte**: Gartner AI Survey 2025

### Editoria B: Temas em Alta

Tendências emergentes e consolidadas no mercado de marketing, vendas, processos, IA e dados — não necessariamente "dores", mas temas que estão em evidência.

#### Fontes recomendadas

- Consultorias (Deloitte, McKinsey, etc) — mesmas de cima
- **Blogs/publicações**: HBR, MIT Sloan, CMO Council, Sales Hacker, Data Science Central
- **Relatórios anuais**: Gartner Magic Quadrant, Forrester Wave
- **LinkedIn**: Conteúdo viral de thought leaders na área
- **Newsletters**: Cold Email Benchmarks, The Revenue Collective, Data Stack Show
- **Podcasts/eventos**: Insights de conferências (SaaStr, MarketingProfs Summit, etc)

#### Como identificar temas em alta

Procure por padrões:
- Mesma palavra-chave aparecendo em múltiplas fontes (ex: "composable architecture")
- Perguntas recorrentes em comunidades (ex: "como implementar product-led growth?")
- Ferramentas novas que explodem em uso
- Metodologias que ganham adoção
- Shifts em estratégia da indústria

#### Estrutura de um Tema em Alta

- **Tema**: Nome do tema (ex: "Product-Led Growth (PLG) em B2B")
- **O que é**: 1-2 frases explicando pra quem não conhece
- **Por que tá em alta**: Contexto de por que virou trend agora (ex: "vendas consultivas custam demais; produtivo auto-serve reduz CAC")
- **Onde tá em alta**: Em qual segmento (ex: "SaaS B2B; especialmente startups Series A-B")
- **Próximos 6 meses**: O que vai evoluir no tema (ex: "integração com AI copilots, análise de comportamento")
- **Fonte**: Publicações/analistas que reportam

**Exemplo:**
- **Tema**: IA como agente autônomo nas operações B2B
- **O que é**: Modelos de IA que não apenas fazem previsões, mas executam ações independentemente (agendar follow-ups, atualizar dados, sugerir prioridades)
- **Por que tá em alta**: 2024-2025 foram de "IA gera insights"; agora é "IA executa"; pressão por automação de trabalho repetitivo
- **Onde tá em alta**: Enterprise, SaaS, áreas de ops/marketing/vendas
- **Próximos 6 meses**: Regulação sobre "IA autônoma"; melhor integração com CRMs; benchmarks de ROI
- **Fonte**: McKinsey "Agentic AI", HBR "The Rise of Autonomous AI", Product Hunt trending

## Formatação e Entrega

### Estrutura do documento

Independente de qual frente(s) pesquisar, organize assim:

```
PESQUISA DE TEMAS
[Data da pesquisa]

== METHODOLOGY ==
Timeframe: [especificar] | Profundidade: [quick/standard/deep] | Público: [target]
Fontes consultadas: [número] | % validado: [X%] | Confiança média: [alta/média/baixa]

== TEMAS RÁPIDOS ==
(se solicitado)

[Lista de temas, cada um com Título, Por que, Ângulo, Fonte, Confiança]

---

== TEMAS ROBUSTOS ==

### Editoria: Dores Específicas
[Lista de dores, cada uma com Dor, Dado, Por que, Quem, Fonte, Confiança]

### Editoria: Temas em Alta
[Lista de temas, cada um com Tema, O que é, Por que, Onde, Próximos 6m, Fonte, Confiança]

---

== QUALITY SUMMARY ==
Total de achados: [X]
🟢 Alta confiança (3+ fontes): [X]
🟡 Média confiança (2 fontes): [X]
🔴 Baixa confiança (1 fonte): [X]

== GAPS & LIMITATIONS ==
[O que faltou/não conseguimos validar/temas que não temos cobertura]

---

[Resumo executivo: 3-4 frases sobre o que essa pesquisa revelou e qual oportunidade emerge]
```

### Formatação em .docx

- Títulos de cada tema/dor em **negrito**
- Campos (Por que, Ângulo, Fonte, etc) em *itálico*
- Dados/citações entre aspas
- Links clicáveis quando houver URL de fonte
- Estrutura de hierarquia clara (H1 para seções, H2 para editorias, nenhuma sublista desnecessária)

Quando pronto, gere o .docx usando o script `scripts/generate_docx.js` (ver seção abaixo).

### Saída final

Entregue direto na conversa:
1. **Resumo executivo** (2-3 frases do insight principal)
2. **Arquivo .docx** anexado

Se o usuário pedir pra enviar por e-mail ou em outro formato, proceda conforme solicitado.

## Pesquisa de Qualidade

Nunca invente citações, estatísticas ou "fatos" sobre o que a McKinsey disse. Se não conseguir encontrar uma fonte confiável, omita o dado e diga "não encontrei fonte recente pra esse ponto" ao invés de alucinizar.

**Regras inegociáveis:**

### Multi-Index Verification (2+ Fontes Obrigatório)
- **Tema/Dor com 1 fonte** = ponto isolado 🔴 (mencione mas não eleve a "trend")
- **Tema/Dor com 2+ fontes concordando** = tema consolidado 🟢 (confiança média/alta)
- Exemplo:
  - ❌ "Só McKinsey reporta isso" → é opinião de 1 consultoria, não trend
  - ✅ "McKinsey + Gartner + HBR concordam" → é trend consolidado

### Confidence Scoring Obrigatório
Marque cada finding:
- 🟢 **ALTA**: 3+ fontes independentes concordam, dados numéricos
- 🟡 **MÉDIA**: 2 fontes, alguns dados, alguns gaps
- 🔴 **BAIXA**: 1 fonte, observação isolada, precisa validação

### Outras Regras
- Toda estatística cita a fonte e a data (ex: "Gartner 2025", não "Gartner diz")
- Temas rápidos: verifica data exata (últimas 2 semanas)
- Temas robustos: busca relatórios dos últimos 6 meses
- Se fonte tem 3+ meses, note se tema evoluiu desde então

## Roteiro de Pesquisa

### Se pedido: Temas Rápidos

1. Busque em Product Hunt, HackerNews, Twitter trending, Google Trends de **hoje/esta semana**
2. Filtro: tem a ver com IA, tools, mercado? Vai viralizar em social?
3. Para cada tema, escreva o ângulo de social pronto pra copiar
4. Entregar no dia (ou em poucas horas)

### Se pedido: Temas Robustos

**Fase 1 — Dores Específicas**

1. Busque nos últimos 2-3 relatórios de McKinsey, Deloitte, Gartner, HBR sobre o segmento (marketing/vendas/IA/dados)
2. Procure por: estatísticas de fracasso, citações de desafios, feedback direto de executivos
3. Agrupe por tema (ex: "todas as dores relacionadas a falta de execução em IA" junto)
4. Para cada dor, traz a citação/dado, contexto e público afetado

**Fase 2 — Temas em Alta**

1. Busque em publicações (HBR, LinkedIn trending), newsletters, relatórios anuais (últimos 6-12 meses)
2. Procure padrões: qual palavra/conceito aparece em múltiplas fontes?
3. Para cada tema, explica o que é, por que é trend agora, onde está em alta, o que vem depois
4. Se o tema foi citado em Gartner Magic Quadrant ou Forrester Wave, mencione

**Fase 3 — Resumo**

Leia tudo e escreva 3-4 frases sobre qual é a maior insight e que oportunidade abre pra quem tá atento.

## Adaptações

Se o usuário pedir pesquisa em **outro idioma**, pesquise e escreva tudo nesse idioma (McKinsey em espanhol, LinkedIn em português, etc). A estrutura fica a mesma.

Se pedir pesquisa em **nicho específico** (ex: só healthcare, só financial services), adapte as fontes pra publicações daquele segmento.

Se pedir temas em **período específico** (ex: "tendências pro próximo trimestre"), explique qual é a base da sua previsão (relatórios que indicam direção, ciclos históricos, etc).

## Como Entregar com Confiança

Antes de finalizar qualquer pesquisa, faça um **Quality Check**:

1. **Multi-index verificado?** Cada dor/tema tem 2+ fontes? Se não, marque como 🔴 BAIXA confiança
2. **Datas checadas?** Temas rápidos são das últimas 2 semanas? Robustos dos últimos 6 meses?
3. **Gaps documentados?** Você deixou claro o que NÃO conseguiu validar?
4. **Confiança distribuída?** Tem mix de 🟢 Alta, 🟡 Média, 🔴 Baixa (não tudo igual)?
5. **Resumo accionável?** O resumo executivo deixa claro "por quê isso importa agora"?

Se falhar em qualquer ponto, revise antes de entregar.

## Troubleshooting

**"Não consigo achar fonte pra essa dor"**
→ Omita a dor e diga "não encontrei validação recente nos últimos 6 meses" em vez de inventar

**"Achei 2 temas muito parecidos"**
→ Mescle em um só ou esclareça a diferença (ex: "Product-Led Growth" vs "Self-Serve Commerce" são relacionados mas distintos)

**"A gente já pesquisou isso mês passado"**
→ Pergunte ao usuário se quer um update (o que mudou) ou temas totalmente novos

**"Encontrei só 1 fonte pra um tema que parece importante"**
→ Marque como 🔴 BAIXA confiança. Mencione: "Precisa validação adicional" ou deixe fora se score ficar muito baixo

**"Fontes discordam sobre a mesma dor"**
→ Documente o desacordo ("McKinsey reporta 60%, Gartner reporta 75%"). Isso é informação, não erro
