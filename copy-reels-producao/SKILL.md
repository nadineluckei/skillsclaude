---
name: copy-reels-producao
description: Especialista em produção visual para Reels/TikTok — cortes, timing, on-screen text, efeitos, sincronização com voiceover. Converte copy-reels-script em guia técnico de produção. Entrega table format completa.
---

# Copy-Reels Producao — Produção Visual para Reels/TikTok

## Visão Geral

Esta skill gera **instruções de produção visual** para vídeos curtos. Pega o roteiro de `copy-reels-script` e adiciona:

- **Cortes & Timing** (quando mudar de cena, quanto tempo ficar)
- **On-Screen Text** (o que escrever na tela, quando)
- **Efeitos & Transições** (quando usar, qual tipo)
- **Sincronização** (match voiceover com visual, timing de fade)
- **Assets Necessários** (fotos, vídeos, música, fontes)

**Output**: Table format pronto pra produtora ou creator seguir. Ou JSON estruturado.

**Integração**: Use junto com `copy-reels-script` pra resultado completo (script + produção).

---

## Entrada Esperada

O usuário pode pedir de três formas:

- **"Produção visual pra esse roteiro"** (passa roteiro) → Gera tabela com timing/cortes/texto
- **"Guia completo script + produção"** → Integra ambas skills
- **"Template de produção pra [tipo de conteúdo]"** → Estrutura padrão por formato

Se ambíguo, confirme qual output quer.

### Intake Interview (Antes de Gerar)

1. **Tipo de conteúdo?** (Talking head, tutorial, animação, motion graphics, compilado)
2. **Já tem assets?** (Vídeo, fotos, áudio) ou precisa orientação de como capturar
3. **Nível de produção?** (Minimalista/phone, amador/dslr, profissional)
4. **Software de edição?** (CapCut, Adobe Premiere, DaVinci, iMovie)
5. **On-screen text necessário?** (Títulos, captions, stats, setas/pointers)
6. **Efeitos desejados?** (Transições simples, zoom, blur, nada)
7. **Timing crítico?** (Sincronizar com beat de música, com números, etc)

---

## Estrutura: O Template de Produção Padrão

### Format de Tabela (Recomendado)

```
TIME (s)  | VISUAL/SCENE               | VOICEOVER/SOM        | ON-SCREEN TEXT     | TRANSIÇÃO/EFEITO
0-1       | [Descrição visual]         | [O que é falado]      | [Texto na tela]     | [Tipo de transição]
1-3       | [Descrição visual]         | [Continuação]         | [Próximo texto]     | [Efeito]
...       | ...                        | ...                   | ...                 | ...
```

### Seções de Produção

#### SEÇÃO 1: CORTES & TIMING

Quando e como mudar de cena.

**Padrão para Talking Head (0-3s Hook):**
- 0-1s: Establishing shot (wide) → Zoom leve pra close-up
- 1-2.5s: Close-up (face + shoulder)
- 2.5-3s: Transition pra próxima cena (zoom out, fade, cut)

**Padrão para Tutorial (8-20s Solution):**
- Setup shot (context)
- Screen capture (em loop se repetitivo)
- Cut quando muda de step
- Hold frame por 1-2s por step

**Padrão para Compilado/Montage:**
- Cut a cada beat de música
- Transição rápida (0.2-0.3s) vs. "breathing room" (0.5-1s)

#### SEÇÃO 2: ON-SCREEN TEXT (Critical)

O que escrever na tela, quando e onde.

