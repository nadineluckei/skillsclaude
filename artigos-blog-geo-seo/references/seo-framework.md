# SEO Framework para Artigos de Blog

## Hierarchy: H1 → H2 → H3

**H1 (único por página)**: Keyword primária + proposta de valor
- Exemplo: "Atribuição Multi-Canal: Por Que 71% dos CMOs Dizem Que É Adivinhação"
- Características: 50-60 caracteres, específico, discordável

**H2 (2-4 por artigo)**: Keywords secundárias, tópicos principais
- Exemplo: "O Problema: Você Não Está Medindo Atribuição — Você Está Adivinhando"
- Características: Quebra lógica do argumento

**H3 (sob H2)**: Tópicos tertiary, detalhe de subseção
- Exemplo: "Por Que Last-Click Attribution Não Funciona Mais"
- Características: Aprofunda ponto específico do H2

## Keyword Placement

| Elemento | Placement | Natureza |
|----------|-----------|----------|
| **H1** | Único, começo artigo | Keyword primária |
| **First 100 words** | Parágrafo introdutório | Keyword primária + variação |
| **H2/H3** | 2-3 subheadings | Keywords secundárias |
| **Bolded text** | 1-2 frases estratégicas | Palavra-chave em negrito (natural) |
| **Meta description** | 155-160 chars | Keyword primária + CTA |
| **Alt text (image)** | Descrição imagem | Keyword variação |
| **Internal links** | Anchor text | Keyword do artigo linkado |

**Regra de Ouro**: Keywords sempre naturais. Se soa forçado, reescreva.

## Meta Description

- **Length**: 155-160 caracteres (título fica truncado no Google)
- **Includes**: Keyword primária, proposta, CTA
- **Format**: Chamativa, não descritiva

Exemplo:
```
❌ Ruim: "Este artigo trata sobre atribuição multi-canal e como medir ROI"
✅ Bom: "71% CMOs dizem que atribuição multi-canal é adivinhação. Descubra como medir ROI real. Guia completo."
```

## Schema Markup (JSON-LD)

Obrigatório:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Seu H1",
  "image": "https://URL-imagem.jpg",
  "datePublished": "2026-08-30",
  "dateModified": "2026-08-30",
  "author": {
    "@type": "Person",
    "name": "Autor",
    "url": "https://site.com/autor"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Seu site",
    "logo": "https://site.com/logo.png"
  }
}
```

Validar em: https://schema.org/validator

## Internal Links

**Objetivo**: Guiar usuário dentro do site, distribuir autoridade

- Mínimo 2, máximo 4 por artigo
- Links devem ser relevantes (não forçado)
- Anchor text = keyword do artigo linkado
- Links em contexto (dentro do parágrafo, não só rodapé)

Exemplo:
```
"Uma estratégia melhor é construir [comunidade de clientes](/artigos/community-led-growth) 
como motor de aquisição, reduzindo dependência de ads."
```

## External Links

**Objetivo**: Credibilidade, contexto, citação de fonte

- Mínimo 2, máximo 4 por artigo
- Links obrigatoriamente vivos (não 404)
- Prioridade: consultorias (Deloitte, McKinsey), journals (HBR, MIT Tech Review), dados (Gartner)
- Abrir em nova aba: `target="_blank" rel="noopener noreferrer"`

## Image Optimization

- **Dimensão**: 1200x630px (aspectratio 16:9, padrão social preview)
- **Tamanho arquivo**: < 100KB
- **Formato**: WebP (melhor compressão) + fallback JPG
- **Alt text**: Descritivo + keyword variação (ex: "CMOs enfrentando problema atribuição multi-canal")
- **File name**: keyword-separado-por-hifen.webp (não "image123.jpg")

## Readability (Flesch Score)

Alvo: 60+ (fácil para executivos lerem)

- Parágrafos: 2-3 frases máximo
- Frases: 15-20 palavras (média)
- Palavras: 1-2 sílabas (evitar jargão excessivo)
- Bullets/listas: Quebram texto, aumentam legibilidade

Ferramentas: Yoast SEO, Readable.com, Flesch-Kincaid (Word/Google Docs)

## Mobile-First

Google rankeia baseado em versão mobile primeiro.

- Sem textos muito longos (máx 3 linhas celular)
- Sem imagens que ocupem tela inteira
- Links clicáveis (mínimo 48x48px)
- Menu legível em mobile
- Velocidade < 3 segundos (test: PageSpeed Insights)

## URL Slug

- Keyword primária: "site.com/artigos/atribuicao-multi-canal"
- Sem acentos ou caracteres especiais
- Sem data (fica desatualizado visualmente)
- Max 50-60 caracteres

❌ `/artigos/2026-08-30-atribuicao-multi-canal`
✅ `/artigos/atribuicao-multi-canal`
