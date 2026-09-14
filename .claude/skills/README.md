# Content Production Pipeline Skills

5 specialized skills para orquestrar o pipeline completo de planejamento de conteúdo (pesquisa → planejamento → vídeo → blog → reels).

## 🎬 Arquitetura

```
/pesquisador-conteudo
  ↓ [Aprova temas no Gmail]
/planejador-conteudo
  ↓ [Aprova plano no Gmail]
/roteirista-video
  ↓ [Aprova roteiros no Gmail]
/redator-conteudo
  ↓
/orquestrador-conteudo (coordena tudo)
```

## 📋 Skills disponíveis

### 1. `/pesquisador-conteudo` — Fase 1.1
Pesquisa temas em alta em fontes confiáveis (MIT, McKinsey, Deloitte, HBR, Gartner, WEF).
- **Input**: Briefing mínimo (público, canal, trimestre, cadência)
- **Output**: Lista de 10-15 temas com fonte e ângulo estratégico
- **Aprovação**: Gmail

### 2. `/planejador-conteudo` — Fase 1.2
Cria planejamento trimestral com eixos temáticos e pautas estruturadas.
- **Input**: Temas aprovados + briefing
- **Output**: Documento .docx com planejamento completo
- **Aprovação**: Gmail

### 3. `/roteirista-video` — Fase 3
Cria roteiros de vídeo YouTube + cortes automáticos para Reels Instagram.
- **Input**: Pautas aprovadas do planejamento
- **Output**: Roteiros com timings + headlines para 2-5 Reels por vídeo
- **Aprovação**: Gmail (ANTES do blog ser redigido)

### 4. `/redator-conteudo` — Fase 2
Redige blog posts completos com SEO/GEO, usando roteiros de vídeo como base.
- **Input**: Pautas + roteiros de vídeo aprovados
- **Output**: Artigos de blog prontos para publicar
- **Aprovação**: Não formal

### 5. `/orquestrador-conteudo`
Coordena todo o pipeline, monitora Gmail para aprovações, passa automaticamente entre fases.
- **Input**: Comando inicial `/orquestrador-conteudo`
- **Process**: Chama cada skill em ordem, aguarda aprovações
- **Output**: Pipeline completo executado

## 🚀 Como usar em outro chat

### Opção A: Orquestração automática (recomendado)
```
/orquestrador-conteudo
```
A skill faz tudo sozinha: pesquisa → planejamento → vídeo → blog

### Opção B: Chamar skills individuais
Se você quiser controlar passo a passo:
```
/pesquisador-conteudo
```
Depois de aprovado os temas:
```
/planejador-conteudo
```
E assim por diante.

## 📧 Aprovações via Gmail

- **Fase 1.1 (Temas)**: Responda "aprova" ou "aprova com ajustes"
- **Fase 1.2 (Planejamento)**: Responda o e-mail com aprovação
- **Fase 3 (Roteiros)**: Responda aprovando os roteiros
- **Fase 2 (Blog)**: Sem gate de aprovação — redige automaticamente

## 📊 Estratégia central

Todos os temas/pautas/conteúdos tocam nos **3 inimigos em comum** da marca:

1. **Ditadura das receitas prontas** — não existem fórmulas genéricas que funcionem
2. **Miopia operacional / ilusão da tecnologia** — tecnologia sozinha não resolve nada
3. **Padronização que apaga identidade** — mercado tenta encaixar todos em moldes genéricos

## 🎥 Produção integrada

Uma produção de vídeo YouTube gera:
- **1 roteiro completo** (6-8 minutos)
- **2-5 Reels Instagram** (cortes temáticos do vídeo)
- **1 artigo de blog** (baseado no roteiro + otimizado para SEO)

Total: 4 vídeos/mês = 12 artigos/trimestre + 24 Reels/trimestre

## 🛠 Assets compartilhados

Todas as skills usam:
- `assets/brand-profile.md` — Perfil de marca Nadine Luckei
- `references/` — Guias de escrita, pesquisa, SEO, anti-slop
- `references/example-plan.json` — Exemplo de planejamento completo

## ✏️ Contato

Marca: **Nadine Luckei** (RevOps, Estratégia de Vendas/Marketing)
E-mail para aprovações: `luckeitolotti@gmail.com`
