# Artigos de Blog — GEO + SEO para Temas Executivos

**Escreva blog posts que rankean em Google E convertem CMOs/heads de marketing.** 

Integra temas executivos (de `pesquisador-temas`) com keyword research, estrutura SEO, geo-targeting e copywriting de conversão.

## Quick Start

### 1. Forneça o Briefing

```
Pauta: Atribuição multi-channel
Público: Heads de marketing SaaS B2B Brasil
Geografia: Brasil (foco), US (secundário)
Tom: Provocador
Keywords: "atribuição multi-canal", "medir ROI", "attribution modeling"
CTA: Download whitepaper
```

### 2. Execute o Pipeline

```bash
cd scripts/
npm install
node article-generator.js --pauta "Atribuição multi-channel" \
  --geo "BR,US" \
  --publico "CMO SaaS" \
  --output "artigo.md"
```

### 3. Outputs

Recebe:
- ✅ `keywords-research.json` (keywords mapeadas por intent/geo)
- ✅ `article-seo-blueprint.md` (estrutura com SEO points)
- ✅ `artigo-final.md` (redação pronta)
- ✅ `schema-markup.json` (JSON-LD schema)
- ✅ `seo-checklist.md` (validação final)

## The 4-Stage Pipeline

| Stage | O Quê | Duração |
|-------|-------|---------|
| **1. Keyword Research** | Expandir keywords, analisar intenção, mapear geo | 15-20 min |
| **2. SEO Blueprint** | Estruturar H1-H6, dimensionar, definir elementos SEO | 10-15 min |
| **3. Redação** | Escrever com copywriting + SEO integrado | 45-60 min |
| **4. Finalization** | Meta tags, schema, hreflang, image, audit | 10-15 min |

**Total**: 80-110 min ponta a ponta

## Diferencial desta Skill

🎯 **Não é genérico**
- Cita dados reais (dores de `pesquisador-temas`)
- Rankea em keywords que CMOs realmente buscam
- Tem estrutura de conversão (CTA específica, social proof)

📍 **Geo-Targeted**
- Variantes por região (BR, US, EU, Global)
- hreflang tags automáticas
- Linguagem adaptada (PT-BR vs EN-US)

🔍 **SEO-First Mas Human**
- Keywords naturais (sem stuffing)
- Readabilidade alta (Flesch 60+)
- Tone alinhado com marca
- Schema markup + internal links

💼 **Para Executivos**
- Parágrafos curtos (2-3 linhas)
- Bullets e listas (scannable)
- Dados específicos (não "deve-se")
- CTA clara (demo, download, cadastro)

## How to Use

### Scenario 1: Tenho uma pauta do produtor-conteudo
```
✓ Já tenho tema aprovado, público, estrutura
→ Vá direto pro Stage 3 (Redação)
→ Use blueprint pronto do produtor-conteudo
→ Tempo: 45-60 min + 15 min finalization
```

### Scenario 2: Tenho tema mas não keywords pesquisadas
```
✓ Tenho tema + público + geografia
→ Comece no Stage 1 (Keyword Research)
→ Depois Stage 2-4 normais
→ Tempo: 80-110 min (full pipeline)
```

### Scenario 3: Tenho tema + keywords + blueprint
```
✓ Já tudo mapeado
→ Vá direto Stage 3 + Stage 4
→ Tempo: 60-75 min
```

## Integration Points

### Com `pesquisador-temas`:
```
Pesquisador identifica:
- Tema: "Atribuição multi-channel impossível"
- Dores: "71% CMOs dizem que é adivinhação"
- Estratégias: "First-party data strategies"

Você usa:
- Cita os dados específicos (credibilidade)
- Endereça as dores (relevância)
- Menciona estratégias emergentes (thought leadership)
```

### Com `produtor-conteudo`:
```
Produtor fornece:
- Pauta com Titulo, Direcionamento, Estrutura
- Temas aprovados, tom definido

Você usa:
- Estrutura da pauta (não reinventar)
- Aprofunda com keywords + SEO
- Mantém tom aprovado
- Adiciona meta tags + schema
```

### Com `conteudo-viral-redes`:
```
Viral identifica:
- Dados quentes da semana
- Ângulos de viralização

Você usa:
- Cite achados recentes (urgência)
- Use como social proof no artigo
- Sugira post curto pra LinkedIn/Reels
```

## SEO Checklist (Validação Final)

### Keywords
- [ ] Mínimo 3 keywords com volume >100
- [ ] Mínimo 1 keyword rankável (dificuldade <40)
- [ ] Long-tail keywords incluídas (menos competição)

### Structure
- [ ] H1 único, contém keyword primária
- [ ] H2/H3 cobrem tópicos secundários
- [ ] Wordcount 2000-3500 (B2B standard)

### On-Page
- [ ] Meta description < 160 chars, com CTA
- [ ] Schema markup válido (Article JSON-LD)
- [ ] Internal links (2-4) relevantes
- [ ] External links confiáveis (2-3)

### Geo & Technical
- [ ] hreflang tags se multi-região
- [ ] URL slug otimizada (keywords, sem accents)
- [ ] Image otimizada (<100KB) + alt text
- [ ] Mobile-friendly (read no celular)

### Content
- [ ] 2+ dados/citações reais (não inventado)
- [ ] Diferencial de marca visível
- [ ] CTA específica (não vaga)
- [ ] Readability score 60+ (Flesch)
- [ ] Tone consistente (sem copy-paste)

## CLI Usage

```bash
# Full pipeline
node article-generator.js \
  --pauta "Seu tema" \
  --publico "Seu público" \
  --geo "BR,US" \
  --tone "provocador" \
  --cta "Download whitepaper" \
  --wordcount "2500" \
  --output "artigo.md"

# Com blueprint pronto (pula Stage 1-2)
node article-generator.js \
  --blueprint "blueprint.md" \
  --tone "provocador" \
  --output "artigo.md"

# Só keyword research
node article-generator.js \
  --keywords-only \
  --tema "Atribuição" \
  --geo "BR,US"
```

## Files Structure

```
artigos-blog-geo-seo/
├── SKILL.md                          # Manual completo (4 stages)
├── README.md                         # Este arquivo
├── references/
│   ├── seo-framework.md              # SEO strategy checklist
│   ├── geo-strategy.md               # Geo-targeting guide
│   ├── keyword-research.md           # Keyword research methodology
│   └── example-article.md            # Artigo exemplo
├── templates/
│   ├── article-template.md           # Template markdown
│   ├── blueprint-template.md         # SEO blueprint template
│   └── schema-markup.json            # JSON-LD template
└── scripts/
    ├── article-generator.js          # Main orchestrator
    └── package.json                  # docx, node-fetch
```

## Quality Gates

✅ **Passa se:**
- Keywords rankáveis + volume real
- H1 único com keyword
- 2+ citações reais
- Meta description convincente
- Schema markup válido
- Readability 60+

❌ **Falha se:**
- Só 1 keyword viável
- H1 genérico
- Dados inventados
- Meta muito longo (>160)
- Tone inconsistente com marca

## Next Steps

1. **Forneça briefing** (pauta, público, geo, tone, CTA)
2. **Execute pipeline** (cmd acima, ou manual stages)
3. **Revise outputs** (keywords, blueprint, redação)
4. **Aprove SEO checklist** (todos items ✅)
5. **Publique no CMS** (com tags, metadata, schema)
6. **Monitore ranking** (track keywords no GSC)

---

_Artigos Blog GEO/SEO v1.0 — 2026-08-30_
