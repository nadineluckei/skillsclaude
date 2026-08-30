# Pesquisa e fontes confiáveis (Fase 1.2)

Esta é a pesquisa que sustenta uma pauta já escolhida — para a etapa
anterior, que descobre quais temas valem virar pauta antes de qualquer
uma delas existir, ver `references/topic-research.md` (Fase 1.1). As duas
etapas usam a mesma lista de fontes confiáveis, mas com alvos diferentes:
lá é descoberta de tema, aqui é comprovação de uma afirmação específica.

Uma pauta forte não é uma opinião — é uma opinião apoiada em algo real. O
campo `Realidade` de cada pauta (ver `references/schema.md`) fica muito mais
forte quando cita um dado, estudo ou achado concreto em vez de afirmar algo
que soa verdadeiro mas não foi checado. Esta etapa existe para isso: antes de
fechar uma pauta, pesquisar um respaldo real para a afirmação central dela.

## Quando pesquisar

Depois de rascunhar a `Narrativa comum` e a `Realidade` de uma pauta (ainda
em fase de esboço), rode 1-3 buscas focadas na afirmação da `Realidade` —
não no tema genérico do mês. Por exemplo, para a pauta "Decisão sem dados é
opinião", a busca certa é algo como `"correlação vs causalidade" decisão
empresarial dados` ou `data-driven decision making failure McKinsey`, não
"tomada de decisão" (genérico demais para achar algo citável).

## Onde priorizar

Não é qualquer link que sustenta uma tese publicada sob o nome de alguém.
Priorize, nesta ordem:

1. **Pesquisa e institutos de peso**: MIT Technology Review, MIT Sloan
   Management Review, Harvard Business Review, McKinsey & Company /
   McKinsey Quarterly, Deloitte Insights, BCG, PwC, Bain & Company, Gartner,
   Forrester, World Economic Forum.
2. **Veículos de negócios com padrão editorial alto**: The Economist,
   Bloomberg, Wall Street Journal, Financial Times, Harvard Business Review
   (de novo, porque é excelente para isso).
3. **Estudos acadêmicos ou de universidades** (Stanford, Wharton, etc.)
   quando disponíveis publicamente.

Evite basear uma tese em posts de blog sem fonte primária, LinkedIn de
terceiros, ou agregadores de conteúdo — eles podem ser úteis para achar a
pista, mas siga até a fonte original antes de citar.

Prefira material dos últimos 2-3 anos, a menos que esteja citando um estudo
clássico/consolidado (ex.: um paper seminal sobre viés cognitivo) — nesse
caso a idade não enfraquece a citação.

## Como usar o que foi encontrado

1. Escolha 1-2 fontes por pauta — o suficiente para sustentar a afirmação
   sem virar uma revisão bibliográfica.
2. Registre cada uma no campo `sources` da pauta:
   `{"title": "...", "publication": "...", "year": 2024, "url": "..."}`.
3. **Costure o dado na própria `Realidade`**, não deixe a citação isolada
   numa lista à parte sem conexão com o argumento. Ex.: em vez de
   "Empresas tomam decisões ruins com dados", escreva algo como "Segundo a
   McKinsey (2024), X% dos executivos dizem confiar em dados para decidir,
   mas Y% admitem já ter revertido uma decisão data-driven que deu errado" —
   o número muda a força da frase.
4. Guarde o link exato usado (não a home do site) — ele vai ser reaproveitado
   como citação real no blog post na Fase 2.

## Regra inegociável: nunca inventar uma fonte

Se depois de pesquisar de verdade não aparecer nada que sustente a
afirmação, **não invente um título, uma publicação ou uma URL parecidos com
o que existiria** — isso é o tipo de erro que destrói a credibilidade da
autora se alguém clicar no link e ele não existir ou disser outra coisa.
Nesse caso, duas saídas honestas:

- Suavize a frase para o que é razoável sem atribuição (“um padrão comum
  observado em operações de médio porte é...”, “na prática de campo, é
  comum ver...”), e deixe claro que é observação, não estatística.
- Ou ajuste o ângulo da pauta para algo que a pesquisa real sustenta melhor.

Se a ferramenta de busca não estiver disponível na sessão em que a skill
está rodando, avise o usuário disso explicitamente em vez de seguir citando
fontes de memória — dados de treinamento podem estar desatualizados ou
simplesmente errados.

## Quando WebFetch está bloqueado mas WebSearch funciona

Em algumas sessões remotas, a política de rede do ambiente bloqueia
`WebFetch` para domínios específicos (isso aconteceu em teste com
`mckinsey.com` e `deloitte.com` numa sessão real) mesmo com `WebSearch`
funcionando normalmente. Nesse caso, não dá para abrir a página original
para conferir a frase exata — mas isso não significa que vale tudo:

- Use apenas trechos que o próprio resultado do `WebSearch` mostrou como
  texto (não invente uma frase "provável" baseada no título do link).
- Se duas ou mais fontes independentes (nas buscas) discordarem sobre a
  origem ou a solidez de uma estatística famosa, trate isso como um sinal
  para não usá-la como fato — ou, melhor ainda, use o próprio questionamento
  como parte do ângulo da pauta (ver exemplo abaixo). Isso costuma gerar um
  ângulo mais interessante do que repetir o número sem crítica.
- A URL registrada em `sources` precisa ser uma URL que realmente apareceu
  nos resultados da busca, nunca uma inferida ou "reconstruída" a partir do
  nome do domínio.

**Exemplo real** (achado testando esta skill): a estatística "70% das
transformações digitais falham", atribuída à McKinsey, é repetida em
incontáveis artigos — mas analistas independentes rastrearam a origem até
uma estimativa "não científica" de 1993 e nunca encontraram a metodologia
por trás do número. Em vez de descartar a pauta, isso virou o próprio
ângulo: uma pauta cética sobre por que o mercado repete estatísticas de
consultoria sem checar a fonte é mais forte — e mais alinhada a um
posicionamento que recusa "copia e cola" — do que citar o número como fato.
