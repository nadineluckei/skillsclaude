# JSON Schema — Pesquisador-Temas

Quando gerar o .docx, estruture os dados assim:

```json
{
  "date": "2026-08-30",
  "rapidThemes": [
    {
      "title": "OpenAI anuncia novo modelo com custos 70% menores",
      "why": "Empresa quer democratizar acesso a IA; competição com Anthropic e Google; mercado busca reduzir custos de operação",
      "socialAngle": "Enquanto isso, seu concorrente já tá usando IA por 1/3 do preço que você paga",
      "source": "OpenAI Blog, 30 ago 2026"
    },
    {
      "title": "Startups de IA para vendas explodem em Product Hunt",
      "why": "Pain point real: equipes de vendas sobrecarregadas; IA pode automatizar follow-ups; demanda de eficiência",
      "socialAngle": "A IA tá automatizando o trabalho mais chato dos vendedores (e eles não reclamam)",
      "source": "Product Hunt Top 10, última semana"
    }
  ],
  "painPoints": [
    {
      "pain": "Execução falha em projetos de transformação digital",
      "data": "McKinsey 2024-2025: 60% dos projetos de transformação digital não atingem ROI esperado",
      "why": "Pressão por resultados rápidos; falta de talent skills em implementação; silagem de dados",
      "whoAffected": "CMOs, CTOs, COOs, CFOs",
      "source": "McKinsey 'Digital Transformation Survey 2025'"
    },
    {
      "pain": "Ceticismo com IA por falta de ROI claro",
      "data": "Gartner 2025: 74% dos líderes de marketing têm dúvida se investimento em IA compensa",
      "why": "Muitos pilotos de IA não viraram negócio real; pressão acionária por justificativa de gasto; falta de métrica clara",
      "whoAffected": "CMOs, CFOs, Board members",
      "source": "Gartner 'State of Marketing 2025'"
    },
    {
      "pain": "Silagem de dados entre marketing, vendas e operações",
      "data": "HBR 2025: 68% das empresas não conseguem usar dados entre departamentos de forma integrada",
      "why": "Cada área tem seu próprio stack de ferramentas; falta de governança de dados; desalinhamento de KPIs",
      "whoAffected": "CDOs, CTOs, heads de marketing e vendas",
      "source": "Harvard Business Review 'Data Silos Kill Strategy'"
    }
  ],
  "risingThemes": [
    {
      "theme": "Product-Led Growth (PLG) consolidando em B2B Enterprise",
      "definition": "Estratégia onde o produto é o principal driver de aquisição e expansão, reduzindo dependência de vendas consultivas. Auto-serve demo, freemium convertendo, usuário final usa sem aprovação de procurement.",
      "why": "Venda consultiva explodiu em custo; corporates querem velocidade; Gen Z preferem self-serve; IA torna PLG mais viável (copilots dentro do produto)",
      "whereHot": "SaaS B2B; especialmente startups Series A-C expandindo pra enterprise; ferramentas dev-first",
      "next6Months": "Integração de IA agents dentro do produto de PLG (recomendações, automação de workflows); métricas de PLG consolidando (PQLs vs SQLs); PLG em verticais mais tradicionais",
      "source": "Pavilion 'The Future of Sales', SaaStr 2025, LinkedIn trending posts de Lenny Rachitsky"
    },
    {
      "theme": "IA como agente autônomo nas operações (não só insight)",
      "definition": "Modelos de IA que transcendem 'gerar dados' e passam a executar ações independentemente: agendar follow-ups, priorizar leads, atualizar registros no CRM, sugerir estratégia. Diferente de IA generativa pura (ChatGPT) — é IA que age.",
      "why": "2024-2025 foram de 'IA gera insights'; market agora é 'IA executa'; pressão por automação de trabalho repetitivo; LLMs + tools integration ficou maduro; empresas querem ROI não insights",
      "whereHot": "Enterprise, SaaS B2B, áreas de ops/RevOps/marketing/vendas; especialmente em processos repetitivos",
      "next6Months": "Regulação sobre 'IA autônoma' e responsabilidade; melhor integração com CRMs (Salesforce AI Cloud, HubSpot ops); benchmarks de ROI de IA agent; preocupações de hallucination/confiança",
      "source": "McKinsey 'Agentic AI', HBR 'The Rise of Autonomous AI', Gartner 'AI Autonomy Maturity'"
    },
    {
      "theme": "Composable Architecture e no-code/low-code para marketing ops",
      "definition": "Em vez de 'platform único' (Salesforce, HubSpot), empresas montam seu próprio stack de tools microserviços. No-code/low-code permite marketing teams construir integrações e automações sem dev skills.",
      "why": "Plataformas monolíticas custam caro e demoram a adaptar; empresas querem flexibilidade; ferramenta de automação ficaram mais acessíveis; dados fragmentados precisam ser conectados",
      "whereHot": "Mid-market pra enterprise; marketing ops teams; especialmente orgs com budget pra customização",
      "next6Months": "IA para gerar código em no-code tools (ex: 'descreva o fluxo e IA cria a automação'); standartização de conectores; consolidação de players no espaço (alguns vão comprar outros)",
      "source": "Forrester 'The Composable Stack', Gartner 'Magic Quadrant Low-Code Platforms 2025', HashiCorp State of Infrastructure"
    }
  ],
  "executiveSummary": "Mercado de 2025 é de execução sobre insight: IA não é mais 'gerar ideias melhor', é 'executar operações melhor'. Dores mais profundas estão em transformação digital falhando (60% sem ROI), ceticismo com IA por falta de métrica clara (74% duvidoso), e silagem de dados travando decisão. Temas em alta que abrem oportunidade: PLG ganhando em enterprise (reduz custo de aquisição), IA agent autônoma operando de verdade (não só consultoria), e arquitetura composta de tools (vs monolítica). Quem priorizar essas três frentes nos próximos 6 meses tira vantagem."
}
```

