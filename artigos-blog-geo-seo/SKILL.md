---
name: artigos-blog-geo-seo
description: Escreve artigos de blog estratégicos baseados em temas executivos do pesquisador-temas, com otimização robusta de SEO e GEO. Integra dados de mercado real (dores, trends, strategy) com keyword research, estrutura H1-H6, internal/external links, meta descriptions, schema markup, localização geográfica e intentionalidade. Produz conteúdo que rankeia bem em busca orgânica E converte executivos (CMOs, heads de marketing, heads de vendas).
---

# Artigos de Blog — Temas Executivos com SEO & GEO

## Visão Geral

Esta skill transforma temas executivos (pesquisados via `pesquisador-temas`) em **artigos de blog estratégicos** otimizados para:

1. **SEO Orgânico**: Rankear bem em Google/Bing para keywords de alto valor (intent comercial, dores reais)
2. **GEO-Targeting**: Endereçar públicos específicos por região/país (ex: CMOs em Brasil vs US vs EU)
3. **Conversão de Executivos**: Converter leitores (CMOs, heads de marketing, heads de vendas) em leads/clientes

**Diferencial**: Não é blog genérico. É blog que:
- Cita dados reais (dores do `pesquisador-temas`)
- Rankeia em keywords que CMOs/marketers buscam
- Tem estrutura de conversão (CTA específico, ofertas, social proof)
- Leva em conta intenção do buscador (o que essa pessoa realmente quer ao digitar essa keyword)

## Entrada Esperada

Após usar `pesquisador-temas` ou `produtor-conteudo` para definir temas e pautas, você fornece:

**Mínimo:**
- Tema/pauta aprovada (ex: "Atribuição multi-channel impossível")
- Público-alvo (ex: "CMOs em SaaS B2B, Series A-C, Brasil")
- Geografia (Brasil, US, EU, Global, ou híbrido)
- Tom de voz (provocador, educacional, consultivo, etc)

**Recomendado:**
- Lista de keywords alvo (pesquisa de keywords prévia)
- Briefing de marca (posicionamento, diferencial, valor)
- Estrutura/outline da pauta (do produtor-conteudo)
- CTA específica (cadastro newsletter, demo, webinar, etc)

**Exemplo de briefing completo:**
```
Pauta: Atribuição multi-channel impossível
Público: Heads de marketing em SaaS B2B (Series A-C), CMOs
Geografia: Brasil (foco primário) + US (secundário)
Tom: Provocador, incisivo, "estrategista de campo de batalha"
Keywords alvo: "atribuição multi-canal", "medir ROI marketing", "attribution modeling", "customer journey mapping"
Diferencial da marca: Estrategista que recusa copy-paste, ataca conceitos, não pessoas
CTA: Download whitepaper "Como Medir ROI Real em Atribuição"
```

## The Pipeline (4 Stages)

### Stage 1: Keyword Research + SEO Strategy

**Entrada**: Tema + público + geografia + keywords candidatas  
**Processo**:
1. Expandir lista de keywords (long-tail, informacional, transacional)
2. Analisar intenção de busca (o que alguém quer ao digitar essa keyword?)
3. Validar volume + dificuldade (keywords viáveis pra rankear)
4. Mapear geo-targeting (keywords por região: "atribuição Brasil", "attribution US")
5. Identificar search operators (como CMOs realmente buscam o tema)

**Output**: JSON com keywords estratificadas por intenção/geo/dificuldade

**Exemplo:**
```json
{
  "tema": "Atribuição multi-channel",
  "keywords_alvo": [
    {
      "keyword": "atribuição multi-canal",
      "volume_mensal": "320",
      "dificuldade": "35 (baixa)",
      "intencao": "informacional-comercial",
      "geo_primaria": "BR",
      "cpc_usd": "1.20",
      "recomendacao": "PRIMARY — H1, meta description, schema"
    },
    {
      "keyword": "como medir ROI marketing multi-canal",
      "volume_mensal": "180",
      "dificuldade": "28",
      "intencao": "informacional",
      "geo_primaria": "BR/US",
      "cpc_usd": "0.85",
      "recomendacao": "SECONDARY — H2, internal link"
    }
  ],
  "geo_variants": {
    "BR": ["atribuição Brasil", "atribuição multi-canal SaaS Brasil"],
    "US": ["multi-channel attribution", "revenue attribution model"],
    "EU": ["multi-channel attribution GDPR", "attribution modeling Europe"]
  }
}
```

### Stage 2: Content Structure + SEO Blueprint

