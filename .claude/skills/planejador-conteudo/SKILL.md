---
name: planejador-conteudo
description: Desenha o planejamento trimestral com eixos temáticos mensais e pautas estruturadas, cada uma ancorada em pesquisa real dos temas aprovados. Produz documento .docx pronto com 3 pautas por mês, direcionamento estratégico completo (narrativa comum, realidade, ângulo, tese) e aprova com o usuário antes de ir para redação.
---

# Planejador de Conteúdo — Fase 1.2

## Visão geral

Esta skill desenha o **planejamento trimestral completo** em cima dos temas que foram aprovados na Fase 1.1 (Pesquisa). Cria 3 eixos temáticos mensais + pautas estruturadas, cada uma com direcionamento estratégico real (não é só uma lista de títulos).

Entrega um **documento .docx** pronto para revisão, que será **aprovado explicitamente** antes de passar para redação de blog posts.

## Processo

### Passo 1 — Confirme os temas aprovados

Você só trabalha com os temas que passaram no gate de aprovação da Fase 1.1. Se o usuário não tiver feito essa pesquisa ainda, **recomende iniciar com `pesquisador-conteudo`** antes de começar o planejamento.

### Passo 2 — Desenhe o arco do trimestre

Usando os temas aprovados, decida a **progressão dos 3 eixos temáticos mensais**. Eles não são soltos — formam uma jornada com lógica de causa-e-efeito.

**Pergunta-chave**: Se alguém ler os 3 meses seguidos, que ideia maior vai absorver que não estava explícita em nenhuma pauta isolada? Essa é a **Narrativa Conectada** do trimestre.

Exemplo (do exemplo-plan.json):
- **Outubro**: Liderança e Decisão (como líderes pensam)
- **Novembro**: Crescimento e Eficiência (como escalar com inteligência)
- **Dezembro**: Futuro e Adaptação (como se preparar para o que vem)
- **Narrativa Conectada**: Empresas falham não por falta de ferramentas, mas por compreensão estratégica

### Passo 3 — Pesquise e escreva as pautas

Para cada mês (3 pautas por mês = 9 pautas total no trimestre):

#### 3a — Pesquisa real para cada pauta

Antes de fechar a pauta, **pesquise um respaldo real** para a afirmação da "Realidade". Reaproveite achados da Fase 1.1 e aprofunde se o ângulo específico exigir um dado mais fino.

**Regra inegociável: nunca invente uma citação.**

#### 3b — Estrutura da pauta

Toda pauta tem estes campos nesta ordem:

```
**Título**: [Tese em forma de frase de efeito, geralmente entre aspas]
(Deve ser específico o bastante para ser discordável)

**Tipo**: [Dois pilares combinados — ex.: "Liderança + Responsabilidade"]

**Headline para redes sociais**: [Frase curta e chamativa para Reels/social]

**Direcionamento**:
- Narrativa comum: [Crença que o público já aceita]
- Realidade: [O que de fato acontece — idealmente com dado pesquisado]
- Ângulo: [O recorte específico que torna publicável]
- Tese: [Frase de uma linha que resume a posição]

**Pergunta central**: [A pergunta que o artigo responde]

**Estrutura esperada**: [~5 bullets esboçando a ordem de argumentação]

**Fontes**: [1-2 citações reais que sustentam a Realidade]

**Palavras-chave**: [Termos de busca/tópico relevantes]

**Tom**: [1-2 frases descrevendo o registro]
```

Exemplo (do example-plan.json):
```
**Título**: "Seu time não falha. Você está pedindo para eles fracassarem."
**Tipo**: Liderança + Responsabilidade
**Headline para redes sociais**: "Por que seu melhor talento está saindo (e não é culpa dele)"
**Direcionamento**:
- Narrativa comum: "Time não é bom, preciso trocar pessoas"
- Realidade: A maioria dos problemas de time vem de liderança que não deixa claro: qual é a estratégia, o que mede sucesso, como decide
- Ângulo: Líderes culpam time por falta de performance quando o problema é falta de clareza na direção
- Tese: "Seus melhores talentos estão deixando porque você não é claro sobre pra onde vai."
**Pergunta central**: Por que a mesma pessoa é estrela em uma empresa e medíocre em outra?
**Estrutura esperada**: [5 bullets com roteiro]
**Fontes**: McKinsey, "Why talent is leaving..." (2024)
**Palavras-chave**: Liderança, gestão de pessoas, retenção de talentos, motivação, clareza estratégica
**Tom**: Incisivo. Responsabiliza o líder pelo fracasso, não o time.
```

**Variedade de tom**: Cada pauta deve ter tom diferente dentro do mês (provocador, educador, desafiador...).

### Passo 4 — Amarre o trimestre

Depois de escrever os 3 meses + 9 pautas, feche o documento com:

**Direcionamento geral do trimestre**:
- Progressão temática (uma linha por mês)
- Narrativa conectada
- Público-alvo
- Tom geral (checklist de adjetivos com explicação cada)

**Resumo do trimestre**:
- Total de pautas
- Frequência de publicação
- Público
- Registro de linguagem
- Foco temático
- Objetivo de posicionamento final

### Passo 5 — Gere o documento

Monte um objeto JSON no formato descrito em `references/schema.md` — veja `references/example-plan.json` como referência — **com todas as 9 pautas do trimestre**, e renderize:

```bash
cd produtor-conteudo/scripts
npm install  # se "docx" não estiver instalado
node generate_docx.js ../path/to/plan.json output.docx
```

O script garante formatação consistente (títulos, listas, negrito, hyperlinks reais).

**Se o usuário pedir outro formato** (Markdown, Google Doc, apresentação), monte o mesmo conteúdo dos passos 1-4 nesse formato em vez de rodar o script.

### Passo 6 — Gate de aprovação

Apresente o planejamento **aqui na conversa** antes de qualquer redação:

1. Compartilhe o resumo das 9 pautas com seu direcionamento (narrativa, realidade, ângulo, tese)
2. Aguarde **confirmação explícita do usuário** (responder "aprovado") — não presuma aprovação por silêncio
3. Se o usuário disser "aprovado", passa para a próxima fase
4. Se aprovar só parte (alguns meses, algumas pautas), trabalhe apenas com o aprovado

## Próxima fase

Assim que o plano for aprovado:

1. Usuário chama a skill `redator-conteudo` para redigir os blog posts de cada pauta
2. Depois, chama a skill de **roteiros de carrosséis** (ex: `roteirista-carrossel` ou similar) para criar roteiros de Reels + legendas baseado nas mesmas pautas
