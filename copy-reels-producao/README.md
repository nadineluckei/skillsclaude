# Copy-Reels Producao Skill

**Instruções de produção visual para Instagram Reels & TikTok com timing preciso, cortes e textos sincronizados.**

Generate professional video production briefs with detailed frame-by-frame instructions for cuts, timing, on-screen text, transitions, and effects. Part of the modular Copy-Reels system.

## Overview

This skill provides deep production guidance for 30-60s viral Reels/TikTok videos focused on:

- **Production Table Format**: Time | Visual Description | Voiceover | On-Screen Text | Transition/Effect
- **Frame-by-Frame Timing**: Exact timing for zooms, cuts, fades, animations (0.2s-0.5s precision)
- **On-Screen Text Mastery**: Legibility rules, 48pt minimum, safe area margins, text layering (title + subtitle)
- **Visual Patterns**: 10+ validated production patterns (Zoom-In-Slow-Down, Cut-on-Beat, Micro-Gancho Visual, etc.)
- **Voiceover Sync**: Exact voiceover text paired with visual/text action at each second
- **Assets Checklist**: Video shots, audio specs, typography, color grading, captions
- **Quality Gates**: Production-specific checklist before export

## Usage

### 1. Basic Workflow

**Input**: Script (voiceover + timing) + visual direction  
**Output**: JSON production table → .docx document with timing table + assets + quality gates

### 2. JSON Structure

See `references/schema.md` for full field documentation. Basic outline:

```json
{
  "date": "2026-08-30",
  "metadata": {
    "titulo": "Seu vídeo",
    "tipo": "talking-head | tutorial | montage | motion-graphics",
    "duracao": "30s | 45s | 60s",
    "nivelProducao": "minimalista | amador | profissional"
  },
  "producaoTable": [
    {
      "timeRange": "0-1s",
      "visual": "Wide shot, rosto + ombros, iluminação frontal, fundo bokeh",
      "voiceover": "Exatamente o que é falado (copiar de script)",
      "onScreenText": "TITULO\nsubtítulo em cinza",
      "transicao": "Cut (nenhuma)"
    },
    {
      "timeRange": "1-3s",
      "visual": "Zoom in suave (0.3s), close-up do rosto, profundidade 0.5m",
      "voiceover": "Próxima frase da VO",
      "onScreenText": "NOVO TEXTO\nmais detalhes",
      "transicao": "Zoom (0.3s) — smooth"
    }
  ],
  "assetsNecessarios": {
    "video": ["Wide shot (30s)...", "Close-up (20s)..."],
    "audio": ["Voiceover: ...", "Bed music: ..."],
    "texto": ["Font: ...", "Cor: ..."],
    "outros": ["Captions: ...", "Color grade: ..."]
  },
  "qualityChecklist": {
    "syncVoiceVisual": true,
    "textLegivelMobile": true,
    "transicoesBreves": true,
    "efeitosDiscretos": true,
    "audioBalanced": true,
    "semArtifatos": true,
    "coresConsistentes": true,
    "durationCorreta": true,
    "audioExport128": true,
    "testedNoPhone": true
  },
  "notasEdicao": "Notas específicas de brand/edição"
}
```

### 3. Generate .docx

```bash
cd scripts/
npm install
node generate_docx.js ../sua-producao.json ../output-producao.docx
```

Output: Formatted Word document with production table, assets, quality checklist ready for editors/producers.

### 4. Example

See `references/example-production.json` for full worked example: "Atribuição Multi-Channel: O Pesadelo Real"

- Metadata: talking-head, 30s, profissional
- 8-row production table with exact timing, visual direction, voiceover sync, on-screen text, transitions
- Asset requirements: wide/close-up video, screen capture, motion graphics, audio specs, typography
- Quality checklist (all passing)
- Brand notes: estrategista de campo de batalha tone, no artificial effects

## Key Concepts

### 1. Production Table Format

**5 Critical Columns:**

| Column | Purpose | Example |
|--------|---------|---------|
| **Timing** | Exact seconds | "0-1s", "1-3s", "3-5s" |
| **Visual** | Shot type + movement + focus | "Wide shot, zoom in 0.3s, close-up rosto, bokeh background" |
| **Voiceover** | Exact script text | Copy voiceover from copy-reels-script |
| **On-Screen Text** | Title + subtitle with timing | "TITULO\nsubtítulo" (appears when?) |
| **Transition/Effect** | Type + duration + timing | "Fade (0.3s)", "Cut on beat", "Zoom (0.3s)" |

**Key rule**: Every second 0-30 must have at least one row (nothing should be "dead air").

