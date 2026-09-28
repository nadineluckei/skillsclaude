---
name: radar-buzz-estrategico
description: Pesquisa os assuntos que mais geraram buzz nos ÚLTIMOS 7 DIAS nas redes sociais e na internet — polêmicas e movimentos de empresas, investimentos e mercado financeiro, influenciadores e creators, notícias e acontecimentos de cultura pop — e cria uma PONTE entre cada assunto e um conteúdo estratégico empresarial sobre marketing, processos, dados, vendas ou liderança, ancorada em conceitos reais de consultorias e publicações renomadas (McKinsey, Deloitte, Harvard Business Review, BCG, Bain, Gartner, MIT Sloan, PwC). Usa WebSearch/WebFetch de verdade, com evidência concreta de buzz e fonte real para o conceito — nunca inventa dado, citação ou link. Entrega 5-8 pautas com o fato do momento, o conceito de gestão que o explica, a tese que liga os dois, o ângulo de marca e hooks prontos. Use sempre que o usuário pedir "o que está bombando essa semana", "pega um assunto do momento e conecta com negócios", "newsjacking", "pauta de oportunidade", "trend para virar conteúdo de estratégia", "o que todo mundo está falando e dá pra usar", ou quiser surfar um assunto viral com conteúdo de autoridade — mesmo sem usar essas palavras exatas.
---

# Radar de Buzz Estratégico

## Visão geral

Esta skill faz o caminho **inverso** das outras skills de pesquisa do
repositório. A `pesquisador-conteudo` e a `conteudo-viral-redes` partem de
relatórios de consultorias e procuram o que neles pode viralizar. Esta aqui
parte **do que já viralizou** — o assunto que todo mundo está comentando
nesta semana, dentro ou fora do mundo dos negócios — e encontra o conceito
de gestão que explica aquele fato melhor do que os comentários rasos que
estão circulando.

O valor está na **ponte**: pegar a atenção que já existe (a demissão
polêmica do CEO, o influenciador que perdeu patrocínio, a ação que
despencou 30% num dia, o lançamento que deu errado, o meme que todo mundo
compartilhou) e transformá-la numa lição de marketing, processos, dados,
vendas ou liderança que o público não enxergaria sozinho — com o respaldo
de um conceito que HBR, McKinsey, Deloitte & cia. já documentaram.

Uma boa entrega passa em três testes ao mesmo tempo:

1. **O buzz é real e recente** — há evidência verificável de que o assunto
   repercutiu forte nos últimos 7 dias.
2. **O conceito é real e bem aplicado** — existe de fato, está atribuído à
   fonte certa, e explica o fato em vez de ser colado nele à força.
3. **A ponte gera insight** — a conclusão não é óbvia; ela muda a forma
   como o leitor enxerga o assunto do momento *e* o próprio negócio.

## Passo 1 — Alinhar o escopo (rápido)

Leia `assets/brand-profile.md` para saber para quem é o conteúdo (pilares,
os 3 inimigos em comum, tom). Se o usuário indicou outra marca na
conversa, use a da conversa.

Confirme ou assuma — dizendo o que assumiu — o seguinte:

- **Recorte geográfico**: padrão é **Brasil + global** (o que repercutiu
  aqui, inclusive assuntos internacionais que viralizaram no Brasil).
- **Pilares prioritários**: marketing, processos, dados, vendas, liderança.
  Padrão: todos, buscando pelo menos 3 pilares diferentes na entrega final.
- **Formato de destino**: Reels/TikTok, carrossel, LinkedIn. Padrão:
  hooks para LinkedIn e Reels.
- **Quantidade**: padrão de **5 a 8 pautas**.
- **Assuntos a evitar**: além das regras de sensibilidade do Passo 3,
  pergunte só se o usuário sinalizar algo (ex.: "nada de política").

