# Plan JSON schema

This is the input contract for `scripts/generate_docx.js`. Build one JSON object
with this shape, save it to a file, then run:

```bash
node scripts/generate_docx.js plan.json output.docx
```

## Top level

| Field | Type | Notes |
|---|---|---|
| `title` | string | Main document title, e.g. `"PLANEJAMENTO ESTRATÉGICO DE CONTEÚDO"` |
| `subtitle` | string | Optional, shown centered/italic under the title, e.g. the quarter and year |
| `channel` | string | Optional, one more centered/italic line (blog name, channel, publication) |
| `labels` | object | Optional. Overrides the field labels used inside every pauta (see below). Defaults are Portuguese; pass your own for another language. |
| `sections_before_months` | array of Section | Intro material — overview, audience, structure of the quarter. Rendered in order before the months. |
| `months` | array of Month | The core of the plan — one entry per month in the quarter. |
| `closing_sections` | array of Section | Wrap-up material — the quarter's throughline and a summary. Rendered in order after the months. |

`labels` keys and their defaults:

```json
{
  "type": "Tipo:",
  "direcionamento": "Direcionamento:",
  "central_question": "Pergunta central:",
  "structure": "Estrutura esperada:",
  "sources": "Fontes:",
  "keywords": "Palavras-chave:",
  "tone": "Tom:"
}
```

## Section (used by `sections_before_months` and `closing_sections`)

A generic, freeform block — use it for anything that isn't a month/pauta.

| Field | Type | Notes |
|---|---|---|
| `heading` | string \| null | Omit or set null for a section that continues the previous heading (e.g. a summary list with no heading of its own) |
| `level` | 1 \| 2 | Heading weight. 1 = top-level section (e.g. `VISÃO GERAL`), 2 = sub-section (e.g. `PÚBLICO`, `Narrativa Conectada:`) |
| `paragraphs` | array of string | Plain paragraphs, rendered in order |
| `bullets` | array of string | Bullet list, rendered after the paragraphs |

A section can mix `paragraphs` and `bullets`; both are optional.

## Month

| Field | Type | Notes |
|---|---|---|
| `label` | string | e.g. `"OUTUBRO / 2026"` |
| `axis_title` | string | e.g. `"EIXO TEMÁTICO: Liderança e Decisão"` — the month's thematic axis |
| `axis_description` | string | 1-2 sentences on what this axis covers and why it's now, in the arc |
| `pautas` | array of Pauta | The content pieces for the month (the reference plan used 3 per month) |

## Pauta (one piece of content)

This is the fixed, repeatable unit — every pauta in the document uses exactly
these fields, which is what makes the plan scannable and comparable across
the whole quarter.

| Field | Type | Notes |
|---|---|---|
| `number` | number | 1, 2, 3... within the month |
| `title` | string | The provocative headline/thesis-as-title, usually a quoted line |
| `type` | string | Two content pillars combined, e.g. `"Liderança + Responsabilidade"` |
| `direcionamento` | array of `{label, text}` | The strategic reasoning behind the piece. The reference plan always used exactly these four, in this order: `Narrativa comum` (the received wisdom), `Realidade` (what's actually true), `Ângulo` (the specific take), `Tese` (the one-line claim the article defends) |
| `central_question` | string | The single question the piece answers — sharp enough to hook a reader in the target audience |
| `structure` | array of string | ~5 bullets sketching the piece's outline, in the order a writer would draft it |
| `sources` | array of `{title, publication, year?, url}` | Optional. Real citations backing the `Realidade` claim — see `references/research.md` for how to find them. Rendered as clickable hyperlinks. Omit the field (don't invent entries) when no credible source was found for that pauta. |
| `keywords` | string | Comma-separated SEO/topic keywords |
| `tone` | string | 1-2 sentences describing the register (e.g. "Incisivo. Responsabiliza o líder pelo fracasso, não o time.") |

See `references/example-plan.json` for a complete worked example (a
transcription of the reference plan this skill was modeled on, in
Portuguese, using the default labels). See `references/example-plan-en.json`
for the same shape in English, with `labels` overridden — the `labels`
defaults are Portuguese, so any non-Portuguese plan must override them or
the rendered document ends up with Portuguese field labels mixed into
another language.
