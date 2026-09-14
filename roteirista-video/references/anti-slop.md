# Anti-slop: escrever sem soar como IA genérica

Isso importa mais nesta skill do que na média: o posicionamento inteiro é
"pensadora, não executora" (ver `assets/brand-profile.md`). Um texto que
soa como qualquer outro texto gerado por IA — cheio dos mesmos tiques que
qualquer leitor experiente já reconhece de longe — mina exatamente a
credibilidade que o conteúdo deveria construir. Aplique esta revisão antes
de entregar qualquer blog post (Fase 2) ou roteiro de Reels (Fase 3).

As regras abaixo vêm de duas fontes: a página `Wikipedia:Signs of AI
writing` (mantida pelo WikiProject AI Cleanup, cataloga padrões que
editores da Wikipédia aprenderam a reconhecer como geração por IA) e dois
projetos públicos de "anti-slop writing" para agentes de código
(`adenaufal/anti-slop-writing` e `jalaalrd/anti-ai-slop-writing`, ambos no
GitHub). Não foi possível abrir a página da Wikipédia diretamente nesta
sessão (bloqueio de rede do ambiente — o mesmo caso documentado em
`references/research.md`), então a lista abaixo foi reconstruída a partir
de múltiplas fontes secundárias que a resumem; trate como um guia sólido,
não como transcrição literal.

## Vocabulário a evitar

Em inglês, os "tiques" mais documentados são palavras como *delve*,
*tapestry*, *landscape*, *testament*, *vibrant*, *pivotal*, *underscore*,
*foster*, *enhance*, *crucial*, *intricate* — usadas fora de contexto
técnico, quase sempre como enchimento. Os equivalentes em português que
aparecem com a mesma função de enchimento genérico: "mergulhar em" (como
abertura vaga), "panorama"/"cenário" usado a cada parágrafo, "essencial"/
"fundamental"/"crucial" empilhados sem critério, "reforça"/"ressalta"
como verbo de transição automático, "no mundo atual" ou "no cenário
competitivo de hoje" como abertura de artigo.

Teste rápido: se a palavra poderia ser cortada da frase sem perder
informação nenhuma, ela é enchimento — corte.

## Aberturas de frase a evitar

"Certamente,", "Além disso," (Moreover), "Adicionalmente," (Additionally),
"Vale ressaltar que...", "É importante notar que..." — como abertura
automática de frase, sem carregar informação nova, são reconhecidos como
tique de IA. Prefira começar a frase pelo conteúdo em si.

## A frase "Não é X, é Y" — regra especial

Este é o padrão de negative parallelism mais documentado como tique de
IA ("It's not a product launch. It's a paradigm shift.") — e é também,
quase literalmente, a fórmula da `Tese` de cada pauta desta skill (ver
`references/schema.md`: "Você não tem um problema de IA. Você tem um
processo mal desenhado que agora também usa IA."). Isso não é
coincidência: é uma estrutura retórica genuinamente eficaz para resumir
uma virada de perspectiva em uma linha — por isso a marca a usa como
assinatura no campo `Tese`.

O problema não é a estrutura em si, é a repetição. Um texto de IA cai
nesse padrão em quase todo parágrafo; um texto bem escrito usa uma vez,
no momento de maior impacto (a tese principal, o fechamento), e escreve o
resto do texto de outro jeito. Ao transformar a `Tese` da pauta em prosa
(Fase 2) ou em roteiro (Fase 3), reserve o "não é X, é Y" para essa única
linha de maior impacto — não deixe cada parágrafo cair no mesmo molde.

## Estrutura da frase e do parágrafo

- **Varie o tamanho das frases.** Um texto de IA tende a ter frases de
  comprimento uniforme, quase todas de tamanho médio. Escrita humana boa
  alterna frase curta, frase longa, frase muito curta — isso é o que cria
  ritmo.
- **Evite o reflexo do "três".** IA generativa tende a listar tudo em
  trios (três adjetivos, três exemplos, três benefícios) mesmo quando não
  faz sentido natural. Na prosa do blog post, dois ou quatro exemplos
  passam despercebidos; três em fileira, repetido várias vezes no mesmo
  texto, chama atenção como padrão artificial. (Isso não vale para os
  campos estruturados da pauta em si — `Direcionamento` tem 4 sub-itens e
  `Estrutura esperada` tem ~5 por design, são metadados de planejamento,
  não prosa.)
- **Não force uma seção de "Conclusão"** só porque o texto está
  terminando. Termine no ritmo do argumento, não num resumo redundante do
  que já foi dito.
- **Evite o vaivém de ressalva** ("por um lado... por outro lado...",
  repetido a cada seção) — é outro tique reconhecível. Tome uma posição
  (a marca é "Provocador" e "Estratégico", não uma lista de prós e
  contras).

## Pontuação e formatação

- **Travessão (—) com moderação.** É um dos tiques mais citados — usado
  em excesso onde uma vírgula bastaria. Releia o texto procurando
  travessões: se aparecem em quase toda frase, é sinal de escrita em
  piloto automático, não de estilo.
- Evite excesso de ponto de exclamação e reticências.
- Um blog post é prosa corrida, não uma apresentação de slides: não
  transforme todo parágrafo em lista com marcadores. Bullets no artigo
  final servem para casos que realmente são uma lista (um checklist, um
  passo a passo) — não como substituto de escrever a frase.
- Não empilhe negrito em várias frases seguidas tentando destacar "os
  pontos principais" — se tudo está em negrito, nada está.

## Nunca inventar pra soar mais convincente

Isso já é regra em `references/research.md` para dados e fontes, mas vale
repetir aqui porque é também um sinal clássico de "slop": estatística
inventada, citação fabricada, ou anedota genérica ("um cliente meu uma vez
me disse...") sem que ela tenha realmente acontecido. Se não há um
exemplo real disponível, escreva o argumento sem o exemplo em vez de
inventar um que soa plausível.

## Exemplo rápido

**Genérico (soa a IA):** "No cenário competitivo atual, é importante
notar que a tecnologia, por si só, não é suficiente — as empresas
precisam de processos robustos, pessoas capacitadas e uma cultura
inovadora para realmente prosperar."

**Reescrito na voz da marca:** "Comprar a ferramenta certa não conserta
um processo quebrado. Só deixa o erro mais rápido."

A segunda versão corta o enchimento, tira o "não é só X, precisa de Y, Z
e W" (rule of three disfarçado), e termina numa frase curta que carrega
a tese sozinha — sem precisar de travessão, sem "é importante notar".
