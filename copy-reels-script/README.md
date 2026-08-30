# Copy-Reels Script Skill

**Escrita viral de Instagram Reels & TikTok com instruções de produção visual integrada.**

Generate high-converting short-form video copy with proven hook patterns, CTA strategy, and quality gates. Part of the modular Copy-Reels system.

## Overview

This skill provides deep copywriting guidance for 30-60s viral Reels/TikTok videos focused on:

- **Hook Patterns**: 9 proven patterns (Identity Call, Contrarian Strike, Open Loop, Confession, Results First, Mistake Warning, List Tease, Direct Question, POV/Relatable)
- **Timing Structure**: Hook (0-3s) → Setup (3-8s) → Solution (8-20s) → Benefit (20-27s) → CTA (27-30s)
- **Gen Z Psychology**: Authenticity requirements, scroll-past epidemic data, 3-second retention thresholds
- **CTA Strategy**: Soft vs hard sell spectrum, placement rules, natural continuation
- **Testing Framework**: A/B testing methodology, confidence scoring (🟢🟡🔴), batch variation approach
- **Quality Gates**: Pre-launch checklists covering voice, authenticity, timing, AI-slop detection

## Usage

### 1. Basic Workflow

**Input**: Brand context, target audience, platform, content objective  
**Output**: JSON script file → .docx document with structured roteiro

### 2. JSON Structure

See `references/schema.md` for full field documentation. Basic outline:

```json
{
  "date": "2026-08-30",
  "metadata": {
    "objetivo": "conversão | awareness | engagement",
    "publico": "Descrição detalhada do público",
    "plataforma": "Reels | TikTok | YouTube Shorts",
    "duracao": "30s | 45s | 60s",
    "tom": "Seu tom de voz"
  },
  "roteiroPrincipal": {
    "hook": { "texto": "...", "padrao": "Results First", "confianca": "🟢 Alta" },
    "setup": { "texto": "..." },
    "solucao": { "texto": "..." },
    "benefit": { "texto": "..." },
    "cta": { "texto": "...", "tipo": "soft | hard" }
  },
  "hookVariations": [
    { "variacao": 1, "padrao": "Identity Call", "texto": "...", "confianca": "🟢" }
  ],
  "ctaVariants": [
    { "texto": "...", "tipo": "soft", "notaDeUso": "..." }
  ],
  "testingNotes": {
    "metricaPrincipal": "3s retention",
    "duracao": "3-5 dias",
    "benchmark": "70%+ @ 3s"
  },
  "qualityChecks": {
    "hookPor3s": true,
    "silentTest": true,
    "autenticoTom": true,
    "aiSlops": false,
    "ctaEspecifico": true,
    "batchVariations": true,
    "testedMindset": true
  },
  "notasBrand": {
    "alinhamentoComMarca": "...",
    "exemploBrand": "..."
  }
}
```

### 3. Generate .docx

```bash
cd scripts/
npm install
node generate_docx.js ../seu-script.json ../output.docx
```

Output: Formatted Word document with all sections ready to share with creators/editors.

### 4. Example

See `references/example-script.json` for full worked example: "Atribuição Multi-Channel: O Pesadelo Real"

- Metadata: objetivo=conversão, publico=Heads de marketing B2B, plataforma=Reels, duracao=30s, tom=provocador
- Hook: Results First pattern ("71% dos CMOs...")
- 5 hook variations for A/B testing
- 3 CTA variants (soft to hard)
- Testing notes with benchmarks
- Quality checks (all passing)

## Key Concepts

### 1. Hook Patterns (9 Total)

Each pattern anchors to a psychological trigger:

| Pattern | Trigger | Example | Confidence |
|---------|---------|---------|------------|
| **Identity Call** | Self-recognition | "Se você está tentando crescer online..." | 🟢 |
| **Contrarian Strike** | Confrontation | "Tudo que você sabe sobre X está errado" | 🟢 |
| **Open Loop** | Curiosity gap | "Descobri 3 coisas que..." | 🟡 |
| **Confession** | Authenticity | "Eu cometi esse erro por 2 anos" | 🟢 |
| **Results First** | Immediate value | "71% dos CMOs dizem que..." | 🟢 |
| **Mistake Warning** | Social proof (negative) | "Não cometa esse erro com seus leads" | 🟢 |
| **List Tease** | Structured curiosity | "5 truques que ninguém fala" | 🟡 |
| **Direct Question** | Engagement trigger | "Qual é seu maior desafio com atribuição?" | 🟢 |
| **POV/Relatable** | Perspective shift | "Ponto de vista de quem cresceu 300%" | 🟢 |

