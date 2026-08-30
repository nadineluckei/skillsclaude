# Pesquisador-Temas

Skill para pesquisa de temas em duas frentes: rápidos (trends, notícias, social media) e robustos (dores do mercado + temas em alta em fontes executivas).

## Estrutura

- **SKILL.md** — Instruções completas da skill
- **references/sources.md** — Fontes de pesquisa recomendadas e como buscar
- **references/schema.md** — Estrutura JSON esperada para gerar .docx
- **references/example-research.json** — Exemplo pronto de pesquisa
- **scripts/generate_docx.js** — Script para gerar .docx a partir de JSON

## Como usar

### 1. Pesquisar

Peça para Claude:
```
Pesquisador-Temas: pesquisa rápida sobre IA
Pesquisador-Temas: pesquisa robusta sobre marketing e vendas
Pesquisador-Temas: pesquisa completa sobre estratégia de conteúdo
```

### 2. Entregar em .docx

Estruture a pesquisa em JSON (ver `references/schema.md`), depois rode:

```bash
cd scripts/
npm install  # primeira vez só
node generate_docx.js ../research.json ../output.docx
```

## Referências

- `references/schema.md` — Como estruturar o JSON
- `references/sources.md` — Onde pesquisar (fontes prioritárias)
- `references/example-research.json` — Exemplo completo pronto

Leia o SKILL.md para instruções completas sobre como pesquisar cada frente.
