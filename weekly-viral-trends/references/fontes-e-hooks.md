# Fontes confiáveis e critério de recorte semanal

Esta pesquisa serve para embasar um post que vai ao ar em poucos dias — se a
fonte for fraca ou o dado for inventado e alguém checar, a credibilidade de
quem publicou o post é o que quebra, não a desta skill. Por isso a barra de
verificação é tão alta aqui quanto seria para uma peça jornalística, mesmo
o resultado final sendo curto.

## Onde priorizar

1. **Consultorias e institutos de peso**: Deloitte Insights, McKinsey &
   Company / McKinsey Quarterly, BCG, PwC, Bain & Company, Gartner,
   Forrester, World Economic Forum.
2. **Publicações de pesquisa/negócios com padrão editorial alto**: MIT
   Technology Review, MIT Sloan Management Review, Harvard Business Review,
   The Economist, Bloomberg, Wall Street Journal, Financial Times.
3. **Anúncios e declarações primárias de players relevantes**: quando a
   "tendência" é um anúncio (lançamento de produto de IA, mudança de
   política de uma big tech, resultado trimestral), a fonte primária é o
   próprio anúncio da empresa ou a cobertura direta de um veículo do item 2
   — não um post de terceiros comentando o anúncio.

Evite basear uma tendência em posts de LinkedIn/X de terceiros sem fonte
primária, agregadores de conteúdo, ou threads que citam "um estudo" sem
nomear qual — eles podem ser o motivo de você ter descoberto o assunto, mas
sempre suba até a fonte original antes de incluir o achado na lista final.

## O que conta como "desta semana"

O objetivo é conteúdo com sensação de atualidade — algo que a audiência
ainda não viu todo mundo comentando. Na prática, isso quer dizer:

- Prefira material publicado ou que começou a circular amplamente nos
  últimos 7 dias corridos a partir da data da pesquisa.
- Um relatório mais antigo (algumas semanas ou até meses) ainda serve se
  algo específico o trouxe de volta à conversa **nesta semana** — uma
  citação num evento, uma nova declaração de um executivo repercutindo o
  dado, uma atualização do próprio relatório. Nesse caso, registre esse
  gatilho recente explicitamente no campo "Por que viraliza" da entrega,
  porque é ele que justifica o recorte "desta semana", não a data original.
- Descarte achados que são apenas "sempre verdade" ou "tendência de longo
  prazo já batida" (ex.: "IA vai transformar o trabalho") sem nenhum dado ou
  ângulo novo desta semana — isso não tem sensação de novidade, mesmo sendo
  tecnicamente correto.

## Como registrar a fonte

Ao montar a entrega (ver Passo 4 do `SKILL.md`), sempre inclua:

- Nome da instituição/publicação.
- Título do relatório, artigo ou declaração.
- Mês/ano de publicação (ou "esta semana" se for uma notícia do próprio
  período).
- O link exato que apareceu no resultado de busca — nunca a home do site,
  nunca uma URL "reconstruída" a partir do nome do domínio ou do título.

## Regra inegociável: nunca inventar uma fonte

Se a pesquisa não trouxer nada verificável e suficientemente recente para
um dos temas pedidos, **não invente um título, uma estatística ou uma URL
parecidos com o que existiria**. Isso é o tipo de erro que, quando descoberto
(e é fácil descobrir — basta alguém clicar no link), destrói a confiança em
qualquer conteúdo publicado a partir dele. As saídas honestas são:

- Avisar o usuário que não achou nada bom para aquele tema nesta janela de
  tempo, e perguntar se ele quer ampliar o recorte (ex.: 2 semanas em vez de
  1) ou seguir só com os temas onde a pesquisa funcionou.
- Entregar um achado um pouco mais antigo, mas deixando a data real bem
  visível na entrega, em vez de disfarçar como se fosse desta semana.

## Quando WebFetch está bloqueado mas WebSearch funciona

Em algumas sessões remotas, a política de rede do ambiente bloqueia
`WebFetch` para domínios específicos (isso já aconteceu em teste com
`mckinsey.com` e `deloitte.com`) mesmo com `WebSearch` funcionando
normalmente. Nesse caso, não dá para abrir a página original para conferir a
frase exata — o que muda o que você pode afirmar com segurança:

- Use apenas números e frases que o próprio resultado do `WebSearch` já
  mostrou como texto (no snippet) — nunca complete ou "adivinhe" o resto de
  uma estatística a partir do título do link.
- A URL registrada precisa ser uma URL que realmente apareceu nos resultados
  da busca, nunca uma inferida a partir do nome do domínio.
- Se duas fontes independentes discordarem sobre um número ou sua origem,
  não escolha uma para citar como fato — ou descarte o achado, ou (melhor
  ainda) transforme a própria divergência no ângulo do post: "todo mundo
  cita esse número, mas ninguém aponta pra mesma origem" costuma ser um
  gancho mais forte do que repetir a estatística sem crítica.

Se a ferramenta de busca não estiver disponível nesta sessão, diga isso
explicitamente ao usuário em vez de seguir citando fontes de memória — dados
de treinamento sobre "o que está em alta esta semana" não existem por
definição, então nunca preencha essa lacuna sem pesquisa real.

## Fabricando um bom hook a partir do achado

Um hook forte normalmente segue um destes padrões — use-os como ponto de
partida, não como fórmula rígida:

- **Contraste de expectativa**: "Todo mundo acha que [crença comum]. A
  [fonte] acabou de publicar um dado que diz o oposto: [dado]."
- **Número solto sem contexto** (que obriga a pessoa a continuar lendo/
  assistindo para entender): "[X]% dos [público] fazem [ação surpreendente]
  — e a [fonte] mostra por que isso devia te preocupar."
- **Citação direta de autoridade**: usar a frase textual de um executivo/
  pesquisador de peso, especialmente se for uma frase mais ousada do que o
  público esperaria dessa pessoa/instituição.
- **Pergunta que incomoda**: transformar o achado numa pergunta que o
  público não quer responder em voz alta (ex.: "Sua equipe de vendas ainda
  faz isso que a McKinsey diz que já não funciona?").

Evite hooks que começam explicando contexto ("Um novo estudo da Deloitte
mostrou que...") — isso é informação, não gancho; o contexto e a fonte vão
no corpo do post, o hook é só a faísca que faz a pessoa parar de rolar o
feed.