### 2. On-Screen Text Mastery

**Legibility requirements (mobile-first):**
- Minimum 48pt for titles (tested on iPhone 6 @ 1m)
- Minimum 32pt for subtitles
- 16px safe area margin from edges
- **White (#FFFFFF) with black drop shadow 2px/40% opacity** for maximum contrast
- Subtitles in gray (#CCCCCC) @ 50% opacity (visual hierarchy)

**Text structure (two-line approach):**
```
PRIMARY TEXT (ALL CAPS if hook/urgency)
secondary text (lowercase, 50% opacity)
```

**Timing rules:**
- Text appears **before** voiceover mentions it (0.2s lead)
- Text disappears **after** voiceover finishes mentioning it (0.3s lag)
- Never overlap 2 on-screen text blocks
- On-screen text "breathes" — each block 1-2s minimum

### 3. Transition/Effect Precision

**Validated transition types:**

| Type | Duration | Use Case | Example |
|------|----------|----------|---------|
| **Cut** | 0s (instant) | Scene change, hard break | talking head → screen capture |
| **Fade** | 0.3s (standard) | Soft transition, emphasis pause | between concepts |
| **Zoom** | 0.3s (standard) | Dynamic close-up, intensity | wide → close-up |
| **Slide** | 0.2s | Side-to-side movement | scrolling effect |
| **Fade to Black** | 0.3-0.5s | Pause/emphasis moment | after key insight |

**Easing rule**: All transitions use ease-out (smooth deceleration), never linear or ease-in-out.

**On-beat rule**: When synced to trending audio, transitions trigger on beat/lyric drop (0.1s precision).

### 4. Visual Scene Descriptions (Shot Templates)

**Talking Head:**
```
Wide shot, rosto + ombros, iluminação frontal + keylight morno (3200K), background bokeh cinzento, câmera nível olho, sem movimento
```

**Close-Up (Detail):**
```
Close-up rosto, profundidade 0.5m da câmera, shallow DoF (f/2.8), foco nos olhos, iluminação soft + rim light subtil
```

**Screen Capture:**
```
Screen capture desktop/mobile, 1920x1080 mín, cores contrastantes, pointer branco (não amarelo), dados claros e legíveis
```

**Motion Graphics/Animation:**
```
Animação gráfica: 5 elementos move para centro em timing escalonado, efeito glow suave, background neutro, duração 6s total
```

**Required fields for every visual:**
- Tipo de shot (wide, close-up, screen, animation)
- Movimento (zoom in/out, pan, static, slow-mo, entrada/saída)
- Focus area (rosto, detalhe, full screen, elemento específico)
- Lighting/background context

### 5. Audio Specifications

**Voiceover:**
- Gravado em room tratado (foam acoustics, sem eco)
- 48kHz, 24-bit WAV, -3dB normalizador
- Sem pops, clicks, background noise

**Bed Music (Background):**
- Subtle electronic/ambient type
- Volume: 20% during talking, 30% during animations, fade out last 0.5s
- Rule: VO 70% / Music 30% (never inverted)
- Examples: Epidemic Sound, Artlist, royalty-free trending

**Sound Effects (optional):**
- Whoosh on Fade transitions (0.2s, low volume)
- Pop click on hard Cuts (OPTIONAL — only if brand uses)

### 6. Production Patterns (10+)

**Zoom-In-Slow-Down:**
- 0-1s: wide shot
- 1-2.5s: smooth zoom in 0.3s
- 2.5-3s: hold close-up (pause effect)
- Use: Drama, emphasis on face/detail

**Cut-on-Beat:**
- Scene transitions timed to audio beat/lyric drop
- 0.1s precision required
- Use: Montage, trending audio sync

**Micro-Gancho Visual (35s mark):**
- On 45-60s content, add visual "hook" at 35s
- Unexpected cut, animation, or POV shift
- Prevents dropout mid-content

**Fade-to-Black Pause:**
- Fade out scene to black 0.3s
- Hold black 0.5-1s (silent moment)
- Fade back in 0.3s
- Use: Emphasize key insight, reset attention

**Pointer/Arrow Direction:**
- White pointer (not yellow/neon) indicates data/focus area
- Enters frame 0.2s after voiceover mentions it
- Moves to next element on VO transition

**Staggered Text Stack:**
- Text line 1 appears at 0s
- Text line 2 appears +0.1s offset
- Subtitle appears +0.2s offset
- Creates layering effect (not overwhelming)

**Contrast Cut:**
- Sudden visual shift (wide → extreme close, color swap)
- 0s transition (hard cut)
- Use: Pattern interrupt, re-engagement

**Slow-Mo Emphasis:**
- 1-2 second segment plays at 0.8x speed
- Use: Highlight crucial gesture/moment
- Audio stays normal speed (just video slows)

**Consistent Framing:**
- Multiple clips maintain identical frame/composition
- Builds visual narrative coherence
- Example: talking head always frame 0.5m distance, f/2.8

**Edge Blur/Vignette:**
- 1-2% vignette on edges (subtle darkening)
- Draws attention inward to face/text
- Never more than 2% (looks artificial if excessive)

### 7. Asset Requirements Checklist

Before production starts:

**Video:**
- [ ] Wide shot (30s minimum, 1920x1080+)
- [ ] Close-up (20s minimum, shallow DoF)
- [ ] Screen capture (10s minimum, 1920x1080 native)
- [ ] Motion graphics template (if needed)

**Audio:**
- [ ] Voiceover 30s (room-treated, 48kHz, -3dB normalized)
- [ ] Bed music (subtle, royalty-free, 60+ seconds)
- [ ] Sound effects (if brand uses them)

**Text:**
- [ ] Font on-brand (Helvetica Neue example, or specify)
- [ ] Color palette finalized (white + gray for text)
- [ ] .srt subtitle file (if captions required)

**Post-Production:**
- [ ] Color grade (consistent 3200K, +5% contrast)
- [ ] No pixelation/freeze frames
- [ ] Tested on iPhone 11 Pro + Pixel 6 @ 1m distance

### 8. Quality Gates (10 Checks)

✅ **syncVoiceVisual**: VO + visual perfectly timed (voiceover starts, visual matches immediately)  
✅ **textLegivelMobile**: On-screen text legible at 6" phone screen @ 1m  
✅ **transicoesBreves**: No transition > 0.5s (max allowed)  
✅ **efeitosDiscretos**: Effects don't distract (zoom is smooth, not jarring)  
✅ **audioBalanced**: VO 70% / Music 30% ratio maintained  
✅ **semArtifatos**: No pixelation, freeze, or compression artifacts  
✅ **coresConsistentes**: Color grade uniform across clips (same 3200K temp)  
✅ **durationCorreta**: Final video exactly 30s (or specified duration)  
✅ **audioExport128**: Audio exported 128kbps stereo MP4  
✅ **testedNoPhone**: Watched on actual device (not just editor preview)

All 10 gates must pass before publication.

## Integration with Copy-Reels Script

This skill generates the **visual/production layer**. The companion skill `copy-reels-script` generates the **script/copywriting layer**.

**Workflow:**
1. Use copy-reels-script to write script (hook, voiceover, CTA)
2. Export script as JSON
3. Use copy-reels-producao to map visual/timing to each second of script
4. Combine outputs into integrated production brief

**Output table format:**
```
Time | Visual | Voiceover | On-Screen Text | Transition
0-1s | Wide shot... | "Hook text..." | TITULO | Cut
1-3s | Zoom in... | "Setup text..." | SUBTITLE | Zoom (0.3s)
... (and so on)
```

This combined table becomes the **single source of truth** for editors/producers.

## Research & Confidence

All guidance backed by 20+ validated sources (2026):

- Short-form video production & editing (8 sources)
- Text overlay & on-screen typography (5 sources)
- Camera techniques & framing (4 sources)
- Trending audio & music integration (3 sources)

See `references/sources.md` for full bibliography and validation methodology.

## Files

```
copy-reels-producao/
├── SKILL.md                          # Full production instruction manual (8,000+ words)
├── README.md                         # This file
├── references/
│   ├── schema.md                     # JSON schema documentation
│   ├── sources.md                    # 20+ validated sources
│   └── example-production.json       # Worked example (Atribuição Multi-Channel)
└── scripts/
    ├── package.json                  # Node dependencies (docx ^8.5.0)
    └── generate_docx.js              # JSON → .docx converter
```

## Workflow Example

**Step 1: Generate script (copy-reels-script)**
```bash
cd copy-reels-script/scripts/
node generate_docx.js ../references/example-script.json ../output-script.docx
```

**Step 2: Generate production (copy-reels-producao)**
```bash
cd copy-reels-producao/scripts/
node generate_docx.js ../references/example-production.json ../output-producao.docx
```

**Step 3: Share both documents**
- `output-script.docx`: Copywriter/creative team reviews hook/CTA/tone
- `output-producao.docx`: Producer/editor reviews timing/shots/effects

**Step 4: Combine into production brief**
Merge both outputs into single table format for final shoot brief.

---

_Copy-Reels Producao Skill v1.0 — 2026-08-30_
