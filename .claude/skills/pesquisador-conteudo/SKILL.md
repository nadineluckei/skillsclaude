---
name: pesquisador-conteudo
description: Pesquisa temas em alta e dores do mercado em fontes confiáveis (MIT Technology Review, Deloitte, McKinsey, HBR, Gartner, WEF) para alimentar o planejamento trimestral de conteúdo. Entrega uma lista de 10-15 temas candidatos com fonte e ângulo estratégico, aprova com o usuário antes de passar para planejamento.
---

# Pesquisador de Conteúdo — Fase 1.1

## Visão geral

Esta skill pesquisa temas em alta no mercado antes de desenhar qualquer pauta. Não inventa temas plausíveis — busca o que está de fato acontecendo no nicho do cliente em fontes confiáveis (MIT Technology Review, McKinsey, Deloitte, Harvard Business Review, Gartner, BCG, WEF) e cruza os achados com o perfil de marca.

Entrega uma **lista de 10-15 temas candidatos** com fonte real e ângulo estratégico, que será **aprovada explicitamente** antes de passar para a próxima fase (Planejamento Trimestral).

## Processo

### Passo 1 — Confirme o briefing mínimo

Antes de pesquisar, você precisa destes dados (verifique `assets/brand-profile.md` primeiro):

- **Briefing / posicionamento da marca**: o que a empresa/pessoa faz, o que a diferencia, que transformação vende
- **Público-alvo**: quem lê — cargo, nível de senioridade, tipo de negócio, o que já sabe e o que subestima
- **Canal e cadência**: blog, LinkedIn, newsletter, etc.; quantas peças por mês
- **Restrições**: temas a evitar, compromissos já assumidos

Se faltar público-alvo ou posicionamento, **pergunte antes de prosseguir** — sem isso a pesquisa não tem direção.

### Passo 2 — Pesquise em fontes confiáveis

Busque em:

1. **MIT Technology Review** e **MIT Sloan** — inovação, tecnologia, comportamento organizacional
2. **Harvard Business Review** — estratégia, liderança, operação
3. **McKinsey & Company** — tendências de mercado, transformação digital, people operations
4. **Deloitte Insights** — futuro do trabalho, operação, customer experience
5. **Gartner** — tecnologia, ciclos de adoção, magic quadrants
6. **Boston Consulting Group (BCG)** — competitividade, estratégia, inovação
7. **World Economic Forum** — tendências globais, future of work

**Regra inegociável: Nunca invente uma citação OU um link.** Se não encontrar a fonte completa (incluindo URL verificada), não inclua na lista.

### Passo 3 — Cruze com a marca

Para cada tema encontrado, pergunte-se:
- Faz sentido para o público-alvo dessa marca?
- Tem a ver com os 3 inimigos em comum (`assets/brand-profile.md`)?
- É um ângulo que a marca consegue defender com propriedade?

Se a resposta for não em qualquer um, deixe de fora.

### Passo 4 — Formato de entrega

Liste os **10-15 temas aprovados** assim:

```
**Tema**: [Título claro da ideia]
**Fonte**: [Publicação + data/autor]
**Link**: [URL da fonte — OBRIGATÓRIO]
**Por que em alta**: [1-2 frases: por que isso importa agora]
**Ângulo para a marca**: [como esse tema toca nos pilares/inimigos da marca]
```

Exemplo:
```
**Tema**: "Líderes que focam em clareza estratégica retêm mais talentos que líderes com 'cultura top'"
**Fonte**: McKinsey, "Why talent is leaving your organization" (2024)
**Link**: https://www.mckinsey.com/articles/why-talent-is-leaving-your-organization
**Por que em alta**: Retenção de talento é a crise #1 em operações agora; empresas estão percebendo que "cultura legal" sem direção clara não segura ninguém
**Ângulo para a marca**: Conecta com o pilar de Liderança + o inimigo "ditadura das receitas prontas" (a fórmula genérica de "basta ter boa cultura" não funciona)
```

**Regra crítica**: Cada tema DEVE ter um link verificado. Se não conseguir encontrar a URL da fonte, não inclua o tema na lista — é preferível entregar 8-12 temas com links reais do que 15 temas com fontes inventadas.

### Passo 5 — Gate de aprovação

Envie a lista para aprovação **antes de qualquer planejamento**:

1. Pergunte como o usuário quer revisar: direto na conversa, como arquivo, ou por e-mail?
2. Se for e-mail, use `luckeitolotti@gmail.com` (do brand-profile) ou outro indicado
3. Envie a lista clara e aguarde **confirmação explícita**
4. Se o usuário aprovar só parte dos temas, trabalhe apenas com os aprovados

## Próxima fase

Assim que temas forem aprovados, o usuário chama a skill `planejador-conteudo` para desenhar o planejamento trimestral em cima desses temas.
