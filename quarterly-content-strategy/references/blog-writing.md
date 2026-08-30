# Fase 2 — Redigir o blog post de uma pauta

Esta fase só começa depois que o usuário aprovou o planejamento (ver
`SKILL.md`, seção "O gate de aprovação") e escolheu quais pautas quer que
sejam redigidas — nunca escreva os 9 (ou N) artigos de uma vez sem essa
confirmação.

A pauta já fez o trabalho estratégico difícil: tese, ângulo, pergunta
central, estrutura e fontes já existem (ver `references/schema.md`). O
trabalho desta fase é executar esse briefing em prosa, na voz da marca
(`assets/brand-profile.md`), sem reabrir decisões estratégicas que a pauta
já tomou — se a pauta diz que a tese é X, o artigo defende X, não uma
versão suavizada de X para agradar todo mundo.

## Estrutura do artigo

- **Título**: pode ajustar o título da pauta para ficar melhor como
  manchete de blog, mas mantenha a tese provocativa — vire clickbait vazio é
  o oposto do posicionamento de "pensadora" que a marca busca.
- **Lead (1º parágrafo)**: responde a `Pergunta central` de forma direta nas
  primeiras 2-3 frases, antes de qualquer contextualização longa. Isso
  importa tanto para reter quem está lendo quanto para GEO (ver abaixo).
- **Corpo**: segue os bullets de `Estrutura esperada` como esqueleto,
  expandido em subtítulos (H2). Cada bullet da pauta normalmente vira um H2
  ou um bloco de 2-4 parágrafos.
- **Dados**: toda afirmação que corresponde ao campo `Realidade` da pauta
  aparece no texto com a fonte pesquisada (`sources`) citada e linkada —
  nunca solta sem atribuição.
- **Fechamento**: reforça a `Tese` da pauta e termina abrindo uma pergunta
  ou provocação para reflexão do leitor — não um CTA de venda direto
  ("agende uma call", "contrate agora"). Ver `assets/brand-profile.md`:
  o posicionamento é de quem pensa junto, não de quem vende execução.

## SEO

- A palavra-chave principal (`Palavras-chave` da pauta) aparece no título,
  no H1, no primeiro parágrafo e em 1-2 subtítulos — sem repetição forçada;
  keyword stuffing hoje derruba ranking e soa robótico, o oposto do tom da
  marca.
- Meta description de ~150-160 caracteres respondendo a pergunta central.
- Subtítulos (H2) formulados como pergunta ou afirmação forte — o tipo de
  frase que alguém realmente digitaria numa busca.
- Links internos para outros posts do blog (se o usuário fornecer o
  catálogo) e links externos para as fontes pesquisadas na Fase 1.

## GEO (Generative Engine Optimization)

Motores de resposta por IA (ChatGPT, Perplexity, Google AI Overviews)
extraem e citam blocos de texto que respondem a uma pergunta de forma
direta, específica e verificável — não parágrafos longos de contexto antes
da resposta. Para aumentar a chance do artigo ser citado por essas
ferramentas:

- A `Pergunta central` da pauta é respondida em 1-2 frases diretas logo no
  início do artigo, antes de qualquer preâmbulo — é literalmente o trecho
  mais citável do texto.
- Subtítulos no formato de pergunta quando fizer sentido (`Por que empresas
  com os melhores dashboards continuam errando?`), porque IA generativa
  tende a casar a pergunta do usuário com um subtítulo parecido.
- Dados sempre com atribuição explícita e clara ("Segundo [fonte], [dado]")
  — mecanismos generativos preferem afirmações que já vêm com a fonte
  embutida, porque isso reduz o risco de alucinação na resposta deles.
- Uma seção curta de FAQ ao final (2-3 perguntas relacionadas, respondidas
  em 1-2 frases cada) quando o tema permitir — é o formato mais citável que
  existe para esses motores.
- Parágrafos curtos (3-4 frases) — blocos longos são candidatos piores à
  extração.
- Nome da autora/marca mencionado de forma consistente ao longo do texto —
  reforça a associação entre a entidade (a pessoa) e o conteúdo, o que
  ajuda tanto SEO de marca quanto a forma como IA generativa atribui
  autoria a uma fonte.

## Entrega

Use a skill `docx` (já disponível no ambiente) para produzir o artigo final
como Word, a menos que o usuário peça outro formato — esta skill não
reimplementa geração de documento de forma livre, só a do planejamento
trimestral, que tem uma estrutura fixa repetível o bastante para valer um
script dedicado. Um blog post é texto corrido, então a skill `docx` já
resolve isso bem.