Se o pedido já é claro ("me traz o que bombou essa semana e conecta com
vendas"), não pergunte nada — comece.

## Passo 2 — Varrer o buzz dos últimos 7 dias

Calcule a janela a partir da data de hoje (ex.: pesquisa em 28/09 → de
21/09 a 28/09) e deixe essa janela explícita nas buscas e na entrega.

Faça buscas separadas por **categoria de buzz** — nunca uma busca genérica
única. Mínimo de uma rodada por categoria:

| Categoria | O que procurar |
|---|---|
| **Empresas** | demissões/contratações de CEO, crises de marca, recalls, lançamentos que deram muito certo ou muito errado, rebranding, fusões, greves, falhas de atendimento que viralizaram |
| **Investimentos e mercado** | ações que dispararam ou despencaram, IPOs, balanços surpreendentes, recuperações judiciais, fraudes contábeis, cripto, bets, rodadas de startups |
| **Influenciadores e creators** | polêmicas, cancelamentos, publis que deram errado, lançamentos de produto de creator, rompimentos com marcas, trends que um creator iniciou |
| **Notícias e cultura** | tecnologia/IA, esporte, entretenimento, reality shows, memes, eventos, regulação que afeta empresas |

Para cada candidato, registre a **evidência de buzz** — pelo menos uma de:

- cobertura por **2+ veículos independentes** na janela;
- presença em listas de trending (Google Trends, X/Twitter, TikTok,
  YouTube) mencionada em fonte verificável;
- números de repercussão publicados (views, menções, variação de ação,
  queda/alta de seguidores) atribuídos a uma fonte;
- repercussão entre perfis de negócios/marketing (sinal de que o público
  da marca já está falando disso).

Veja `references/fontes-de-buzz.md` para a lista de fontes, exemplos de
buscas e o que fazer quando `WebFetch` está bloqueado.

Reúna **12 a 20 candidatos** antes de filtrar — a ponte boa raramente sai
dos três primeiros assuntos que aparecem.

## Passo 3 — Filtrar os candidatos

Descarte o candidato se qualquer uma destas for verdadeira:

- **Fora da janela**: o pico de conversa foi há mais de 7 dias e nada novo
  o trouxe de volta nesta semana.
- **Buzz não verificável**: só existe em um post isolado ou agregador sem
  fonte primária.
- **Tragédia ou sofrimento humano como gancho**: mortes, desastres,
  violência, doenças, crimes contra pessoas. Usar isso como "lição de
  vendas" é oportunismo e destrói reputação. (Exceção: a *resposta
  corporativa* a uma crise pode ser analisada, com respeito, se o usuário
  pedir explicitamente.)
- **Polarização política/religiosa** como assunto central — a menos que o
  usuário peça.
- **Acusação não comprovada contra uma pessoa**: não trate alegações como
  fatos. Se o caso ainda está em apuração, fale do *fenômeno* (a reação do
  mercado, a gestão da crise), nunca afirme culpa.
- **Sem ponte honesta**: se o único conceito que "encaixa" exige distorcer
  o fato ou o conceito, fica de fora.

Regras específicas para **investimentos**: o conteúdo analisa o que o
movimento revela sobre gestão/estratégia/comunicação — **nunca** recomenda
compra ou venda de ativo, nem sugere que o público "aproveite" a queda ou a
alta. Não projete preço futuro.

## Passo 4 — Construir a ponte

Para cada candidato que sobreviveu, faça a pergunta central:

> **"Que decisão de gestão (ou falta dela) está por trás disso — e qual
> conceito de marketing, processos, dados, vendas ou liderança já explica
> esse padrão?"**

Método em 4 movimentos (detalhado em `references/ponte-narrativa.md`):

1. **Descreva o fato sem adjetivo** — o que aconteceu, em uma frase.
2. **Identifique a leitura rasa** — o que todo mundo está dizendo sobre o
   assunto (ex.: "o influenciador foi cancelado porque falou besteira").