**Regras:**
- Máx 5-7 palavras por frame
- Font legível em phone size (testar no 6" screen simulado)
- Aparecer por 2-3 segundos (tempo de leitura)
- Desaparecer antes de novo texto (não sobrepor)
- Posicionar longe de faces (cantos superiores/inferiores)

**Timing de ON-SCREEN TEXT:**

```
0-1s:    Aparece no HOOK — frase-chave (ALL CAPS ou bold)
1-3s:    Mantém + adiciona sub-text (cinza, smaller)
3s:      Fade out, novo text aparece
```

**Exemplo Hook de 3s:**

```
0-1s:    "71% DOS CMOS"
         "... dizem que atribuição é adivinhação"
1-3s:    "ASSISTE ATÉ O FIM"
3s:      Fade + novo texto
```

#### SEÇÃO 3: EFEITOS & TRANSIÇÕES

Quando e qual tipo usar.

**❌ EVITAR (Mata Performance):**
- Transições longas (>0.5s)
- Efeitos que piscam (seizure risk)
- Transições em cada cut (exaustão visual)
- Blur excessivo de fundo

**✅ USAR (Aumenta Retention):**
- **Cut simples** (nenhuma transição) = mais usado em TikTok viral
- **Fade** (0.2-0.3s) = transição suave
- **Zoom** (rápido, 0.3-0.5s) = direciona atenção
- **Slide** (0.2-0.3s) = movimento subtil
- **On-beat** transições (sincronizar com música) = adiciona ritmo

**Efeecto Pattern por Seção:**

```
HOOK (0-3s):
- Nenhuma transição, cut simples
- Talvez 1 zoom no 1.5s pra reforçar atençãoVisual pattern shift

SETUP (3-8s):
- 1-2 cortes naturais (transição simples, fade)
- Não saturar com efeitos

SOLUÇÃO (8-20s):
- Efeitos discretos só se algoritmica necessário
- Foco em conteúdo, não em "visual noise"

CTA (27-30s):
- Nenhuma transição nova (mantém visual estável)
- Apenas on-screen text animado (fade in)
```

#### SEÇÃO 4: SINCRONIZAÇÃO COM VOICEOVER

Match visual timing com o que é falado.

**Regra de Ouro:**
- Voiceover + Visual devem estar em **sincronia perfeita** em pontos-chave
- Pausa visual = pausa de voiceover
- Nova afirmação = visual muda

**Exemplo:**

```
VOICEOVER: "71% dos CMOs..."
VISUAL:    Wide shot, on-screen text aparece

VOICEOVER: "...dizem que atribuição é adivinhação."
VISUAL:    Zoom leve pra close-up, text evolui

VOICEOVER: "Vou te mostrar por quê."
VISUAL:    Fade pra nova cena (corte)
```

**Timing Técnico:**
- Voiceover gravado primeiro (padrão)
- Depois visual editado pra matchar
- Deixar "breathing room" de 0.5s entre frases (permite pausa natural)

#### SEÇÃO 5: ASSETS NECESSÁRIOS

O que capturar / criar antes de editar.

**Video:**
- Talking head: Mínimo 2 ângulos diferentes (wide + close-up)
- Screen capture: Resolução 1080p, 60fps (se motion é rápido)
- Background: Neutro ou on-brand, bem iluminado

**Audio:**
- Voiceover: Gravado em estúdio ou room tratada (sem eco)
- Bed music: Trending sound ou background track (low volume)
- Efeitos sonoros: Opcional, mas aumenta retention

**Texto:**
- Font: Sistema operacional (Helvetica, San Francisco, Roboto) ou on-brand
- Cor: Contraste alto com fundo (branco/preto é safe)
- Tamanho: Testado em phone 6"

**Outros:**
- Captions .srt (opcional, requer trabalho extra)
- Sutis: Arrows, circles, background blurs pra dirigir atenção

#### SEÇÃO 6: INSTRUÇÕES POR TIPO DE CONTEÚDO

##### Tipo 1: Talking Head (Conversacional)

```
Timing    | Visual                 | VO              | On-Screen Text    | Efeito
0-1s      | Wide (body + face)     | Hook            | Título/pergunta    | Nada
1-2.5s    | Zoom suave pra close   | Desenvolvimento | Sub-text           | Zoom (0.3s)
2.5-3s    | Fade out               | Transição       | —                  | Fade (0.3s)
3-8s      | Setup novo             | Setup           | Novo título        | Cut
8-20s     | Close ou demo visual   | Solução         | Números/prova      | Subtle zoom
20-27s    | Voltando pra close     | Benefit         | Resultado          | Nada
27-30s    | Mantém close           | CTA             | CTA em bold        | Fade final
```

**Dicas:**
- Iluminação frontal (evita sombras)
- Olha pra câmera por 70% do tempo
- Micro movimentos (hands, expressão) mantêm engajamento
- Evita piscadas no 3s mark (soa artificial)

##### Tipo 2: Tutorial / Screen Capture

```
Timing    | Visual                   | VO              | On-Screen Text    | Efeito
0-1s      | Screen wide (full)       | Hook            | Título da task     | Nada
1-8s      | Screen + pointer         | Setup           | Step 1, Step 2     | Simples cortes
8-20s     | Close em detalhe crítico | Solução (steps) | Números/highlights | Zoom em crítico
20-27s    | Resultado final          | Benefit         | "Pronto!"          | Nada
27-30s    | CTA (botão/link)         | CTA             | "Clica aqui"       | Fade final
```

**Dicas:**
- Screen capture em 1080p, 60fps pra smooth motion
- Slow down (0.75x ou 0.8x) se movimento muito rápido
- Zoom em área crítica (+25-50%) pra legibilidade
- Use cursor highlight pra direcionar atenção

##### Tipo 3: Motion Graphics / Animação

```
Timing    | Visual                   | VO              | On-Screen Text    | Efeito
0-1s      | Animação hook (intro)    | Hook            | Número/titulo      | Entrance animation
1-3s      | Evolui animação          | Setup           | Subtítulo          | Morph/swipe
3-8s      | Novo elemento            | Body            | Cada ponto          | Stagger animation
8-20s     | Build-up visual          | Solução         | Estatísticas       | Entrada sincro
20-27s    | Climax visual            | Benefit         | Resultado          | Saída sincro
27-30s    | Logo/CTA aparece         | CTA             | CTA animado        | Exit animation
```

**Dicas:**
- Entrada/saída de texto sincronizadas com voiceover
- Não fazer 2 animações simultâneas (distração)
- Motion leve (não "crazy" — mata retention)
- Cores alinhadas com brand

##### Tipo 4: Compilado / Montage

```
Timing    | Visual                   | VO              | On-Screen Text    | Efeito
0-1s      | Clip 1 hook              | Hook            | Título            | Cut simples
1-1.5s    | Clip 2                   | Transição       | —                  | Cut
1.5-2.5s  | Clip 3 setup             | Setup           | Label              | Fade rápido
2.5-3s    | Clip 4                   | Setup cont      | —                  | Cut
3-8s      | Multi-clip loop (repeat) | Body            | Números/stats      | Cut on beat
8-20s     | Clip novo pra solução    | Solução         | Key insight        | Transição temática
20-27s    | Montage rápido           | Benefit         | Resultado          | Cut on beat
27-30s    | Clip final + CTA         | CTA             | CTA bold           | Fade
```

**Dicas:**
- Sincronize cortes com beat de música (0.2-0.3s entre clips)
- Alternei comprimento de clips (1s, 1.5s, 0.5s) pra ritmo
- Não usar mesma clip 2x (monótono)
- Color grade ligeiramente diferentes se clips são de fontes diferentes

#### SEÇÃO 7: QUALITY GATE DE PRODUÇÃO

Antes de exportar final:

1. ✅ Voiceover sincronizado com visual em pontos-chave?
2. ✅ On-screen text legível em phone 6"?
3. ✅ Nenhuma transição > 0.5s?
4. ✅ Efeitos discretos (não saturado)?
5. ✅ Audio levels balanced (VO 70%, música 30%)?
6. ✅ Sem artefatos de compressão (pixelação, freeze frames)?
7. ✅ Cores consistentes entre clips?
8. ✅ Duração exata (0-3s hook rápido, resto conforme plano)?
9. ✅ Áudio export em 128kbps MP4 stereo?
10. ✅ Testado em phone real antes de upload?

---

## Os 10+ Padrões de Produção Que Funcionam

### Padrão 1: The Zoom-In-Slow-Down
**O que é:** Zoom leve na face durante hook (0-1.5s), hold por 1.5s
**Por que funciona:** Direciona atenção pra rosto (confiança + conexão)
**Timing:** Começa em 0.5s, completa em 1.5s
**Quando usar:** Talking head, confession, contrarian hooks

### Padrão 2: The Cut-on-Beat
**O que é:** Corte visual sincronizado exato com beat de música
**Por que funciona:** Ritmo aumenta retention
**Timing:** Marque exatamente onde beat cai, corte 1 frame antes
**Quando usar:** Montage, fast-paced content, energia alta

### Padrão 3: The Micro-Gancho Visual (35s Mark)
**O que é:** Mudança visual repentina no segundo 35 (em Reels 45-60s)
**Por que funciona:** Recovers viewers primed to scroll
**Timing:** 0.3s cut + fade, nada muito longo
**Quando usar:** Extended reels só

### Padrão 4: The Fade-to-Black Pause
**O que é:** Fade to preto, hold 0.5s com on-screen text só, fade in
**Por que funciona:** Força pausa de atenção (reset)
**Timing:** Total 1-1.5s
**Quando usar:** Transição entre seções principais

### Padrão 5: The Pointer / Arrow Direction
**O que é:** Animação sutil de seta/círculo direciona pra elemento importante
**Por que funciona:** Direciona atenção sem parecer amateurista
**Timing:** Aparece com on-screen text, some quando text vai
**Quando usar:** Screen capture, números críticos, detalhe visual

### Padrão 6: The Staggered Text Stack
**O que é:** Primeira linha aparece, 0.5s depois aparece segunda linha (não simultâneo)
**Por que funciona:** Permite leitura sequencial (não compete com voiceover)
**Timing:** Cada linha +0.5s depois
**Quando usar:** Stats, multi-point lists, números

### Padrão 7: The Contrast Cut
**O que é:** Corte repentino de quiet scene pra high-energy (ou inverso)
**Por que funciona:** Padrão interrupção (stop scroll)
**Timing:** 0.3s total, abrupt
**Quando usar:** Problem-to-solution transition, contrarian hooks

### Padrão 8: The Slow-Mo Emphasis
**O que é:** Replay de ação importante em slow motion (0.75x ou 0.5x)
**Por que funciona:** Destaca momento crítico
**Timing:** Apenas no key moment (1-2s em slow)
**Quando usar:** Resultado visual, ação que prova ponto

### Padrão 9: The Consistent Framing
**O que é:** Mesma posição de câmera pra falas principais (consistency builds trust)
**Por que funciona:** Reduz "visual noise"
**Timing:** Volta pra mesmo frame a cada nova ideia
**Quando usar:** Education, authority positioning

### Padrão 10: The Edge Blur / Vignette
**O que é:** Subtle blur das laterais (1-2% opacity) pra dirigir olho ao centro
**Por que funciona:** Foco visual sem parecer artificial
**Timing:** Presente durante todo vídeo (consistency)
**Quando usar:** Talking head, busy backgrounds, distraction reduction

---

## Integração: Copy-Reels Script → Produção

### Como Usar Ambas Skills Juntas

1. **Generate roteiro** com `copy-reels-script`
2. **Receba JSON** com hook, timing, CTA
3. **Input pra `copy-reels-producao`**: Cole JSON + tipo de conteúdo
4. **Output**: Table format completo (Time | Visual | VO | Text | Efeito)
5. **Passe pra producer/editor** com tabela

### Format de Integração

```
TIME (s)  | VISUAL/SCENE                           | VOICEOVER/SOM                      | ON-SCREEN TEXT      | TRANSIÇÃO/EFEITO
0-1       | Close-up face, vibe provocador         | "71% dos CMOs dizem que atribuição  | "71% DOS CMOS"       | Nenhuma (cut)
          |                                        | é adivinhação."                    | (white, bold, center)|
1-3       | Zoom suave in, mantém close            | "Vou te mostrar por quê."          | "Assiste até fim"    | Zoom (0.3s)
          |                                        |                                    | (gray, smaller)      |
3-8       | Fade pra screen capture de CRM         | "Seu CEO em call de forecast..."   | "PROBLEMA:"          | Fade (0.3s)
          |                                        |                                    | "5 touchpoints"      |
8-20s     | Screen + pointer apontando pra dados   | "Marketing, email, ads, web..."    | Cada touchpoint      | Subtle zoom no crítico
          |                                        |                                    | numerado (1, 2, 3..)|
20-27s    | Close-up face novamente, direito       | "Medir real = investir em canais   | "SOLUÇÃO:"           | Nenhuma
          |                                        | certos."                           | "Dados integrados"   |
27-30s    | Mantém close, fade leve                | "Salva esse — próximo explico."    | "SALVA ESSE"         | Fade final (0.5s)
          |                                        |                                    | (bold, white, center)|
```

---

## Quality Checklist (Template)

Antes de passar pra producer/exportar:

- [ ] Voiceover e visual sincronizados em pontos-chave
- [ ] On-screen text legível em phone 6"
- [ ] Nenhuma transição > 0.5s
- [ ] Efeitos discretos (não oversaturated)
- [ ] Áudio levels balanced
- [ ] Sem artifacts de compressão
- [ ] Cores consistentes
- [ ] Duração correta (0-3s hook = fast, resto = timing conforme plano)
- [ ] Audio export 128kbps stereo MP4
- [ ] Testado em phone real antes de final

---

## Troubleshooting

**"Voiceover tá fora de sync"**
→ Audio foi gravado pós-produção. Re-time visual pra matchar VO (não o contrário).

**"On-screen text é muito pequeno pra mobile"**
→ Increase font size 50%, test em phone simulado. Melhor deixar menos text que inlegível.

**"Transitions tão muito lento"**
→ Corte 50% do duration. Transitions > 0.5s matam scroll-through.

**"Background muito busy"**
→ Apply subtle blur (-10 to -20 in editor) ou vignette (1-2% edge blur).

**"Video tá "dead" — sem energia"**
→ Aumenta audio levels do bed music (+3-5db), adiciona 1 zoom/cut sutil.

**"Efeitos ficaram demais"**
→ Remove 50%. Motion graphics = less is more. Content é star, não efeitos.