**Entrada**: Keywords mapeadas + tema + público  
**Processo**:
1. Definir título H1 (inclui keyword primária, 50-60 chars)
2. Estruturar H2/H3 (subseções com keywords secundárias)
3. Dimensionamento (palavra-count alvo: 2000-3500 pra executivos B2B)
4. Elementos obrigatórios:
   - Meta description (155-160 chars, inclui keyword + CTA)
   - Schema markup (Article JSON-LD, FAQPage, Product)
   - Internal links (2-4 links pra outros artigos)
   - External links (2-3 fontes confiáveis/citações)
   - CTA em 2-3 pontos estratégicos
   - Author byline + social proof (se aplicável)
5. Geo-tagging (hreflang para variantes por região)

**Output**: Documento blueprint em Markdown com estrutura exata

**Exemplo:**
```markdown
# (H1) Atribuição Multi-Canal: Por Que 71% dos CMOs Dizem Que É Adivinhação
- Keyword primária: "atribuição multi-canal"
- Meta: "71% dos CMOs dizem que atribuição multi-canal é adivinhação. Entenda por quê e como medir ROI real. Guia completo."
- Wordcount: 2800 (alvo B2B SaaS)

## (H2) O Problema: Você Não Está Medindo Atribuição — Você Está Adivinhando
- Keyword secundária: "como medir ROI marketing"
- [Parágrafo 1: Estatística + contexto]
- [Parágrafo 2: Problema específico dos CMOs]
- [CTA 1: "Descubra seu cenário" — direciona pra quiz]

## (H2) Por Que Ferramentas Tradicionais Falham
- Keyword: "attribution modeling failed"
- [Subseção: last-click attribution problem]
- [Subseção: multi-touch attribution complexity]
- [Internal link: artigo sobre "customer journey"]

## (H2) Como Medir Atribuição Real (Estratégia Emergente)
- Keyword: "como implementar atribuição real"
- [Subseção: first-party data strategy]
- [Subseção: community-led growth metrics]
- [CTA 2: "Download whitepaper"]

## (H2) Checklist: Você Tá Pronto Pra Medir Atribuição Real?
- [Perguntas práticas]
- [CTA 3: "Avaliar readiness"]

---

**SCHEMA MARKUP**: Article (autor, data, headline, description, image)
**INTERNAL LINKS**: [customer-journey-mapping], [first-party-data-strategy]
**EXTERNAL LINKS**: Deloitte 2025 report, HBR attribution article
**GEO VARIANTS**: hreflang pt-BR, en-US, en-EU
```

### Stage 3: Redação com SEO Integrado

**Entrada**: Blueprint SEO + temas executivos + diferencial de marca  
**Processo**:
1. Escrever cada seção mantendo keywords naturais (sem keyword stuffing)
2. Usar dados reais (citações de `pesquisador-temas`, estudos consultoria)
3. Aplicar "copywriting + SEO" (não SEO puro):
   - Parágrafos curtos (2-3 frases), fáceis de ler
   - Subheadings quebram o texto (melhor UX + SEO)
   - Negrito/itálico em pontos críticos
   - Listas e bullets para scannability
4. CTAs naturais (não forçado, alinhado com stage da jornada)
5. Tone consistente com marca (provocador = incisivo, sem ser agressivo)
6. Verificar legibilidade (Flesch reading score 60+, para executivos)

**Output**: Artigo .docx ou .md pronto pra publicar

**Checklist durante redação:**
- [ ] H1 inclui keyword primária
- [ ] Primeira linha (antes de H2) resume tema em 1-2 frases
- [ ] Cada H2 começa com keyword secundária ou variação
- [ ] Parágrafos não excedem 4 linhas (mobile-first)
- [ ] Mínimo 2 dados/citações do `pesquisador-temas`
- [ ] CTA aparece em 2-3 pontos naturais (não só no fim)
- [ ] Tone alinhado com marca (revisar auto-autocrítica: "isso é copy-paste?")
- [ ] Links internos fazem sentido (não forçado)
- [ ] Meta description é convincente (155-160 chars)

### Stage 4: SEO & GEO Finalization

**Entrada**: Artigo redacionado + keywords + geo-strategy  
**Processo**:
1. Inserir meta tags:
   ```html
   <title>Atribuição Multi-Canal: Por Que 71% dos CMOs Dizem Que É Adivinhação</title>
   <meta name="description" content="71% CMOs dizem que atribuição multi-canal é adivinhação. Entenda por quê e descubra como medir ROI real. Guia completo para CMOs e heads de marketing.">
   <meta name="keywords" content="atribuição multi-canal, medir ROI marketing, attribution modeling, customer journey">
   ```

2. Inserir JSON-LD Schema:
   ```json
   {
     "@context": "https://schema.org",
     "@type": "Article",
     "headline": "Atribuição Multi-Canal: Por Que 71% dos CMOs Dizem Que É Adivinhação",
     "image": "URL da imagem",
     "datePublished": "2026-08-30",
     "dateModified": "2026-08-30",
     "author": {
       "@type": "Person",
       "name": "Nome do autor",
       "jobTitle": "Estrategista de Marketing",
       "url": "URL do autor"
     },
     "description": "71% CMOs dizem...",
     "articleBody": "[conteúdo do artigo]"
   }
   ```