3. **Encontre o mecanismo** — o padrão de gestão por trás do fato (ex.:
   "a marca terceirizou a própria confiança para uma pessoa sem processo
   de due diligence"). Consulte `references/biblioteca-conceitos.md` para
   o repertório de conceitos por pilar.
4. **Formule a tese** — uma frase afirmativa, discutível, que liga o fato
   ao negócio do leitor (ex.: "Contrato de publi sem critério é o CRM
   caro sem processo do marketing de influência").

**Valide o conceito com pesquisa real.** A biblioteca é um ponto de
partida, não uma fonte citável por si só. Para cada conceito escolhido,
faça uma busca que traga um link real (artigo HBR, McKinsey Insights,
Deloitte Insights etc.) e, sempre que possível, prefira um artigo
**recente** da consultoria sobre o mesmo tema ao artigo clássico — isso dá
atualidade ao conteúdo. Se não achar link real, cite o conceito pelo nome
e autor sem link, deixando claro que é referência conceitual, ou troque de
conceito.

**Cruze com a marca**: a tese deve tocar pelo menos um dos 3 inimigos em
comum do `brand-profile.md` (receitas prontas, ilusão da tecnologia,
padronização que apaga identidade) ou um dos pilares. Se não tocar,
reavalie — pode ser uma boa pauta para outra marca, não para esta.

## Passo 5 — Ranquear e entregar

Priorize as pautas com a melhor combinação de:

- **Força do buzz** (quanto o público já está falando disso);
- **Surpresa da ponte** (quão inesperada e reveladora é a conexão);
- **Aderência à marca** (quanto reforça o posicionamento);
- **Janela de vida** (ainda vai ser assunto daqui a 3-5 dias?).

Garanta variedade: no máximo 2 pautas do mesmo pilar e no máximo 2 da
mesma categoria de buzz.

Entregue direto na conversa, em Markdown, neste formato:

```markdown
## Radar de Buzz Estratégico — [DD/MM] a [DD/MM/AAAA]

### 1. [Título-manchete da pauta] · [Pilar] · Urgência: [alta/média]

**O buzz:** [o que aconteceu, 2-3 frases, com datas e números]
**Evidência de repercussão:** [veículos/trending/números] — [links reais]
**Leitura rasa (o que todo mundo está dizendo):** [1 frase]
**O conceito:** [Nome do conceito] — [autor/instituição, publicação, ano]
— [link real]. [1-2 frases explicando o conceito sem jargão]
**A ponte (tese):** [1 frase afirmativa e discutível]
**Por que funciona para a marca:** [inimigo em comum/pilar que reforça]
**Analogia sugerida:** [analogia do cotidiano no estilo V.R.A. da marca]
**Hooks:**
- LinkedIn: "[primeira frase pronta]"
- Reels/TikTok: "[fala de até 3 segundos]"
**Formato recomendado:** [Reels / carrossel / post] — [por quê, 1 frase]
**Cuidados:** [riscos de sensibilidade, pontos ainda em apuração, validade
do assunto — ou "nenhum relevante"]
```

Feche com:

- uma linha com a janela pesquisada e a data da pesquisa;
- uma lista curta de **assuntos descartados** e o motivo (ex.: "caso X —
  tragédia, fora do escopo"; "tendência Y — pico foi há 3 semanas"), para
  o usuário saber o que foi avaliado;
- a pergunta: **quais pautas aprovar** e se quer desenvolver alguma em
  roteiro de Reels (`roteirista-video`), carrossel (`roteirista-carrossel`)
  ou blog (`redator-conteudo`).

Não escreva o roteiro ou o post completo nesta skill — ela entrega a pauta
com a ponte pronta. Desenvolver a peça é um pedido separado.

## Regras inegociáveis

- **Nunca invente** buzz, número de repercussão, citação, estudo, autor,
  ano ou URL. Todo link na entrega precisa ter aparecido nos resultados de
  busca desta sessão.
- **Nunca atribua um conceito à fonte errada** (ex.: Jobs to Be Done é de
  Clayton Christensen/HBR, não da McKinsey). Na dúvida, verifique.
- **Buzz ≠ fato**: diferencie o que está confirmado do que é rumor ou
  alegação. Use "segundo [veículo]" quando for o caso.
- **Sem ferramenta de busca, sem pauta**: se `WebSearch` não estiver
  disponível, avise o usuário. O que está em alta nesta semana não existe
  nos dados de treinamento — não preencha a lacuna de memória.
- **Se a semana estiver fraca** num pilar ou categoria, diga isso em vez de
  forçar uma ponte ruim. Menos pautas boas > lista completa medíocre.
