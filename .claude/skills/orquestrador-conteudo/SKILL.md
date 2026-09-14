---
name: orquestrador-conteudo
description: Coordena o pipeline completo de planejamento de conteúdo (pesquisa → planejamento → redação → vídeo), chamando cada skill em sequência e monitorando o Gmail para aprovações em cada etapa. Aguarda confirmação explícita antes de passar para a próxima fase.
---

# Orquestrador de Conteúdo

## Visão geral

Esta skill **coordena todo o pipeline** de planejamento de conteúdo do zero ao fim:

1. **Fase 1.1** — `pesquisador-conteudo`: Pesquisa temas
2. **Fase 1.2** — `planejador-conteudo`: Planejamento trimestral
3. **Fase 2** — `redator-conteudo`: Blog posts
4. **Fase 3** — `roteirista-video`: Roteiros de vídeo/Reels (opcional)

A orquestradora **monitora o Gmail** para aprovações em cada etapa, **aguarda confirmação explícita**, e só passa para a próxima fase quando o usuário confirma (respondendo o e-mail de aprovação).

## Como funciona

### Inicialização

Você confirma o **briefing mínimo** uma só vez:

- Público-alvo (já no brand-profile)
- Canais (Reels Instagram, Blog, YouTube)
- Trimestre/período
- Quantas peças por mês
- Restrições

### Fluxo automático

```
[INÍCIO]
  ↓
┌─────────────────────────────────┐
│ Fase 1.1: Pesquisa (pesquisador)│
├─────────────────────────────────┤
│ Pesquisa temas em fontes        │
│ → Envia lista para Gmail        │
│ → AGUARDA aprovação             │
└─────────────────────────────────┘
  ↓ [Aprova no Gmail]
┌─────────────────────────────────┐
│ Fase 1.2: Planejamento (planejador)
├─────────────────────────────────┤
│ Cria plano trimestral .docx     │
│ → Envia .docx para Gmail        │
│ → AGUARDA aprovação             │
└─────────────────────────────────┘
  ↓ [Aprova no Gmail]
┌─────────────────────────────────┐
│ Fase 2: Redação (redator)       │
├─────────────────────────────────┤
│ Redige blog posts               │
│ → Entrega posts (não precisa    │
│   aprovação formal)             │
└─────────────────────────────────┘
  ↓ [Opcional: quer vídeos?]
┌─────────────────────────────────┐
│ Fase 3: Vídeo (roteirista)      │
├─────────────────────────────────┤
│ Cria roteiros YouTube + Reels   │
│ → Entrega roteiros              │
└─────────────────────────────────┘
  ↓
[FIM]
```

## Detalhes técnicos

### Gates de aprovação via Gmail

A orquestradora faz isto **automaticamente**:

1. **Fase 1.1 completa**: Manda lista de temas para `luckeitolotti@gmail.com` com assunto
   ```
   "Temas sugeridos para o trimestre — para aprovação"
   ```

2. **Aguarda resposta no Gmail** — monitora a thread
   - Se responde com "aprova" / "ok" / thumbs-up → passa para Fase 1.2
   - Se responde pedindo ajustes → volta ao pesquisador para refinar
   - **Nunca presume aprovação** por silêncio

3. **Fase 1.2 completa**: Manda .docx do planejamento com assunto
   ```
   "Planejamento trimestral de conteúdo — [período] — para aprovação"
   ```

4. **Aguarda resposta no Gmail** — similar a cima

5. **Fase 2 (Redação)**: Não precisa gate formal
   - Redige conforme demanda do usuário (quais pautas quer redigidas agora)
   - Entrega posts prontos

6. **Fase 3 (Vídeo)** — Optional
   - Se o usuário disser que quer vídeos, chama roteirista
   - Entrega roteiros + cortes para Reels

### Checagem periódica do Gmail

Como **não há notificação automática de e-mail novo** nesta sessão, a orquestradora:

1. Calendariza uma **rotina de checagem a cada 30 minutos** (ou configurável)
   ```
   "Checar Gmail por resposta da aprovação de [fase]"
   ```

2. Se encontrar resposta:
   - **Processa a aprovação** (ou ajustes)
   - **Passa para próxima fase automaticamente**
   - **Cancela a rotina de checagem** (não é pra ficar rodando para sempre)

3. Se não encontrar resposta:
   - Não faz nada, não incomoda
   - Próxima checagem em 30 minutos

4. Se o usuário responder **na conversa** (aqui mesmo) em vez de e-mail:
   - Aceita a aprovação direto
   - Passa para próxima fase

### Estrutura de chamadas

A orquestradora chama cada skill como uma **rotina com contexto**:

```
"Continue a Fase 1.2 do pipeline. Os temas já foram aprovados.
Aqui está o briefing e os temas:

[Insere briefing + lista de temas]

Use a skill planejador-conteudo para desenhar o planejamento trimestral."
```

Cada skill recebe:
- Briefing atualizado (público, trimestre, cadência)
- Contexto da fase anterior (temas aprovados, plano aprovado, etc)
- Instruções claras

## Você pode parar a qualquer hora

Se em qualquer momento o usuário disser "não quero continuar" ou "muda de rumo":
- A orquestradora **cancela qualquer rotina pendente**
- **Para de aguardar aprovações**
- Fica pronta para reiniciar conforme o novo direcionamento

## Começar

Para iniciar o pipeline do zero:

```
/orquestrador-conteudo
```

Responda o briefing mínimo e a orquestradora começa a Fase 1.1 (Pesquisa).