## Campo por Campo

### Top Level

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|------------|-----------|
| `date` | string (YYYY-MM-DD) | Não | Data da pesquisa. Omita pra usar data atual. |
| `rapidThemes` | array | Não | Lista de temas rápidos (ver abaixo). Omita se só quer robustos. |
| `painPoints` | array | Não | Lista de dores específicas (ver abaixo). Omita se não tem. |
| `risingThemes` | array | Não | Lista de temas em alta (ver abaixo). Omita se não tem. |
| `executiveSummary` | string | Não | 3-4 frases de insight final. Omita e o script não inclui a seção. |

### Temas Rápidos (`rapidThemes`)

```json
{
  "title": "string (máx 1 frase)",
  "why": "string (1-2 frases, contexto de por que tá em alta)",
  "socialAngle": "string (frase de gancho pronta pra social, diferente do title)",
  "source": "string (onde viu, idealmente com data)"
}
```

### Dores Específicas (`painPoints`)

```json
{
  "pain": "string (nome da dor, curto e específico)",
  "data": "string (citação/estatística + fonte, ex: 'McKinsey 2025: 60% dos...')",
  "why": "string (contexto de por que é dor AGORA)",
  "whoAffected": "string (cargos/funções afetadas)",
  "source": "string (consultoria + data, ex: 'McKinsey State of Org 2025')"
}
```

### Temas em Alta (`risingThemes`)

```json
{
  "theme": "string (nome do tema)",
  "definition": "string (1-2 frases explicando oq é, pra quem não conhece)",
  "why": "string (por que virou trend agora)",
  "whereHot": "string (segmentos/áreas onde está em alta)",
  "next6Months": "string (evolução esperada do tema)",
  "source": "string (publicações/analistas que reportam)"
}
```

## Exemplo Mínimo

Se só quer Temas Rápidos:

```json
{
  "rapidThemes": [
    {
      "title": "OpenAI anuncia novo modelo",
      "why": "Redução de custos",
      "socialAngle": "Seu concorrente já tá usando",
      "source": "OpenAI Blog, 30 ago"
    }
  ]
}
```

Se só quer Dores:

```json
{
  "painPoints": [
    {
      "pain": "Execução falha",
      "data": "McKinsey: 60% sem ROI",
      "why": "Pressão por velocidade",
      "whoAffected": "CTOs",
      "source": "McKinsey 2025"
    }
  ]
}
```

## Como Usar

1. Estruture sua pesquisa neste JSON
2. Salve como `research.json`
3. Rode:
   ```bash
   cd scripts/
   npm install  # (primeira vez só)
   node generate_docx.js ../research.json ../output.docx
   ```
4. Arquivo `.docx` pronto!

## Validações

O script não valida campos — se omitir um campo obrigatório, a seção sai vazia ou quebrada. Sempre preencha os campos do schema.