3. GEO-tagging:
   ```html
   <link rel="alternate" hreflang="pt-BR" href="https://site.com/pt/atribuicao-multi-canal/">
   <link rel="alternate" hreflang="en-US" href="https://site.com/en-us/multi-channel-attribution/">
   <link rel="alternate" hreflang="en-EU" href="https://site.com/en-eu/multi-channel-attribution/">
   <link rel="alternate" hreflang="x-default" href="https://site.com/en/multi-channel-attribution/">
   ```

4. Image optimization:
   - Redimensionar pra web (1200x630 pra social preview)
   - Comprimir (< 100KB, sem perder qualidade)
   - Alt text relevante: "CMOs enfrentando problema de atribuição multi-canal"

5. Link audit:
   - [ ] Todos links internos clicáveis?
   - [ ] External links têm target="_blank" + rel="noopener"?
   - [ ] Links apontam pra páginas vivas (não 404)?

6. SEO checklist final:
   - [ ] H1 exato, sem duplicação
   - [ ] Keywords em H2/H3 (natural, sem stuffing)
   - [ ] Meta description < 160 chars, com CTA
   - [ ] Schema markup presente e válido
   - [ ] hreflang tags se multi-região
   - [ ] Internal links (2-4)
   - [ ] External links confiáveis (2-3)
   - [ ] Imagem otimizada + alt text
   - [ ] Mobile-friendly (parágrafos curtos, listas)
   - [ ] Readability score 60+ (executivos podem ler sem esforço)

**Output**: Arquivo final HTML/MD com metadata completa, pronto pra CMS

## Quality Gates

**Gate 1: Keywords**
- [ ] Mínimo 3 keywords com volume mensal >100
- [ ] Mínimo 1 keyword com dificuldade <40 (rankável)
- [ ] Keywords refletem intent real de CMOs/marketers

**Gate 2: SEO Structure**
- [ ] H1 único, contém keyword primária
- [ ] H2/H3 cobrem tópicos secundários (não repetição)
- [ ] Wordcount 2000-3500 (B2B executivo standard)
- [ ] Schema markup presente e válido (test via schema.org/validator)

**Gate 3: Conteúdo**
- [ ] 2+ dados/citações reais (não inventado)
- [ ] Diferencial de marca visível (não genérico)
- [ ] CTA clara e específica (não vaga)
- [ ] Tone consistente (revisar: "pena de marca?")

**Gate 4: Geo & Performance**
- [ ] hreflang tags se multi-região
- [ ] Meta description < 160 chars
- [ ] URL slug otimizada (keywords, sem accents)
- [ ] Internal links relevantes
- [ ] Readability 60+

Se falhar em qualquer gate, revise antes de publicar.

## Integration com Outras Skills

### Com `pesquisador-temas`:
- Input: JSON dos temas/dores identificadas
- Use: Cite dados específicos, não genéricos
- Output: Artigo que endereça dores reais do público

### Com `produtor-conteudo`:
- Input: Pauta aprovada (titulo, direcionamento, estrutura)
- Use: Estrutura já validada, só aprofundar com SEO/GEO
- Output: Artigo pronto (pode pular Stage 2, ir direto pra Stage 3)

### Com `conteudo-viral-redes`:
- Input: Dados quentes da semana
- Use: Cite achados recentes pra credibilidade
- Output: Artigo + sugestão de post curto pra LinkedIn/Reels

## When to Use This Skill

✅ **Use quando:**
- Precisa escrever blog posts que rankean em Google
- Público é executivos (CMOs, heads de marketing, heads de vendas)
- Tem temas aprovados (de pesquisador-temas ou produtor-conteudo)
- Quer endereçar múltiplas regiões (BR, US, EU)
- CTA é específica (download, demo, cadastro)

❌ **Pule se:**
- Artigo é 100% pensamento próprio (nenhuma pesquisa)
- Público é consumidor final (não B2B executivo)
- Já tem SEO setup (pule pra redação direto)
- Só quer "algo escrito rápido" (qualidade SEO leva tempo)

## Files & References

```
artigos-blog-geo-seo/
├── SKILL.md                          # Este manual
├── README.md                         # Quick-start guide
├── references/
│   ├── seo-framework.md              # SEO strategy checklist
│   ├── geo-strategy.md               # Geo-targeting guide
│   ├── keyword-research.md           # Keyword research methodology
│   └── example-article.md            # Artigo exemplo completo
└── templates/
    ├── article-template.md           # Template markdown
    └── schema-markup.json            # JSON-LD template
```

---

_Artigos Blog GEO/SEO v1.0 — 2026-08-30_
