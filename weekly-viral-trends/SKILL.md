---
name: weekly-viral-trends
description: Pesquisa o que está em alta NESTA SEMANA especificamente em marketing, vendas, tecnologia e IA, usando fontes confiáveis e citáveis — consultorias e institutos de peso (Deloitte, MIT Technology Review, McKinsey, Gartner, HBR, BCG, PwC, Bain, Forrester, WEF) e veículos de alto padrão editorial (The Economist, Bloomberg, WSJ, FT) — com WebSearch/WebFetch reais, nunca inventando dado, estudo ou fonte. Filtra e ranqueia os achados por potencial de viralização em redes sociais como conteúdo RÁPIDO (post de LinkedIn, thread, Reels/TikTok, carrossel), priorizando dados contraintuitivos, viradas de expectativa e declarações polêmicas de fontes de peso — não relatórios genéricos ou desatualizados. Para cada tendência selecionada entrega o achado, a fonte real com link, por que é contraintuitivo/viral, e 1-2 ângulos de hook prontos para post curto — sem escrever o post inteiro, porque o objetivo é agilidade de produção. Use sempre que o usuário pedir pesquisa de tendências da semana, conteúdo para viralizar, pauta rápida baseada em dado de mercado recente, ou perguntar algo como "o que está bombando essa semana em IA/marketing/vendas/tech" ou "me dá ideias de post com dado real" — mesmo sem usar essas palavras exatas.
---

# Pesquisa de Tendências Virais da Semana

## Visão geral

Esta skill não escreve o post final — ela entrega a matéria-prima para alguém
produzir conteúdo rápido (LinkedIn, thread, Reels/TikTok, carrossel) ainda
hoje ou amanhã: um achado real, publicado por uma fonte de peso, que
contraria uma expectativa ou surpreende, mais 1-2 ganchos já lapidados para
abrir o post. A pressa é o ponto central do pedido — por isso o output é uma
lista enxuta de "achado + fonte + por que viraliza + hook", nunca um
relatório longo nem o texto pronto do post.

Ela é focada e recorrente: sempre que rodar, o recorte temporal é **os
últimos dias**, não "o que existe sobre o tema" em geral. Um dado de dois
meses atrás, por melhor que seja, não é uma tendência desta semana — ver
`references/fontes-e-hooks.md` para como aplicar esse filtro na prática.

## Passo 1 — Definir o escopo com o usuário (quando não estiver claro)

Antes de pesquisar, confirme rapidamente (ou assuma um padrão razoável e
diga o que assumiu, se o usuário claramente quer algo rápido e não parece
disposto a responder perguntas antes de começar):

- **Quais dos quatro temas priorizar** — marketing, vendas, tecnologia, IA,
  ou todos? Se o usuário não especificar, cubra os quatro, mas sinta-se
  livre para pesar mais peso num tema se o pedido sugerir isso implicitamente
  (ex.: "trabalho com RevOps" pesa para vendas + tech).
- **Para qual formato/rede o conteúdo vai** — LinkedIn, Instagram/TikTok
  (Reels curto), thread de X, carrossel? Isso muda o tipo de hook do Passo 4.
  Se não especificado, entregue hooks para LinkedIn e para Reels/TikTok por
  padrão — são os dois formatos mais comuns para esse tipo de pedido.
- **Quantas tendências entregar** — o padrão é 5, um número que dá opção de
  escolha sem virar trabalho de curadoria para o usuário.

Não trave o trabalho nisso: se o usuário só disse "pesquisa o que está em
alta essa semana em marketing e IA", já é informação suficiente para
começar.

## Passo 2 — Pesquisar de verdade, com recorte semanal

