# JSON Schema — Copy-Reels Producao

Quando gerar instruções de produção em JSON, estruture assim:

```json
{
  "date": "2026-08-30",
  "metadata": {
    "titulo": "Título do roteiro",
    "tipo": "talking-head | tutorial | montage | motion-graphics",
    "duracao": "30s | 45s | 60s",
    "nivelProducao": "minimalista | amador | profissional"
  },
  "producaoTable": [
    {
      "timeRange": "0-1s",
      "visual": "Descrição da cena visual",
      "voiceover": "Texto do voiceover",
      "onScreenText": "TITULO TEXTO",
      "transicao": "Tipo e duração"
    },
    {
      "timeRange": "1-3s",
      "visual": "Descrição visual",
      "voiceover": "Continuação",
      "onScreenText": "Subtítulo em cinza",
      "transicao": "Zoom (0.3s)"
    }
  ],
  "assetsNecessarios": {
    "video": ["Wide shot", "Close-up", "Screen capture"],
    "audio": ["Voiceover clean", "Bed music (trending)", "Efeitos sonoros (opcional)"],
    "texto": ["Font on-brand", "Cor contrastante", "Tamanho testado em mobile"],
    "outros": ["Captions .srt (opcional)", "Color grade consistent"]
  },
  "qualityChecklist": {
    "syncVoiceVisual": true,
    "textLegivelMobile": true,
    "transicoesBreves": true,
    "efeitos Discretos": true,
    "audioBalanced": true,
    "semArtifatos": true,
    "coresConsistentes": true,
    "durationCorreta": true,
    "audioExport128": true,
    "testedNoPhone": true
  },
  "notasEdicao": "Instruções adicionais específicas do projeto"
}
```

---

## Campo por Campo

### Top Level

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|------------|-----------|
| `date` | string | Não | Data geração. |
| `metadata` | object | Sim | Contexto de produção. |
| `producaoTable` | array | Sim | Tabela timing/visual/audio/text. |
| `assetsNecessarios` | object | Recomendado | O que precisa capturar/criar. |
| `qualityChecklist` | object | Recomendado | Gate de qualidade. |
| `notasEdicao` | string | Não | Notas específicas do projeto. |

### Metadata

```json
{
  "titulo": "string",
  "tipo": "talking-head | tutorial | montage | motion-graphics",
  "duracao": "30s | 45s | 60s",
  "nivelProducao": "minimalista | amador | profissional"
}
```

### Production Table Row

```json
{
  "timeRange": "0-1s | 1-3s | 3-8s | etc",
  "visual": "Descrição detalhada da cena (ângulo, zoom, etc)",
  "voiceover": "Exatamente o que é falado (copiar de script)",
  "onScreenText": "TITULO (ALL CAPS) ou Subtítulo (lowercase)",
  "transicao": "Cut | Fade (0.3s) | Zoom (0.3s) | Slide (0.2s)"
}
```

**Visual Description Template:**
- Tipo de shot (wide, close-up, screen capture, animação)
- Movimento (zoom in, pan, static, slow-mo)
- Focus area (rosto, detalhe, full screen)
- Background/context

**On-Screen Text Template:**
- Primeira linha: Frase principal (ALL CAPS se urgência/hook)
- Segunda linha: Sub-text (lowercase, 50% opacity, gray)
- Timing: Quando aparece, quando desaparece (cover na timeRange)

**Transition Template:**
- Type (Cut, Fade, Zoom, Slide, On-Beat)
- Duration (0.2s, 0.3s, 0.5s — máx)
- If audio-sync: "Cut on beat" ou "Fade on lyric"

### Assets Necessarios

```json
{
  "video": [
    "Wide shot of [descrição]",
    "Close-up [descrição]",
    "Screen capture [descrição]"
  ],
  "audio": [
    "Voiceover clean (gravado em room tratado)",
    "Bed music: [trending sound name ou original]",
    "Efeitos sonoros: [lista de efeitos necessários]"
  ],
  "texto": [
    "Font: [on-brand font name ou sistema]",
    "Cor: [white/black com contraste high]",
    "Tamanho: [testado em phone 6 polegadas]"
  ],
  "outros": [
    "Captions .srt: [sim/não]",
    "Color grade: [consistent | match between clips]",
    "Vignette/edge blur: [sim/não]"
  ]
}
```

