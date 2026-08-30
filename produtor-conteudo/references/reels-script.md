# Fase 3 — Transformar um blog post em roteiro de Reels

Assim como a Fase 2, esta fase só roda depois de aprovação — não gere o
roteiro de Reels de um artigo que o usuário ainda nem viu ou aprovou como
blog post. Pergunte, se não estiver claro, se é para transformar todos os
artigos aprovados ou só alguns.

O roteiro não é um resumo do blog post — é uma tradução da mesma tese para
um formato de 30-60 segundos, feito para prender atenção nos primeiros 3
segundos e persuadir sem soar a um discurso de vendas. Leia
`assets/brand-profile.md` antes de escrever: a marca tem regras específicas
de tom, léxico e posicionamento que um roteiro genérico de "dicas virais"
vai violar.

## Regra de ouro: pensadora, não executora

Este é o ponto mais fácil de errar e o mais importante de acertar. O
roteiro nunca deve:

- Oferecer para fazer o trabalho pela pessoa ("eu resolvo isso pra você",
  "contrate minha consultoria para implementar", "faço seu RevOps").
- Prometer um resultado numérico específico como se fosse um serviço
  executado ("aumento sua conversão em X%").
- Terminar num CTA de venda direta.

O roteiro deve sempre:

- Revelar uma forma de enxergar o problema que a audiência não tinha —
  a autoridade dela vem de mostrar um ângulo, não de terceirizar a
  execução (ver "Diagnóstico de Autoridade" em `assets/brand-profile.md`).
- Terminar convidando à reflexão, ao comentário, ou a seguir para mais
  perspectiva — nunca a "chamar no direct para eu resolver".
- Manter a pergunta em aberto quando fizer sentido: um roteiro que entrega
  a resposta completa e fechada tira o motivo de comentar ou seguir; um que
  provoca sem ser vago demais gera engajamento genuíno.

Se o brand profile do usuário for diferente do padrão desta skill e não
tiver essa mesma restrição, siga o que o brand profile efetivamente
fornecido pedir — a regra acima é a leitura padrão de "pensadora, não
executora", não algo travado no código.

## Estrutura do roteiro

Use o Método V.R.A. da marca (Vibe / Rótulo / Ação — ver
`assets/brand-profile.md`) para calibrar tom, vocabulário e mecanismo de
explicação (analogias do cotidiano), e monte o roteiro nestes blocos:

1. **Hook (0-3s)** — se a pauta já tiver um `social_headline` sugerido na
   Fase 1.2 e aprovado pelo usuário, use-o como ponto de partida do hook em
   vez de inventar um novo do zero (ajuste o texto se o ritmo do roteiro
   pedir, mas não descarte a headline já aprovada sem motivo). Se não
   houver `social_headline`, construa o hook em uma das formas abaixo,
   sempre curto (10-14 palavras cabe bem em 3 segundos falados):
   - *Afirmação polêmica*: a `Tese` da pauta dita direto, sem suavizar.
   - *Gap de curiosidade*: promete uma revelação sem entregar ainda
     (`Narrativa comum` invertida como pergunta retórica).
   - *Problema + promessa*: "Se sua empresa ainda [faz X do jeito errado],
     isso muda como você vê o problema" — usa a `Narrativa comum` como o
     "X".
   O hook aparece como texto na tela E como primeira fala — teste mudo
   (sem áudio) antes de gravar: se o texto na tela sozinho não segura a
   atenção, o hook ainda não está pronto.
2. **Tensão (3-8s)** — nomeia a crença comum que a audiência carrega
   (`Narrativa comum` da pauta) de um jeito que a pessoa se reconheça nela.
3. **Virada (8-20s)** — revela a `Realidade`/`Ângulo` usando uma analogia
   do cotidiano (o mecanismo de "Ação" do método V.R.A.) em vez de jargão
   técnico. É o coração persuasivo do roteiro.
4. **Prova (20-35s, opcional)** — 1 estatística citável da pesquisa da
   Fase 1 (`sources` da pauta), dita rápido e com atribuição clara
   ("segundo a Deloitte..."). Só inclua se não quebrar o ritmo.
5. **Micro-gancho (opcional, antes dos 35s em roteiros de 45s+)** — uma
   linha curta que promete que "o ponto principal" ainda está por vir
   ("mas isso não é nem a parte mais importante"). É onde a maioria dos
   Reels perde audiência (a metade do vídeo); um micro-gancho recupera
   quem estava prestes a rolar pra próxima.
6. **Tese / Insight (35-50s)** — a frase de efeito que resume a virada de
   perspectiva. É o momento mais "salvável"/citável do vídeo.
7. **CTA de posicionamento (50-60s)** — convite a comentar, salvar ou
   seguir para mais perspectiva estratégica — nunca a contratar execução.

Ajuste os tempos livremente conforme a duração real desejada (Reels mais
curtos de 15-20s cortam direto do Hook para a Tese, sem Prova nem
micro-gancho).

Antes de finalizar o texto de qualquer bloco falado, revise contra
`references/anti-slop.md` — um roteiro que soa a texto gerado por IA
(cheio de "não é só X, é Y" repetido, travessão em toda frase, "é
importante notar que...") quebra o efeito de alguém falando com convicção
direto pra câmera, que é o que faz um Reels reter atenção.

## Formato de entrega

Monte o roteiro como uma tabela com as colunas: **Tempo | Cena/Visual |
Fala (locução) | Texto na tela**. Depois da tabela, inclua uma sugestão de
legenda (caption) para o post e 5-8 hashtags relevantes ao tema da pauta.

Entregue como `.docx` (via skill `docx`) por padrão, ou como texto simples
se o usuário pedir algo mais rápido de colar num teleprompter/app de
edição.
