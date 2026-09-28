# Fontes de buzz e como verificar repercussão

O objetivo desta etapa é descobrir **o que as pessoas estão de fato
comentando** — não o que as consultorias publicaram. As fontes abaixo
servem para achar o assunto e provar que ele repercutiu. Os conceitos de
gestão vêm depois (ver `biblioteca-conceitos.md`).

## Onde procurar

### Termômetros de tendência
- **Google Trends** (buscas em alta no Brasil / "Year in search" semanal)
- **X/Twitter** trending topics — normalmente verificável via matérias que
  citam "o assunto ficou entre os mais comentados"
- **TikTok Creative Center** (hashtags e sons em alta)
- **YouTube** em alta
- **Reddit** (r/brasil, r/investimentos, r/marketing, r/technology)

Esses termômetros raramente podem ser abertos via `WebFetch`. Na prática,
use-os como pistas e confirme a repercussão por cobertura jornalística.

### Negócios, mercado e investimentos — Brasil
- Valor Econômico, InfoMoney, Exame, Estadão (Economia), Folha (Mercado),
  O Globo (Economia), NeoFeed, Brazil Journal, Pipeline (Valor), Money
  Times, CNN Brasil Business, g1 Economia

### Negócios, mercado e tecnologia — global
- Bloomberg, Reuters, Financial Times, Wall Street Journal, CNBC, The
  Verge, TechCrunch, Business Insider, Axios

### Marketing, marcas e creators
- Meio & Mensagem, Propmark, B9, Mundo do Marketing, AdNews, Adweek,
  Ad Age, The Drum, Marketing Week, Business of Fashion
- Portais de entretenimento e celebridades (g1 Pop & Arte, Terra,
  UOL Splash, Metrópoles, Quem) para polêmicas de influenciadores — sempre
  cruzando com um segundo veículo

## Buscas que funcionam

Combine **categoria + recorte temporal + tipo de evento**. Exemplos:

- `empresa polêmica viralizou redes sociais esta semana`
- `ação despenca bolsa [mês] [ano]` / `ação dispara maior alta [mês] [ano]`
- `CEO demitido [mês] [ano]` / `CEO renuncia após polêmica`
- `influenciador perde patrocínio [mês] [ano]` / `marca rompe contrato influenciadora`
- `campanha publicitária repercussão negativa [mês] [ano]`
- `lançamento viral marca [mês] [ano]`
- `mais comentados Twitter Brasil semana` / `assunto mais buscado Google semana`
- `recuperação judicial [mês] [ano]` / `IPO [mês] [ano]`
- `IA lançamento repercussão [mês] [ano]`
- Em inglês: `viral brand backlash this week`, `stock plunges [month] [year]`,
  `CEO ousted [month] [year]`, `creator brand deal controversy`

Use o nome do mês e o ano atual nas buscas — "esta semana" sozinho traz
muito conteúdo antigo.

## Checagem de data

- Verifique a **data de publicação** de cada matéria.
- O assunto conta como "dos últimos 7 dias" se o pico da conversa (ou um
  novo desdobramento relevante) caiu dentro da janela.
- Se o fato é antigo mas voltou à conversa nesta semana, registre o
  **gatilho recente** (novo capítulo, declaração, decisão judicial,
  resultado financeiro) na evidência de repercussão.

## Evidência mínima de buzz

Registre pelo menos uma destas na entrega:

- **2+ veículos independentes** cobrindo o assunto dentro da janela;
- menção verificável a **trending** ("ficou entre os assuntos mais
  comentados do X", "subiu 500% no Google Trends");
- **número publicado** de repercussão (views, menções, perda de
  seguidores, variação da ação, valor de mercado perdido);
- **reação de perfis de negócios** (executivos, marcas, publicações de
  marketing comentando o caso).

"Todo mundo está falando disso" sem evidência não entra.

## Quando WebFetch está bloqueado

Em algumas sessões remotas, `WebFetch` é bloqueado para certos domínios
enquanto `WebSearch` funciona. Nesse caso:

- Use apenas números e frases que apareceram **no snippet** do resultado
  de busca — nunca complete uma estatística a partir do título do link.
- A URL registrada precisa ter aparecido nos resultados; nunca reconstrua
  uma URL a partir do domínio ou do título.
- Se dois veículos divergirem sobre um número, não escolha um: cite a
  divergência ou descarte o dado.

## Sinais de alerta (fonte fraca)

- Perfis de fofoca ou "páginas de notícia" sem veículo por trás
- Threads que citam "um estudo" sem nomear qual
- Prints de post sem link para o original
- Conteúdo gerado por IA em sites caça-clique

Podem ser o motivo de você descobrir o assunto, mas sempre suba até a
fonte primária antes de incluí-lo.