### Quality Checklist

```json
{
  "syncVoiceVisual": true,           // Voiceover + visual sincronizado
  "textLegivelMobile": true,         // Text legível em phone 6"
  "transicoesBreves": true,          // Nenhuma > 0.5s
  "efeitosDiscretos": true,          // Não saturado
  "audioBalanced": true,             // VO 70%, música 30%
  "semArtifatos": true,              // Sem pixelação/freeze
  "coresConsistentes": true,         // Color grade uniforme
  "durationCorreta": true,           // Timing exato conforme plan
  "audioExport128": true,            // 128kbps stereo MP4
  "testedNoPhone": true              // Testado em device real
}
```

---

## Exemplo Mínimo

Roteiro de 30s, talking head simples:

```json
{
  "metadata": {
    "titulo": "Atribuição Multi-Channel",
    "tipo": "talking-head",
    "duracao": "30s",
    "nivelProducao": "amador"
  },
  "producaoTable": [
    {
      "timeRange": "0-1s",
      "visual": "Wide shot, face + shoulders, iluminação frontal",
      "voiceover": "71% dos CMOs dizem que atribuição é adivinhação.",
      "onScreenText": "71% DOS CMOS",
      "transicao": "Cut (nenhuma)"
    },
    {
      "timeRange": "1-3s",
      "visual": "Zoom suave in pra close-up (0.3s), mantém por 1.7s",
      "voiceover": "Vou te mostrar por quê.",
      "onScreenText": "ASSISTA ATÉ FIM",
      "transicao": "Zoom (0.3s)"
    },
    {
      "timeRange": "3-8s",
      "visual": "Fade pra screen capture de CRM, pointer em dados",
      "voiceover": "Seu CEO exige: 'De onde saiu esse lead?'",
      "onScreenText": "PROBLEMA: 5 touchpoints",
      "transicao": "Fade (0.3s)"
    },
    {
      "timeRange": "20-27s",
      "visual": "Back to close-up, mantém framing",
      "voiceover": "Medir real = investir em canais certos.",
      "onScreenText": "SOLUÇÃO: dados integrados",
      "transicao": "Cut"
    },
    {
      "timeRange": "27-30s",
      "visual": "Zoom out leve, fade final",
      "voiceover": "Salva esse — próximo post explico.",
      "onScreenText": "SALVA ESSE",
      "transicao": "Fade (0.5s)"
    }
  ],
  "assetsNecessarios": {
    "video": [
      "Wide shot (30s) — face + shoulders, room bem iluminado",
      "Close-up (20s) — rosto, profundidade 0.5m da câmera",
      "Screen capture (10s) — CRM dashboard ou planilha"
    ],
    "audio": [
      "Voiceover: 30s gravado em room tratado (sem eco)",
      "Bed music: Subtle background track (low volume, 20%)",
      "Efeitos: Nenhum necessário"
    ],
    "texto": [
      "Font: Helvetica Neue bold (on-brand)",
      "Cor: Branco com sombra preta leve (contraste alto)",
      "Tamanho: 48pt (testado legível em iPhone 6)"
    ],
    "outros": [
      "Captions: Não necessário",
      "Color grade: Consistente, bem iluminado",
      "Vignette: Leve (1% edge blur) para focar rosto"
    ]
  }
}
```

---

## Como Usar

1. Estruture tabela de produção neste JSON
2. Salve como `producao.json`
3. Rode gerador (mesmo script que copy-reels-script):
   ```bash
   node generate_docx.js ../producao.json ../output-producao.docx
   ```
4. Passa pra producer/editor com tabela + assets list

---

## Notas

- O schema é flexível — adapte conforme projeto
- Coluna `visual` é descritiva (producer/editor interpreta)
- Coluna `transicao` é específica (duração exata, tipo)
- `assetsNecessarios` é checklist pra antes de começar edição
- `qualityChecklist` é gate antes de export final
