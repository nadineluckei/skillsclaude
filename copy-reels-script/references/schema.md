# JSON Schema — Copy-Reels Script

Quando gerar roteiros em JSON, estruture assim:

```json
{
  "date": "2026-08-30",
  "metadata": {
    "objetivo": "awareness | consideração | conversão | engajamento",
    "publico": "descrição específica do público-alvo",
    "plataforma": "TikTok | Reels | ambas",
    "duracao": "30s | 45s | 60s",
    "tom": "provocador | educador | storyteller | humorista"
  },
  "roteiroPrincipal": {
    "titulo": "Título descritivo do roteiro",
    "hook": {
      "texto": "Uma frase que faz parar o scroll",
      "padrao": "Identity Call | Contrarian Strike | Open Loop | etc",
      "timing": "0-3s",
      "confianca": "high"
    },
    "setup": {
      "texto": "Expõe o problema ou contexto",
      "timing": "3-8s"
    },
    "solucao": {
      "texto": "Mostra exatamente como funciona",
      "timing": "8-20s"
    },
    "benefit": {
      "texto": "Por que isso importa",
      "timing": "20-27s"
    },
    "cta": {
      "texto": "Ação específica",
      "tipo": "soft | hard",
      "timing": "27-30s"
    }
  },
  "hookVariations": [
    {
      "variacao": 1,
      "padrao": "Identity Call",
      "texto": "Se você é [identidade específica]...",
      "confianca": "high"
    },
    {
      "variacao": 2,
      "padrao": "Contrarian Strike",
      "texto": "Todo mundo diz [crença comum]. A verdade é [contrário].",
      "confianca": "high"
    },
    {
      "variacao": 3,
      "padrao": "Results First",
      "texto": "Fui de [X] pra [Y]. Aqui está como...",
      "confianca": "high"
    }
  ],
  "ctaVariants": [
    {
      "cta": 1,
      "texto": "Salva esse vídeo",
      "tipo": "soft"
    },
    {
      "cta": 2,
      "texto": "Comenta se você concorda",
      "tipo": "soft"
    },
    {
      "cta": 3,
      "texto": "Clica no link (bio)",
      "tipo": "hard"
    }
  ],
  "testingNotes": {
    "metricaPrincipal": "3-second retention",
    "duracao": "3-5 dias por hook",
    "benchmark": "70%+ retention @ 3s",
    "nextSteps": "Substituir hook se benchmark não atingido"
  },
  "qualityChecks": {
    "hookPor3s": true,
    "silentTest": true,
    "autenticoTom": true,
    "aiSlops": false,
    "ctaEspecifico": true,
    "batchVariations": true,
    "testedMindset": true
  }
}
```

---

## Campo por Campo

### Top Level

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|------------|-----------|
| `date` | string (YYYY-MM-DD) | Não | Data da geração. Omita pra usar data atual. |
| `metadata` | object | Sim | Contexto do roteiro. |
| `roteiroPrincipal` | object | Sim | Roteiro principal estruturado. |
| `hookVariations` | array | Não | 3-5 variações de hook pra A/B test. |
| `ctaVariants` | array | Não | 3-4 CTAs alternativas. |
| `testingNotes` | object | Recomendado | Notas de testing. |
| `qualityChecks` | object | Recomendado | Checklist de qualidade. |

### Metadata

```json
{
  "objetivo": "awareness | consideração | conversão | engajamento",
  "publico": "Head de marketing em SaaS B2B série A-C (ex de específico)",
  "plataforma": "TikTok | Reels | ambas",
  "duracao": "30s | 45s | 60s",
  "tom": "provocador | educador | storyteller | humorista"
}
```

### Roteiro Principal (Estrutura 30s)

```json
{
  "titulo": "string",
  "hook": {
    "texto": "string (máx 1 frase)",
    "padrao": "Identity Call | Contrarian Strike | Open Loop | Confession | Results First | Mistake Warning | List Tease | Direct Question | POV/Relatable",
    "timing": "0-3s",
    "confianca": "high | medium | low"
  },
  "setup": {
    "texto": "string (1-2 frases)",
    "timing": "3-8s"
  },
  "solucao": {
    "texto": "string (ação ou insight claro)",
    "timing": "8-20s"
  },
  "benefit": {
    "texto": "string (transformação, economia, valor)",
    "timing": "20-27s"
  },
  "cta": {
    "texto": "string (específica, não genérica)",
    "tipo": "soft | hard",
    "timing": "27-30s"
  }
}
```

### Hook Variations

```json
{
  "variacao": 1,
  "padrao": "Identity Call | Contrarian Strike | Open Loop | ...",
  "texto": "string (hook completo)",
  "confianca": "high | medium | low"
}
```

**Confiança Scoring:**
- `high`: Padrão validado 3+ fontes, proven performer
- `medium`: Padrão funciona mas saturado no mercado
- `low`: Novo padrão, needs validation

### CTA Variants

```json
{
  "cta": 1,
  "texto": "string (1-3 palavras)",
  "tipo": "soft | hard",
  "notaDeUso": "Use em educational content" (opcional)
}
```

### Testing Notes

```json
{
  "metricaPrincipal": "3-second retention",
  "duracao": "3-5 dias",
  "benchmark": "70%+ retention @ 3s = hook funciona",
  "nextSteps": "Se benchmark não atingido, replace hook"
}
```

### Quality Checks

```json
{
  "hookPor3s": true,              // Hook entrega premissa?
  "silentTest": true,             // Funciona sem som?
  "autenticoTom": true,           // Não forçado?
  "aiSlops": false,               // Sem padding words?
  "ctaEspecifico": true,          // Não genérica?
  "batchVariations": true,        // 3-5 hooks?
  "testedMindset": true           // Não "é o único jeito"?
}
```

---

## Exemplo Mínimo

Se só quer roteiro principal + 1 hook alternative:

```json
{
  "metadata": {
    "objetivo": "conversão",
    "publico": "CMOs em empresa 20-500 pessoas",
    "plataforma": "Reels",
    "duracao": "30s"
  },
  "roteiroPrincipal": {
    "titulo": "Atribuição Multi-Channel",
    "hook": {
      "texto": "71% dos CMOs dizem que atribuição é adivinhação. Vou te mostrar por quê.",
      "padrao": "Results First",
      "timing": "0-3s"
    },
    "setup": { "texto": "Seu CEO exige 'de onde saiu esse lead?' — e você não sabe." },
    "solucao": { "texto": "Porque 5 touchpoints acontecem antes da compra." },
    "benefit": { "texto": "Medir real = investir em canais certos." },
    "cta": { "texto": "Salva pra depois", "tipo": "soft" }
  }
}
```

---

## Como Usar

1. Estruture seu roteiro neste JSON
2. Salve como `script.json`
3. Rode o script de geração:
   ```bash
   cd scripts/
   npm install  # (primeira vez só)
   node generate_docx.js ../script.json ../output.docx
   ```
4. Arquivo `.docx` pronto!

---

## Validações

O script não valida campos — se omitir obrigatório, a seção fica vazia ou quebrada. Sempre preencha:
- `metadata`
- `roteiroPrincipal`
- Pelo menos 3 `hookVariations` para testing
- `testingNotes` (essencial pra qualidade)