### 2. The 3-Second Threshold

**Critical metric for short-form success:**
- Viewers decide to stay/leave in first 3 seconds
- Benchmark: 70%+ retention @ 3s
- Hook must land **completely** within 0-3s window
- Visual must support VO sync (see copy-reels-producao)

### 3. Soft vs Hard CTA Spectrum

| Soft | Middle | Hard |
|------|--------|------|
| "Salva esse" | "Comenta sua experiência" | "Testa free agora" |
| "Assista até fim" | "Entra no link" | "Compra hoje" |
| Low friction, re-engagement | Moderate commitment | Immediate conversion |

**Rule**: Only 1-2 hard CTAs per 10 pieces of content. Stack soft CTAs for engagement.

### 4. Testing Methodology

**Batch approach (recommended):**

1. Create 10 hook variations using different patterns
2. Run all 10 simultaneously for 3-5 days
3. Track 3s retention + view-through rate
4. Scale winning hooks (70%+ @ 3s benchmark)
5. Test 2-3 CTA variants on top-performing hooks

**Confidence scoring:**
- 🟢 High: 3+ independent sources validate (hook pattern proven across 25+ pieces)
- 🟡 Medium: 2 sources (emerging pattern, trend-dependent)
- 🔴 Low: 1 source (one-off success, not scalable)

### 5. Quality Gates (7 Checks)

✅ **hookPor3s**: Hook fully resolves within 0-3s (not setup → benefit later)  
✅ **silentTest**: Script reads naturally when silent (visual standalone communicates 70%)  
✅ **autenticoTom**: Copy matches brand voice (not AI-generic, not try-hard)  
✅ **aiSlops**: No tell-tale AI phrases ("Discover the secret", "Not X, it's Y", padding words)  
✅ **ctaEspecifico**: CTA is concrete action (not vague: "Veja mais" → "Testa free por 7 dias")  
✅ **batchVariations**: 10+ hook variations tested, not single version  
✅ **testedMindset**: Copy assumes viewer is skeptical, interruption-averse (not captive audience)

All 7 gates must pass before publication.

## Integration with Copy-Reels Producao

This skill generates the **script layer**. The companion skill `copy-reels-producao` generates the **visual/production layer**.

**Workflow:**
1. Use copy-reels-script to write/test script (hook, VO, CTA)
2. Use copy-reels-producao to map visual/timing/on-screen text to each second
3. Combine outputs into single production table: **Time | Visual | VO | Text | Transição**

See copy-reels-producao README for full integration details.

## Research & Confidence

All guidance backed by 28+ validated sources (2026):

- Short-form video production & editing (8 sources)
- Text overlay & on-screen typography (3 sources)
- Trending audio & music integration (3 sources)
- Camera techniques & framing (4 sources)
- Gen Z authenticity & tone (5+ sources)
- CTA strategy & soft/hard sell (7+ sources)

See `references/sources.md` for full bibliography and validation methodology.

## Files

```
copy-reels-script/
├── SKILL.md                          # Full copywriting instruction manual (12,000+ words)
├── README.md                         # This file
├── references/
│   ├── schema.md                     # JSON schema documentation
│   ├── sources.md                    # 28+ validated sources
│   └── example-script.json           # Worked example (Atribuição Multi-Channel)
└── scripts/
    ├── package.json                  # Node dependencies (docx ^8.5.0)
    └── generate_docx.js              # JSON → .docx converter
```

## Next Steps

1. **Write**: Create your script JSON using `references/example-script.json` as template
2. **Test**: Generate .docx, share with creative team, gather feedback
3. **Iterate**: Refine hook/CTA based on testing framework
4. **Produce**: Hand .json to copy-reels-producao for visual instructions
5. **Launch**: Combine script + production outputs into final brief

---

_Copy-Reels Script Skill v1.0 — 2026-08-30_