Rode buscas focadas por tema (não uma busca genérica tipo "tendências de
marketing"). Boas buscas combinam o tema com um recorte temporal e o tipo de
fonte que se quer achar, por exemplo:

- `Deloitte AI adoption report 2026 site:deloitte.com`
- `MIT Technology Review AI this week`
- `McKinsey marketing trend latest`
- `Gartner sales technology 2026 survey`
- `HBR AI leadership research new`

Depois de achar candidatos, **confira a data de publicação** — o critério
"desta semana" é sobre quando o dado ficou público/comentado, não sobre
quando o fenômeno subjacente começou. Um estudo publicado há 3 meses mas que
só começou a circular amplamente esta semana (por exemplo, citado num evento
grande ou numa declaração recente) também conta como "em alta agora" —
nesse caso, registre por que está circulando agora, não apenas a data
original de publicação.

Veja `references/fontes-e-hooks.md` para a lista completa de fontes
priorizadas, a regra inegociável contra inventar citação, e o que fazer
quando `WebFetch` está bloqueado para um domínio mas `WebSearch` funciona.

## Passo 3 — Filtrar por potencial de viralização

Nem todo achado real é um bom gancho de post curto. Depois de reunir os
candidatos, descarte os que são apenas "informação correta, mas óbvia" e
priorize os que têm pelo menos uma destas características:

- **Contraintuitivo**: contraria uma crença comum do público-alvo (ex.: "a
  maioria acha que X, mas o dado mostra Y").
- **Virada de expectativa**: um número ou resultado que surpreende por ser
  muito maior/menor do que se esperaria.
- **Declaração polêmica de fonte de peso**: uma afirmação ousada ou
  desconfortável vinda de alguém/instituição que o público reconhece e
  respeita — a autoridade da fonte é o que dá permissão para a polêmica.
- **Estatística chocante e específica**: um número preciso (não "a maioria")
  que por si só já causa reação ao ser lido.

Um achado tecnicamente correto mas soso ("empresas continuam investindo em
IA") não entra na lista final mesmo que a fonte seja excelente — o filtro é
sobre a reação que o dado provoca, não sobre a qualidade da fonte sozinha
(embora a fonte precise ser real e boa também, ver Passo 2).

## Passo 4 — Entregar a lista final

Para cada tendência selecionada (ver quantidade acordada no Passo 1), entregue
neste formato, direto na conversa em Markdown — nunca gere um documento
formal (.docx/.pdf) para esta skill, o ponto é agilidade:

```markdown
### [Tema] — [título curto do achado, tipo manchete]

**O achado:** [1-3 frases descrevendo o dado/estudo/declaração, com o
número ou citação exata quando houver]

**Fonte:** [Nome da publicação/instituição, título do relatório/artigo,
mês/ano] — [link real que apareceu na busca]

**Por que viraliza:** [1-2 frases explicando qual dos gatilhos do Passo 3
se aplica — contraintuitivo, virada de expectativa, polêmica, estatística
chocante]

**Hooks prontos:**
- LinkedIn: "[frase de abertura pronta para colar no post]"
- Reels/TikTok: "[frase de abertura falada, mais curta e direta, pensada
  para os 3 primeiros segundos de vídeo]"
```

Regras para os hooks:

- O hook é a primeira frase que a pessoa vai ler ou ouvir — precisa causar
  uma reação (curiosidade, discordância, choque) sozinho, sem contexto
  adicional. Se o hook precisa de uma segunda frase para fazer sentido,
  reescreva.
- O hook de LinkedIn pode ser um pouco mais construído (uma frase completa,
  eventualmente com uma vírgula de suspense). O hook de Reels/TikTok precisa
  ser dizível em voz alta em menos de 3 segundos — mais curto, mais
  coloquial.
- Nunca escreva o roteiro ou o post inteiro nesta skill, mesmo que pareça
  fácil continuar — o valor do output é a curadoria rápida do material bruto
  mais o gancho, não a peça finalizada. Se o usuário pedir para desenvolver
  um hook específico em post/roteiro completo depois de ver a lista, isso é
  um pedido novo e separado.

Feche a entrega com uma linha citando o recorte de tempo usado na pesquisa
(ex.: "Pesquisa feita em 30/08/2026, cobrindo achados dos últimos 7 dias.")
para deixar claro o quão "fresco" o material é.

## Regra inegociável de fonte

Nunca invente um dado, estudo, citação ou URL — nem para preencher uma vaga
num tema onde a pesquisa não achou nada bom. Se depois de pesquisar de
verdade não aparecer nada citável e realmente recente num dos temas
pedidos, diga isso explicitamente ao usuário (ex.: "não encontrei nada
verificável e desta semana especificamente sobre vendas — os achados mais
recentes que achei têm quase um mês; quer que eu entregue mesmo assim
marcando a data, ou prefere só os outros três temas?") em vez de forçar uma
tendência fraca ou inventada só para completar a lista. Ver
`references/fontes-e-hooks.md` para o detalhamento desta regra e como reagir
quando a ferramenta de busca não está disponível na sessão.
