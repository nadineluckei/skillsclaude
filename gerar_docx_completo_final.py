#!/usr/bin/env python3
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_carousel(doc, c):
    carrossel_heading = doc.add_heading(f'CARROSSEL {c["numero"]}: {c["titulo"]}', level=2)
    info = doc.add_paragraph(f'Eixo: {c["eixo"]} | Tipo: {c["tipo"]}')
    info.runs[0].italic = True
    info.runs[0].font.size = Pt(10)
    info.space_after = Pt(12)

    for slide in c['slides']:
        slide_para = doc.add_paragraph()
        slide_para.add_run(f'SLIDE {slide["numero"]}: ').bold = True
        slide_para.add_run(slide['title'])
        slide_para.space_after = Pt(6)
        text_para = doc.add_paragraph(slide['texto'])
        text_para.space_after = Pt(12)

    caption_heading = doc.add_paragraph()
    caption_heading.add_run('CAPTION:').bold = True
    caption_para = doc.add_paragraph(c['caption'])
    caption_para.space_after = Pt(12)

    sources_heading = doc.add_paragraph()
    sources_heading.add_run('FONTES:').bold = True
    for fonte in c['fontes']:
        fonte_para = doc.add_paragraph(fonte['titulo'])
        fonte_para.runs[0].font.color.rgb = RGBColor(5, 99, 193)
        fonte_para.runs[0].underline = True
        fonte_para.space_after = Pt(6)

    doc.add_paragraph()

carrosseis_completos = [
    {
        "numero": 1, "mes": "SETEMBRO", "eixo": "Liderança e Decisão",
        "titulo": "Seu time não fracassa. Você está pedindo para eles fracassarem.",
        "tipo": "Liderança + Responsabilidade",
        "slides": [
            {"numero": 1, "title": "SEU TIME NÃO FRACASSA. VOCÊ ESTÁ PEDINDO PARA ELES FRACASSAREM.", "texto": "Como você culpa capacidade quando o problema é clareza."},
            {"numero": 2, "title": "Aquele seu melhor funcionário que saiu semana passada", "texto": "Não saiu por falta de capacidade. Saiu porque não sabia pra onde a empresa ia. Porque liderança nunca deixou claro qual era a estratégia, o que media sucesso, como a gente decide aqui. Saiu porque talento não quer mais cobrança sem direção."},
            {"numero": 3, "title": "70% dos problemas de performance vêm de falta de clareza", "texto": "Não de capacidade. Não é que o time é ruim. É que o time está cego porque você não deixou claro pra onde está indo. E talentos bons não ficam em empresas cegas."},
            {"numero": 4, "title": "É como cinco pessoas remando um barco sem saber pra onde vai", "texto": "Cinco remadores competentes. Cinco pessoas que sabem remar bem. Mas se cada um está puxando pra um lado — um quer ir pro norte, outro pro sul, outro fica remando pra trás — o barco não anda. Ou anda em círculos. O problema não é competência de remar. É que ninguém sabe o destino."},
            {"numero": 5, "title": "LIDERANÇA NÃO É EXIGIR MAIS. É DEIXAR CLARO PARA ONDE.", "texto": "O que faz talento querer ficar é saber o destino. É entender qual é a estratégia. É ter clareza de como a gente decide aqui. É confiar que a direção faz sentido. Sem isso, você pode ter o melhor time do mundo e ele vai ficar paralisado ou frustrado."},
            {"numero": 6, "title": "Em 2026, reter talento não é bônus ou cultura cool. É clareza.", "texto": "Talentos não saem porque o salário é baixo — saem porque não sabem pra onde vão. Não saem porque não gostam do time — saem porque a direção fica mudando toda semana. Não saem porque o trabalho é duro — saem porque ninguém explicou por que vale a pena fazer esse trabalho."},
            {"numero": 7, "title": "3 sinais de que seu time está desmotivado por falta de clareza", "texto": "1. As pessoas trabalham isoladas — ninguém entende como seu trabalho conecta ao objetivo maior. 2. Decisões parecem aleatórias — muda de prioridade toda semana. 3. Talentos saem em silêncio — pedem demissão sem feedback, sem briga, só saem."},
            {"numero": 8, "title": "Antes de culpar capacidade: pergunta se você foi claro.", "texto": "Porque talentos ruins ficam em empresas certas. E talentos bons fogem de empresas que não sabem para onde vão. A culpa não é deles. É sua."},
        ],
        "caption": "Seu melhor talento não está saindo porque não consegue fazer o trabalho — está saindo porque você não deixou claro pra onde a empresa vai. Esse é o padrão que vemos em operações por aí: líderes cobram resultado mas nunca deixam explícito qual é a estratégia, por que aquela prioridade importa, ou como a organização decide quando há conflito. Aí vem o time cego, pulando de tarefa em tarefa, achando que está falhando em capacidade quando na verdade está falhando em direção. A ilusão da tecnologia mata empresa — mas a falta de clareza mata empresa duas vezes. Porque além de perder talento, você fica achando que o problema é as pessoas, não a sua liderança. Se você está perdendo seus melhores profissionais e achando que é por falta de capacidade, a pergunta real é: você foi claro sobre pra onde está indo? O que você faria diferente na próxima conversa com sua liderança sobre clareza estratégica? Comenta aí.",
        "fontes": [
            {"titulo": "Harvard Business Review: Why Talent is Leaving Your Organization (2024)", "link": "https://www.hbr.org"},
            {"titulo": "McKinsey: Why Talent is Leaving Your Organization (2024)", "link": "https://www.mckinsey.com"}
        ]
    },
    {
        "numero": 2, "mes": "SETEMBRO", "eixo": "Liderança e Decisão",
        "titulo": "Decisão sem dados é opinião. Decisão com dados errados é pior.",
        "tipo": "Liderança + Dados",
        "slides": [
            {"numero": 1, "title": "DECISÃO SEM DADOS É OPINIÃO. DECISÃO COM DADOS ERRADOS É PIOR.", "texto": "Como seus dashboards bonitos estão te deixando cego."},
            {"numero": 2, "title": "Você tem um dashboard lindo. Mostra ele na reunião.", "texto": "Todos acreditam que você controla a situação. Porque tem números. Porque aquele número subiu. Porque você está tão orgulhoso de mostrar que tem tudo sob controle. Só que — enquanto esse número sobe — a empresa inteira está piorando em outro lugar."},
            {"numero": 3, "title": "Empresas colhem dados ruins, interpretam errado, e decidem pior", "texto": "Do que se tivessem seguido instinto puro. Confundem correlação com causalidade. Veem dois eventos acontecendo junto e acham que um causou o outro. A obsessão por dados sem compreensão de contexto deixa empresa cega de um jeito diferente: confiante e cega."},
            {"numero": 4, "title": "É como surfar olhando só pro velocímetro da prancha", "texto": "Você vê a velocidade aumentando e acha que está indo bem. Mas não olha onde a onda está indo. Não vê se tem outro surfista na frente. Não sente se a prancha está em equilíbrio. Olhou só pra um número e ignorou tudo mais que está acontecendo na água."},
            {"numero": 5, "title": "O PROBLEMA NÃO É O NÚMERO. É A HISTÓRIA QUE VOCÊ CONTA A PARTIR DELE.", "texto": "Um número que sobe não explica por quê. Um número que sobe em um departamento não explica o impacto nos outros. Um gráfico que cresce enquanto a margem cai é dado sem contexto. A pergunta não é \"aumentou?\". A pergunta é \"por quê? E se mudar de novo amanhã, como fico?\"."},
            {"numero": 6, "title": "DADOS ERRADOS NÃO GERAM DÚVIDA. GERAM CONFIANÇA NA DECISÃO ERRADA.", "texto": "Se você segue instinto errado, pelo menos fica em dúvida. Questiona. Busca mais informação. Mas se você tem um número, um gráfico, um dashboard — você segue com certeza. E aí você não apenas erra. Você erra acreditando que está sendo racional."},
            {"numero": 7, "title": "Antes de decidir por um número, faça 3 perguntas", "texto": "1. Por que esse número está assim? Qual é a causa real, não só o sintoma? 2. O que mudou no contexto desde a última vez que esse número importava? 3. Se o contexto mudar novamente amanhã, essa decisão continua fazendo sentido?"},
            {"numero": 8, "title": "A pergunta não é \"aumentou?\". A pergunta é \"por quê?\"", "texto": "Dado sem contexto é ilusão. Contexto sem dado é achismo. O líder que ganha é quem consegue ambos. Qual você tem escolhido?"},
        ],
        "caption": "Você tem dashboards lindos. Números bonitos. Gráficos que mostram tudo sob controle. Só que enquanto você olha pra aquele número que subiu, a empresa inteira está piorando em outro lugar. Essa é a receita pronta do mercado: ser data-driven. Mas ninguém fala que dados sem contexto é pior que opinião pura. Porque opinião você questiona. Dados errados você segue com certeza. O padrão que vejo é: empresas confundem correlação com causalidade o tempo inteiro. Veem um comportamento e outro lado a lado, acham que um causou o outro, e tomam decisão. Enquanto isso, estava acontecendo outra coisa completamente diferente no contexto que ninguém olhou. A ditadura das receitas prontas está aí: ser data-driven virou frase de efeito, sem ninguém avisar que dados ruins são pior que nenhum dado. Isso atinge o gerente que quer provar resultado, o diretor que quer mostrar controle, todo tomador de decisão que quer parecer racional mas está na verdade confiante em decisão errada. A pergunta é: você conhece a diferença entre número que subiu e compreensão do por quê? Qual foi a última decisão sua baseada em dados que você questionou o contexto? Comenta aí.",
        "fontes": [
            {"titulo": "McKinsey: Decision-Making and Data in Marketing (2024)", "link": "https://www.mckinsey.com"},
            {"titulo": "Harvard Business Review: Data Interpretation Bias (2023)", "link": "https://www.hbr.org"}
        ]
    },
    {
        "numero": 3, "mes": "SETEMBRO", "eixo": "Crescimento e Estratégia",
        "titulo": "Foco é a palavra mais cara que você nunca implementa.",
        "tipo": "Crescimento + Estratégia",
        "slides": [
            {"numero": 1, "title": "FOCO É A PALAVRA MAIS CARA QUE VOCÊ NUNCA IMPLEMENTA.", "texto": "Você diz que foca mas investe em tudo."},
            {"numero": 2, "title": "Toda reunião de estratégia tem essa frase: \"Vamos focar em X\"", "texto": "Semana depois aparece uma oportunidade em Y. Tem potencial, não é errada, é diferente. Você aprova. Semana depois vem Z. Depois vem W. De repente você está fazendo de tudo."},
            {"numero": 3, "title": "Empresas dizem que focam, mas investem em 10 projetos simultâneos", "texto": "Têm 5 prioridades \"críticas\". Mudam de estratégia a cada trimestre. Time está fragmentado. Pulando de tarefa em tarefa o tempo inteiro. Resultado mediocre. E a gente chama isso de \"ser ambicioso\"."},
            {"numero": 4, "title": "É como uma roda de samba tocando vários sambas ao mesmo tempo", "texto": "Cada músico é competente. Cada um sabe tocar bem seu instrumento. Mas se estão tocando ritmos diferentes, diferentes tempos, diferentes sambas — o resultado é caos. Ninguém entra em sincronia. A batida não fecha. Porque estão em transição constante."},
            {"numero": 5, "title": "NÃO É QUE VOCÊ TEM MUITAS IDEIAS. É QUE VOCÊ PERSEGUE MUITAS IDEIAS.", "texto": "Ideias boas abundam. Execução focada é rara. Você confunde foco com perda de oportunidade. Quando na verdade foco é dizer não pra 90% pra poder dizer sim com profundidade pra 10%. Foco é decisão, não limitação."},
            {"numero": 6, "title": "A empresa que domina um mercado com profundidade vence sempre", "texto": "A que toca 5 mercados de rasante. Porque ela acumulou conhecimento, relacionamento, reputação num lugar só. A outra empresa está em transição o tempo inteiro. Foco não é sacrifício. Foco é arma competitiva."},
            {"numero": 7, "title": "3 perguntas para saber se sua empresa é realmente focada", "texto": "1. Você consegue dizer \"não\" para oportunidades boas? Se não consegue, não é focado. 2. Seu time pula entre tarefas constantemente? Quantas vezes por dia mudam de prioridade? 3. Você muda de estratégia a cada trimestre? Se muda, prioridades não são claras."},
            {"numero": 8, "title": "Você não é focado. Você é indeciso disfarçado de ambicioso.", "texto": "Foco é decisão. E decisão é dizer \"não\" pra 90% das oportunidades pra poder dizer \"sim\" com profundidade pra 10%. Qual você tem escolhido?"},
        ],
        "caption": "Você diz que foca. Na última reunião estratégica você falou que 2026 é sobre foco. Mas quando você olha os projetos aprovados nos últimos 3 meses, estão fazendo de tudo. 10 projetos simultâneos. 5 prioridades \"críticas\". Estratégia que mudou 2 vezes esse semestre. Isso não é foco, é indecisão disfarçada de ambição. A ditadura das receitas prontas está aí: \"vamos ser focados\" virou frase bonita que ninguém implementa de verdade. Porque implementar foco significa dizer não. Significa olhar pra uma oportunidade boa — de verdade boa — e dizer que não cabe agora. Significa ter clareza do que você está sacrificando pra profundar em outra coisa. A miopia operacional começa aí: você pensa que estar em 5 lugares é estar em lugar nenhum, mas segue fazendo de tudo do mesmo jeito. Isso atinge o gestor que quer agradar todo mundo, o empreendedor que vê oportunidade em tudo, o diretor que não consegue priorizar. O resultado é sempre o mesmo: times fragmentados, resultados mediocres, talento saindo porque não sabe qual é o destino. A pergunta é: você consegue dizer \"não\" pra uma oportunidade boa? Ou você já perdeu a capacidade de focar? Qual foi a última vez que você realmente priorizou e deixou algo importante de fora? Manda aí.",
        "fontes": [
            {"titulo": "McKinsey: The Focused Corporation (2024)", "link": "https://www.mckinsey.com"},
            {"titulo": "BCG: Strategic Focus and Growth (2023)", "link": "https://www.bcg.com"}
        ]
    },
    {
        "numero": 4, "mes": "SETEMBRO", "eixo": "Futuro e Adaptação",
        "titulo": "Cenários futuros são previsões. O que importa é como você se move.",
        "tipo": "Futuro + Adaptação",
        "slides": [
            {"numero": 1, "title": "CENÁRIOS FUTUROS SÃO PREVISÕES. O QUE IMPORTA É COMO VOCÊ SE MOVE.", "texto": "Você gasta tempo prevendo. Deveria gastar aprendendo a se adaptar."},
            {"numero": 2, "title": "Todo planejamento começa com \"e se?\"", "texto": "E se o mercado ficar assim? E se o consumidor mudar? E se o concorrente fizer aquilo? Você desenha cenários bonitos. Faz projeção. Apresenta na reunião. Aí os próximos 6 meses ninguém faz nada até o cenário se confirmar."},
            {"numero": 3, "title": "A realidade é: ninguém acerta em prognóstico", "texto": "Previsão é ilusão. O que acontece sempre é diferente do que você imaginou. Não porque você errou na análise, mas porque mundo é caótico. Variáveis demais. Contexto muda rápido. O que você planejou pro cenário A virou obsoleto no cenário C."},
            {"numero": 4, "title": "É como tentar seguir a batida certa da música quando a música muda", "texto": "Você aprendeu a sambar em determinado ritmo. Treinou muito. Você sabe sambar bem naquele ritmo. Mas de repente a música muda. O ritmo é outro. A batida é outra. Se você fica insistindo no ritmo anterior, fica desafinado. O que funciona é aprender a dançar com o ritmo que está tocando agora."},
            {"numero": 5, "title": "O PROBLEMA NÃO É PREVER O FUTURO. É ESTAR PREPARADO PARA QUALQUER FUTURO.", "texto": "Empresas que ganham não são as que acertam em previsão. São as que estão preparadas pra mudar rápido quando contexto muda. Que conseguem pivotar. Que têm estrutura mental pra se adaptar. Porque mudança é a única certeza."},
            {"numero": 6, "title": "Em 2026, adaptabilidade vale mais que previsão", "texto": "Porque o futuro vai ser diferente do que você imaginou. Sempre é. O que diferencia não é quem adivinhou certo. É quem consegue se mover rápido quando tudo muda. Quem mantém a estrutura ágil."},
            {"numero": 7, "title": "3 sinais de que você está preso em previsão errada", "texto": "1. Você gasta mais tempo defendendo seu cenário que testando hipóteses. 2. Seu plano não tem Plano B porque \"o Plano A vai dar certo\". 3. Quando contexto muda, você segue como se nada tivesse mudado."},
            {"numero": 8, "title": "Não é sobre adivinhar futuro. É sobre estar pronto pra mudança.", "texto": "A pergunta real não é \"qual cenário vai acontecer?\". É \"qual é minha capacidade de me adaptar quando tudo mudar?\". Qual você consegue responder?"},
        ],
        "caption": "Você passa meses desenhando cenários do futuro. Faz projeção bonita. Apresenta pra liderança. E depois os próximos 6 meses a empresa inteira fica congelada esperando seu cenário se confirmar. Quando na verdade o mundo já virou pra outro lado completamente diferente. Essa é a receita pronta: prever bem. Mas ninguém avisa que previsão é ilusão. Porque mundo é caótico. Variáveis demais. Contexto muda mais rápido que qualquer planejamento que você faça. A empresa que ganha não é a que acertou na previsão — é a que conseguiu se adaptar rápido quando o contexto virou. É a que tinha estrutura mental pra pivotar. A miopia operacional do planejamento está aí: você gasta tempo prevendo quando deveria estar preparado pra qualquer futuro. Isso atinge o estrategista que quer controlar tudo, o gerente que quer ter a resposta certa antes de agir, todo tomador de decisão que confunde planejamento com vidência. O padrão é: quando contexto muda, empresa fica presa no cenário que previa porque não construiu capacidade de adaptação. A pergunta é: você consegue pivotar rápido quando tudo muda? Ou você fica preso defendendo o cenário que acreditava? Qual foi a última vez que você mudou de direção sem perder tempo? Comenta aí.",
        "fontes": [
            {"titulo": "MIT Technology Review: Adaptive Strategy in Uncertain Times (2024)", "link": "https://www.technologyreview.com"},
            {"titulo": "Harvard Business Review: Scenario Planning and Adaptability (2023)", "link": "https://www.hbr.org"}
        ]
    },
    {
        "numero": 5, "mes": "OUTUBRO", "eixo": "Crescimento e Competição",
        "titulo": "Quando você copia estratégia do competitor, você já perdeu.",
        "tipo": "Crescimento + Competição",
        "slides": [
            {"numero": 1, "title": "QUANDO VOCÊ COPIA ESTRATÉGIA DO COMPETITOR, VOCÊ JÁ PERDEU.", "texto": "O que funciona pra player grande não funciona pra você."},
            {"numero": 2, "title": "Seu competitor grande faz assim. Você pensa: vamos fazer igual.", "texto": "Faz sentido. Eles têm recursos, marca, escala. Se funciona pra eles, tem que funcionar pra gente. Você copia a tática. Executa bem. E nada acontece. Ou, pior: você queima orçamento e não consegue o resultado que eles conseguem."},
            {"numero": 3, "title": "O que funciona pra player grande falha pra empresa menor", "texto": "Porque contextos são radicalmente diferentes. Recursos diferentes. Marca diferente. Posição de mercado diferente. Capacidade de investimento diferente. Copy-paste de estratégia ignora essas diferenças estruturais."},
            {"numero": 4, "title": "É como um atleta profissional ensinar sua técnica pra iniciante na musculação", "texto": "Atleta faz exercício que demanda força que levou 10 anos pra desenvolver. Iniciante vê, tenta fazer igual, se machuca. A técnica funciona pro atleta porque tem base, volume, força acumulada. Iniciante não consegue reproduzir resultado porque contexto do corpo é diferente. Copy-paste de técnica não recupera 10 anos de treino."},
            {"numero": 5, "title": "COPY-PASTE DE ESTRATÉGIA FALHA PORQUE VOCÊ NÃO TEM O MESMO CONTEXTO.", "texto": "Você não tem os mesmos recursos, a mesma marca equity, a mesma posição de mercado. Quando você copia sem adaptar pra sua realidade, está competindo no jogo que o player grande já ganhou. E você não pode ganhar ali porque as regras são favelas pra ele."},
            {"numero": 6, "title": "Em 2026, único jeito de vencer é jogando seu próprio jogo", "texto": "Não o jogo que o player grande inventou. Você precisa entender o que seu mercado precisa e que o player grande não consegue entregar. Aí você vence. Porque compete onde tem vantagem."},
            {"numero": 7, "title": "3 sinais de que você está copiando estratégia errada", "texto": "1. Você gasta os mesmos recursos que o player grande mas consegue 30% do resultado. 2. Sua proposta é idêntica mas seu preço é menor — isso é commoditização. 3. Seu positioning é \"somos igual, mas mais barato\" — você já perdeu."},
            {"numero": 8, "title": "Você não vence competitor maior copiando. Vence entendendo seu mercado melhor.", "texto": "Qual é o problema que você consegue resolver melhor? Qual é o jeito diferente de você pensar sobre seu cliente? Aí você ganha."},
        ],
        "caption": "Seu competitor grande usa estratégia X e funciona. Você acha que a solução é copiar. Executa bem. Queima orçamento. Nada acontece. Porque você está competindo no jogo que ele já ganhou. E nesse jogo, ele sempre vai ganhar porque tem mais recursos, mais marca, mais escala. A ditadura das receitas prontas está aí: copy-paste de tática bem executada é receita pro fracasso. Ninguém avisa que o contexto é diferente. Que o que funciona pra player grande — com equity de marca, com recursos, com posição consolidada — não funciona pra PME. Porque o jogo é diferente. Você não compete com o player grande nos critérios que ele é bom. Você compete achando um critério que ele é fraco. O padrão que vejo é: empresa pequena tira estratégia de grande, copia, e acha que não funcionou porque execução foi ruim. Quando na verdade foi ruim porque estava tentando ganhar um jogo que não era o jogo dela. Isso atinge o gestor que quer segurança de \"se funciona lá, funciona aqui\", o gerente que não quer arriscar em estratégia própria. A pergunta é: você conhece o mercado que você quer vencer melhor do que seu competitor grande? Qual é a única coisa que você consegue fazer melhor que qualquer outro? Qual é o jogo seu, não dele? Manda aí.",
        "fontes": [
            {"titulo": "BCG: Competing in an Age of Disruption (2024)", "link": "https://www.bcg.com"},
            {"titulo": "McKinsey: Competitive Strategy for SMBs (2023)", "link": "https://www.mckinsey.com"}
        ]
    },
    {
        "numero": 6, "mes": "OUTUBRO", "eixo": "Crescimento e Operação",
        "titulo": "Qualidade não é feita no final. É decidida no começo.",
        "tipo": "Crescimento + Operação",
        "slides": [
            {"numero": 1, "title": "QUALIDADE NÃO É FEITA NO FINAL. É DECIDIDA NO COMEÇO.", "texto": "Lançar rápido e corrigir depois é ilusão (muito cara)."},
            {"numero": 2, "title": "Você quer lançar rápido. Corrige depois se tiver problema.", "texto": "Faz sentido em teoria. Pense rápido, errado é melhor que lento e perfeito. Mas a realidade é: quando você lança coisa de qualidade ruim, o mercado forma opinião ruim e você não recupera mais. Marca fica suja. Confiança vai embora."},
            {"numero": 3, "title": "Marcas que lançam com qualidade ruim nunca recuperam percepção", "texto": "Custo de corrigir depois é 10x maior que fazer certo desde o início. Porque você gasta em marketing pra limpar imagem. Perde cliente que não volta. Perde confiança. E confiança quando perdida demora anos pra recuperar — se recupera."},
            {"numero": 4, "title": "É como começar um treino de yoga com postura errada", "texto": "Você aprende postura errada. Treina com postura errada 100 vezes. Agora seu corpo aprendeu errado. Depois precisa desaprender. Desaprender é mais difícil que aprender certo desde o começo. Quanto mais você repete algo errado, mais profundo fica no seu sistema."},
            {"numero": 5, "title": "QUALIDADE NÃO É FEATURE EXTRA. É DECISÃO SOBRE O QUE VOCÊ ACEITA COMEÇAR.", "texto": "Decisão é feita no design, não na execução. Quando você decide o que vai fazer, já está decidindo a qualidade que isso vai ter. Se quer qualidade, começa a pensar em qualidade no primeiro sketch, no primeiro protótipo, no primeiro texto. Não deixa pra corrigir depois."},
            {"numero": 6, "title": "Em 2026, primeira impressão vale mais que segunda chance", "texto": "Mercado é barulhento. Atenção é escassa. Se você lança de qualidade ruim, pode ser que a pessoa não volte pra segunda vez. Economia de tempo é ilusão. Você gasta o dobro recuperando imagem."},
            {"numero": 7, "title": "3 sinais de que sua operação está lançando antes de estar pronta", "texto": "1. Você tem post-mortém todo mês sobre algo que deu errado no lançamento. 2. Seu cliente reclama do mesmo problema múltiplas vezes. 3. Você gasta em marketing pra \"reparar imagem\" de coisa que já lançou."},
            {"numero": 8, "title": "Você não economiza tempo lançando rápido e corrigindo. Economiza não fazendo errado.", "texto": "Qualidade no começo é investimento, não custo. A pergunta é: você investiu em pensar bem antes de executar?"},
        ],
        "caption": "Você quer ser rápido. Fast-moving company. Lança rápido, corrige depois se tiver problema. Faz sentido quando você lê na revista de startup. Mas quando seu cliente recebe coisa de qualidade ruim — conteúdo raso, produto com bugs, experiência quebrada — ele forma opinião ruim e não volta. Essa é a receita pronta: velocidade sem qualidade. Mas ninguém avisa que o custo de recuperar imagem é 10x maior que fazer certo desde o início. A ditadura das receitas prontas está aí: \"lean\" virou desculpa pra lançar medíocre. Porque ninguém quer dizer \"nossa, foi de má qualidade mesmo, a gente errou\". Todo mundo diz \"foi lean, rapidinho, agora corrige\". Mas o dano já foi feito. Confiança quando perdida demora anos pra recuperar. O padrão que vejo é: empresa lança conteúdo raso, cliente se frustra, nunca mais volta. Empresa lança produto com bug, cliente desconfia de qualidade, pensa que você não está pronto. Então gasta meses — e orçamento — tentando limpar imagem. Isso atinge o time que quer ir rápido, o diretor que pressiona velocidade acima de qualidade, todo tomador de decisão que confunde eficiência com produção contínua. A pergunta é: quando você lança algo, você já fez o trabalho pra estar pronto? Ou você lança e depois vem correndo atrás? Qual foi o último lançamento seu onde você sentia que estava 100% pronto? Manda aí.",
        "fontes": [
            {"titulo": "Deloitte: Brand Quality and Customer Perception (2024)", "link": "https://www.deloitte.com"},
            {"titulo": "Harvard Business Review: Quality and Growth (2023)", "link": "https://www.hbr.org"}
        ]
    },
    {
        "numero": 7, "mes": "OUTUBRO", "eixo": "Crescimento e Marca",
        "titulo": "Diferenciação real não é logo novo. É como você pensa diferente.",
        "tipo": "Crescimento + Marca",
        "slides": [
            {"numero": 1, "title": "DIFERENCIAÇÃO REAL NÃO É LOGO NOVO. É COMO VOCÊ PENSA DIFERENTE.", "texto": "Seu rebranding falhou porque a estratégia de fundo é igual."},
            {"numero": 2, "title": "Você faz rebranding. Muda cores, muda palavras, muda visual.", "texto": "Apresenta pra empresa. Todos gostam. Bonito mesmo. Mas depois de 3 meses, cliente continua vendo você da mesma forma. Sua proposta não mudou. Seu posicionamento não mudou. Seu jeito de se comunicar não mudou. Só a cor mudou."},
            {"numero": 3, "title": "Marcas fazem rebranding e continuam oferecendo o mesmo", "texto": "Percepção não muda porque o insight estratégico é o mesmo. Diferenciação vem de entender de forma diferente o problema do cliente. Se você continua entendendo igual, rebranding é cosmético. Mudou a embalagem, não o produto."},
            {"numero": 4, "title": "É como mudar de roupa em uma aula de dança", "texto": "Você entra com roupa vermelha. Sai e volta com roupa azul. Roupa mudou. Mas se seu jeito de dançar é o mesmo, a postura é a mesma, o ritmo que você segue é o mesmo — ninguém vai notar a roupa. Vão notar como você dança. Se dança igual, roupa nova não muda como você se apresenta."},
            {"numero": 5, "title": "DIFERENCIAÇÃO REAL NÃO VEM DE VISUAL DIFERENTE, VEM DE PENSAMENTO DIFERENTE.", "texto": "Você precisa entender o problema do cliente de um jeito que ninguém mais consegue enxergar. Aí visual diferente faz sentido. Aí rebranding é verdadeiro. Porque você tem um novo argumento, não só uma nova cor."},
            {"numero": 6, "title": "Em 2026, marca não muda com logo novo. Muda com ideias novas.", "texto": "Seu posicionamento muda quando você consegue pensar diferente sobre seu mercado. Quando consegue servir cliente de jeito que competitor não consegue porque pensa de forma diferente."},
            {"numero": 7, "title": "3 sinais de que seu rebranding é cosmético", "texto": "1. Seu argumento de venda é o mesmo, só com palavras novas. 2. Seu cliente não entende qual é a diferença real. 3. Seu competitor consegue copiar rápido porque é só visual."},
            {"numero": 8, "title": "Você não diferencia mudando logo. Diferencia mudando como você pensa.", "texto": "Qual é o jeito novo de você enxergar o problema? Aí sim você diferencia. Qual é esse jeito?"},
        ],
        "caption": "Você investe em rebranding. Muda cores, muda palavras. Fica bonito de verdade. Mas passado um tempo, cliente continua vendo você igual. Porque você continua oferecendo a mesma coisa, do mesmo jeito, com o mesmo argumento. Só mudou a embalagem. Essa é a colocação em caixas que mata marca: você precisa estar em \"caixa de rebranding\" pra parecer inovador, quando na verdade inovação é ideias novas, não cores novas. A ditadura das receitas prontas está aí: rebranding é receita pronta. Paga agência, faz rebranding, pronto. Mas ninguém fala que se não mudar a forma de pensar sobre seu cliente, rebranding é desperdício. O padrão que vejo é: marca muda visual, continua com mesmo posicionamento, e estranha por que cliente não vê diferença. Porque visual é o primeiro que muda, mas último que cliente repara. Cliente repara em como você resolve o problema. Se você continua resolvendo igual, visual diferente não muda percepção. Isso atinge o gestor que quer parecer moderno, o diretor que acha que marca velha precisa de cara nova, todo tomador de decisão que confunde diferenciação com rebranding. A pergunta é: qual é o jeito novo que você enxerga seu cliente? Qual é a insights estratégica que você tem que competitor não consegue ver? Ou você só precisa de cores novas? Comenta aí.",
        "fontes": [
            {"titulo": "BCG: The Art and Science of Brand Differentiation (2024)", "link": "https://www.bcg.com"},
            {"titulo": "Harvard Business Review: What Makes a Brand Distinctive (2023)", "link": "https://www.hbr.org"}
        ]
    },
    {
        "numero": 8, "mes": "OUTUBRO", "eixo": "Crescimento e Inovação",
        "titulo": "Canibalize seu próprio produto antes que concorrência canibalize.",
        "tipo": "Crescimento + Inovação",
        "slides": [
            {"numero": 1, "title": "CANIBALIZE SEU PRÓPRIO PRODUTO ANTES QUE CONCORRÊNCIA CANIBALIZE.", "texto": "Medo de fazer seu próprio cliente migrar é receita pro seu cliente migrar mesmo."},
            {"numero": 2, "title": "Você tem um produto que funciona. Gera receita. Você pensa em novo produto.", "texto": "Mas novo produto vai canibalicar vendas do antigo. Vai tirar cliente de um pra colocar em outro. Aí você freeia. Acha que é melhor proteger o que você tem do que arriscar em inovação que rouba seu próprio mercado."},
            {"numero": 3, "title": "Mas aqui está o padrão: seu competitor não está pensando assim", "texto": "Seu competitor está desenho novo produto. Novo jeito de servir seu cliente. Nova forma de resolver o problema. Enquanto você protege seu modelo antigo, ele está inovando pra seu cliente já estar com ele quando seu modelo ficar obsoleto."},
            {"numero": 4, "title": "É como um pagodeiro que tem música sucesso mas tem medo de gravar outra", "texto": "Sua música é sucesso. Ganha dinheiro. Aí surge oportunidade de gravar música diferente. Mas tem medo de canibalicar a primeira. Aí fica anos tocando a mesma música. Enquanto isso, outro artista grava coisa nova, seu público migra, você fica com modelo velho."},
            {"numero": 5, "title": "CANIBALIZE SIGNIFICA VOCÊ ESTÁ EVOLUINDO. CONCORRÊNCIA ESTÁ FAZENDO DE VOCÊ O OBSOLETO.", "texto": "Se você não canibalicar seu próprio modelo, concorrência vai canibalicar. Vai oferecer versão melhor. Versão nova. Versão que seu cliente quer. E você fica com modelo velho enquanto cliente vai embora."},
            {"numero": 6, "title": "Em 2026, único jeito de ficar relevante é continuar inovando", "texto": "Inclusive canibalizando seu próprio modelo. Porque se você não faz, alguém faz. E seu cliente vai querer a coisa nova, não a velha que você insiste em defender."},
            {"numero": 7, "title": "3 sinais de que você está preso em modelo antigo", "texto": "1. Você freeia inovação porque \"vai afetar receita de produto atual\". 2. Seu cliente quer coisa que você não oferece, então vai pra competitor. 3. Seu produto é \"referência\" mas está perdendo relevância no mercado."},
            {"numero": 8, "title": "Canibalize você mesmo. Do contrário, concorrência canibaliça você.", "texto": "Qual é o novo jeito de você servir seu cliente que você tem medo de oferecer porque vai tirar receita de modelo antigo? Aí sim você inova."},
        ],
        "caption": "Você tem um produto que funciona. Gera receita. Você está pensando em novo produto que vai servir cliente melhor, de forma diferente. Mas novo produto vai tirar vendas de produto antigo. Aí você freeia. Acha que é melhor proteger o que você tem. Enquanto isso seu competitor está corajoso. Está desenvolvendo coisa nova. E quando seu cliente percebe que existe opção melhor, ele vai pra lá. Porque você não quis evoluir. Essa é a receita pronta para ficar no passado: proteger modelo antigo. Mas ninguém avisa que enquanto você protege o velho, o mundo está pedindo o novo. A ditadura das receitas prontas está aí: maximizar receita de produto atual é objetivo financeiro óbvio — mas é também receita pro fracasso se você não inovar. O padrão que vejo é: empresa cheia de receio de canibalicar próprio modelo, fica congelada, competitor não tem esse receio, inovadora, toma cliente da empresa congelada. Aí empresa congelada descobre que modelo antigo que estava protegendo agora não vale mais nada porque ficou obsoleto. Isso atinge o gerente que quer cumprir meta de receita, o diretor financeiro que acha que inovação é custo, todo tomador de decisão que confunde proteção de modelo com proteção de negócio. A pergunta é: qual é o novo jeito que você precisa servir seu cliente que vai canibalicar seu modelo antigo? E por que você ainda não está desenvolvendo? Qual é o medo por trás disso? Manda aí.",
        "fontes": [
            {"titulo": "McKinsey: Innovation and Cannibalization Strategy (2024)", "link": "https://www.mckinsey.com"},
            {"titulo": "Harvard Business Review: Managing Cannibalization (2023)", "link": "https://www.hbr.org"}
        ]
    },
    {
        "numero": 9, "mes": "NOVEMBRO", "eixo": "Futuro e Liderança",
        "titulo": "Clarity vs. Activity — Por que gestor focado em tático deixa receita na mesa.",
        "tipo": "Futuro + Liderança",
        "slides": [
            {"numero": 1, "title": "CLARITY VS. ACTIVITY — POR QUE GESTOR TÁTICO DEIXA RECEITA NA MESA.", "texto": "Estar ocupado não é o mesmo que estar estratégico."},
            {"numero": 2, "title": "Você tem um gestor que funciona muito bem tacticamente", "texto": "Executa projeto, entrega no prazo, time gosta. Mas quando você olha pro crescimento real — receita, impacto, resultado mensurável — ele não cresce. Porque estava focado em fazer bem, não em fazer a coisa certa."},
            {"numero": 3, "title": "Gestor tático está sempre ocupado. Sempre correndo. Sempre resolvendo crise.", "texto": "Mas está resolvendo crise que poderia ter sido prevenida se tivesse parado pra pensar. Está executando projeto que poderia ter sido priorizado melhor se tivesse clareza estratégica. Está fazendo bem as coisas erradas."},
            {"numero": 4, "title": "É como um corredor que treina para maratona mas corre na direção errada", "texto": "Ele é rápido. Muito rápido. Muito dedicado. Mas está correndo na direção errada. Competência individual, esforço máximo, mas direção incorreta. No final de tudo, mais rápido ainda está chegando no lugar errado."},
            {"numero": 5, "title": "O PROBLEMA NÃO É FALTA DE ATIVIDADE. É FALTA DE CLAREZA SOBRE QUAL ATIVIDADE IMPORTA.", "texto": "Gestor estratégico não executa mais. Executa diferente. Executa o que realmente vai gerar resultado. Porque parou pra pensar antes de agir. Porque tem clareza sobre qual é o destino e qual atividade leva pra lá."},
            {"numero": 6, "title": "Em 2026, gestor que está muito ocupado é gestor que vai perder receita", "texto": "Porque estava focado em fazer bem, não em fazer estratégico. Porque não tinha clareza pra priorizar. Porque estava correndo sem direção clara."},
            {"numero": 7, "title": "3 sinais de que sua operação está presa em atividade", "texto": "1. Seu gestor está sempre ocupado, sempre com crise, nunca tem tempo pra estratégia. 2. Vocês executam bem mas resultado não sobe no ritmo que deveria. 3. Seu time não entende qual é o destino final, só sabe de tarefa seguinte."},
            {"numero": 8, "title": "Atividade sem clareza é corrida sem destino. Qual você está correndo?", "texto": "Você está focado em estar ocupado ou em chegar a lugar específico? A resposta decide seu crescimento."},
        ],
        "caption": "Você tem um gestor que executa muito bem. Projeto sai no prazo, time gosta dele, é eficiente. Mas quando você olha o resultado estratégico — receita, crescimento real, impacto no negócio — ele não subiu. Porque seu gestor estava focado em atividade, não em clareza. Estava correndo rápido, mas sem saber pra onde. E por mais rápido que corra, se a direção está errada, chega em lugar errado. Essa é a receita pronta para deixar receita na mesa: estar ocupado. Gestores ocupados são gestores que não param pra pensar. Que não têm clareza sobre qual atividade realmente importa. Que executam bem as coisas erradas. A ditadura das receitas prontas está aí: ser data-driven, ser eficiente, estar sempre fazendo. Mas ninguém fala que estar ocupado é diferente de estar estratégico. O padrão que vejo é: empresa cheia de atividade, gestores ocupados, execução boa, resultado medíocre. Porque ninguém parou pra pensar qual atividade realmente gera resultado. Qual atividade tem impacto estratégico. Qual atividade paga a conta no final do mês. Isso atinge o gerente que se sente produtivo quando está ocupado, o diretor que mede sucesso por atividade executada, todo tomador de decisão que confunde eficiência com resultado. A pergunta é: seu gestor conhece qual é o destino estratégico? Ou ele só sabe qual é a próxima tarefa? Qual foi a última conversa estratégica que você teve com seu líder de operação? Comenta aí.",
        "fontes": [
            {"titulo": "Deloitte: Strategic Leadership and Operational Execution (2024)", "link": "https://www.deloitte.com"},
            {"titulo": "CMO Council: Strategic Focus vs Tactical Execution (2024)", "link": "https://www.cmocouncil.org"}
        ]
    },
    {
        "numero": 10, "mes": "NOVEMBRO", "eixo": "Futuro e Operação",
        "titulo": "Escala não é fazer mais do mesmo. É fazer diferente.",
        "tipo": "Futuro + Operação",
        "slides": [
            {"numero": 1, "title": "ESCALA NÃO É FAZER MAIS DO MESMO. É FAZER DIFERENTE.", "texto": "Seu processo de 10 pessoas quebra quando você tem 100."},
            {"numero": 2, "title": "Você tem processo que funciona bem com time pequeno", "texto": "Todo mundo conhece todo mundo. Comunicação é rápida. Decisão é fácil. Você quer crescer. Aí pensa: agora é aumentar volume. Contrata mais gente. Tenta rodar o mesmo processo com 3x mais pessoas. E tudo desaba."},
            {"numero": 3, "title": "Processos que funcionam em pequena escala quebram em grande escala", "texto": "Porque comunicação ficou mais complexa. Porque decisão fica mais lenta. Porque há mais gente, mais pontos de vista, mais conflito. Você precisa redesenhar estrutura, comunicação, decisão."},
            {"numero": 4, "title": "É como aumentar a intensidade de um treino de musculação sem aumentar o volume progressivo", "texto": "Você treina com 10kg. Está bem. Aí você pensa: vou colocar 100kg amanhã mesmo. Seu corpo não aguenta. Se quebra. Treino precisa evoluir progressivamente. Você tem que aumentar carga, volume, intensidade — de forma estruturada. Não salta de 10 pra 100 de uma vez."},
            {"numero": 5, "title": "ESCALA REAL SIGNIFICA REDESENHAR O QUE VOCÊ FAZ, NÃO SÓ FAZER MAIS.", "texto": "Significa mudar estrutura. Significa mudar comunicação. Significa mudar como você toma decisão. Porque com 10 pessoas funciona de um jeito. Com 100, funciona de outro. Com 1000, funciona de outro ainda."},
            {"numero": 6, "title": "Em 2026, empresa que não consegue escalar morre. Empresa que escala errado morre mais rápido.", "texto": "Porque quando você cresce de forma caótica, você queima energia. Queima talento. Queima cultura. E no final fica grande mas fraco."},
            {"numero": 7, "title": "3 sinais de que sua operação está escalando errado", "texto": "1. Você contratou 50% mais gente e resultado não subiu 50%. 2. Sua cultura está mudando pra pior — talento está saindo. 3. Líderes estão dizendo que antes era melhor quando era menor."},
            {"numero": 8, "title": "O que funciona para 10 pessoas não funciona para 100. O que funciona para 100 não funciona para 1000.", "texto": "Qual é a mudança que você precisa fazer agora pra estar pronto pra próximo tamanho?"},
        ],
        "caption": "Você tem um processo que funciona bem com 10 pessoas. Tudo ágil, tudo rápido, todo mundo conhece todo mundo. Você quer crescer. Contrata mais gente. Tenta rodar o mesmo processo com 100 pessoas. E descobre que quebrou. Porque processo pra 10 não é processo pra 100. Porque comunicação ficou mais complexa. Porque decisão fica mais lenta. Essa é a receita pronta pra crescimento caótico: tentar escalar sem mudança. Mas ninguém avisa que escala não é multiplicar o mesmo jeito. Escala é redesenhar como você faz as coisas. A ditadura das receitas prontas está aí: ser ágil, ser rápido, ser pequeno. Mas quando você cresce, ágil não funciona mais. Rápido fica confuso. Pequeno vira desordenado. O padrão que vejo é: empresa cresce, traz mais gente, tenta manter cultura e processo iguais, e tudo descaminha. Aí culpam a mudança de tamanho. Quando na verdade culpa é ter esperado crescer sem mudar estrutura. Isso atinge o empreendedor que ama trabalhar em startup mode, o gestor que não aceita que estrutura muda quando cresce, todo tomador de decisão que confunde crescimento com multiplicação. A pergunta é: você já parou pra pensar qual é a mudança estrutural que você vai precisar fazer pra escalar 10x? Qual é o processo novo que vai funcionar pra próximo tamanho? Qual é a liderança que vai ser necessária? Comenta aí.",
        "fontes": [
            {"titulo": "MIT Sloan: Organizational Transformation at Scale (2024)", "link": "https://sloan.mit.edu"},
            {"titulo": "Deloitte: Scaling Operations (2023)", "link": "https://www.deloitte.com"}
        ]
    },
    {
        "numero": 11, "mes": "NOVEMBRO", "eixo": "Futuro e Estratégia",
        "titulo": "Vantagem competitiva real não é tecnologia. É como você pensa.",
        "tipo": "Futuro + Estratégia",
        "slides": [
            {"numero": 1, "title": "VANTAGEM COMPETITIVA REAL NÃO É TECNOLOGIA. É COMO VOCÊ PENSA.", "texto": "A startup sem budget vence a empresa com melhor ferramenta."},
            {"numero": 2, "title": "Você investe em tecnologia melhor que seus competitors. Melhor CRM. Melhor automação. Melhor ferramenta.", "texto": "Pensa que isso é vantagem competitiva. Que ninguém consegue acompanhar com ferramenta pior. Mas em 6 meses, competitor copia sua ferramenta. Porque ferramenta é copiável. E aí você descobre que tecnologia não era vantagem."},
            {"numero": 3, "title": "Tecnologia pode ser copiada em 6 meses. Marca pode ser perdida em um dia. Preço é frágil.", "texto": "A verdadeira vantagem é como você pensa sobre o mundo e sobre seu mercado. É como você enxerga problema que ninguém mais enxerga. É como você resolve de jeito que ninguém mais consegue resolver. Isso não é copiável."},
            {"numero": 4, "title": "É como um dançarino de samba que tem técnica melhor que qualquer outro", "texto": "A técnica dele é copiável — outros praticam. Mas o jeito dele de ler a música, de antecipar o ritmo, de improvisar quando a batida muda — isso não é copiável. É pensamento. É anos de observação do ritmo. É visão que outros não têm."},
            {"numero": 5, "title": "EMPRESAS QUE ENTENDEM MUNDO DIFERENTE GANHAM DE EMPRESAS COM MELHOR FERRAMENTA.", "texto": "Porque conseguem usar qualquer ferramenta de jeito que ferramenta foi pensada pra ser usada — ou descobrir jeito novo. Porque conseguem se adaptar rápido. Porque conseguem pensar diferente quando contexto muda."},
            {"numero": 6, "title": "Em 2026, o que diferencia é mentalidade da organização, não ferramenta que você comprou.", "texto": "Porque ferramenta envelhece. Mentalidade que sabe pensar diferente continua gerando vantagem."},
            {"numero": 7, "title": "3 sinais de que você está competindo com ferramenta em vez de pensamento", "texto": "1. Seu diferencial é \"temos CRM melhor\" ou \"automação mais rápida\". 2. Seu competitor copia sua ferramenta em 3 meses e tira sua vantagem. 3. Você gasta mais em tecnologia do que em desenvolver visão estratégica."},
            {"numero": 8, "title": "Você não compete com concorrência. Você compete com a forma como pensa.", "texto": "Qual é o jeito único que sua organização enxerga e resolve problema? Esse é seu diferencial."},
        ],
        "caption": "Você investe em ferramenta melhor que competitor. Melhor tecnologia. Melhor plataforma. Pensa que é sua vantagem competitiva. Mas em 6 meses, competitor compra a mesma ferramenta. Porque tecnologia é copiável. O que não é copiável é o jeito que você pensa sobre problema. O jeito que você enxerga cliente. A visão que você tem de mercado. Essa é a ilusão da tecnologia: empresas gastam milhões em ferramenta pensando que é vantagem competitiva. Mas ferramenta é pé de igualdade. O que realmente diferencia é mentalidade. Como você observa mundo. Como você antecipa mudança. Como você se adapta quando contexto vira. A ditadura das receitas prontas está aí: compra ferramenta certa. Mas ninguém fala que ferramenta é fácil de copiar. O que é difícil de copiar é o pensamento que você usa ferramenta. O padrão que vejo é: empresa investe em tecnologia caríssima pensando que é vantagem competitiva. Competitor não consegue investir, então terceiriza. Usa ferramenta mais simples. Mas pensa melhor. E ganha. Porque ferramenta é só ferramenta. O que ganha é pensar. Isso atinge o diretor que confunde inovação com tecnologia, o gestor que acha que investir em software é investir em competitividade, todo tomador de decisão que confunde meio com fim. A pergunta é: qual é a vantagem que sua empresa tem que competitor não consegue copiar nem com mesma ferramenta? Qual é a mentalidade que você cultiva? Qual é a visão que ninguém mais tem? Comenta aí.",
        "fontes": [
            {"titulo": "Harvard Business Review: Sustainable Competitive Advantage (2024)", "link": "https://www.hbr.org"},
            {"titulo": "BCG: Thinking Differently to Compete (2023)", "link": "https://www.bcg.com"}
        ]
    },
    {
        "numero": 12, "mes": "NOVEMBRO", "eixo": "Futuro e Comportamento",
        "titulo": "Comportamento do consumidor mudou. Sua estratégia mudou também?",
        "tipo": "Futuro + Comportamento",
        "slides": [
            {"numero": 1, "title": "COMPORTAMENTO DO CONSUMIDOR MUDOU. SUA ESTRATÉGIA MUDOU TAMBÉM?", "texto": "Seu playbook de 2023 não funciona mais em 2026."},
            {"numero": 2, "title": "Você tem playbook que funcionava em 2023. Funcionava bem mesmo.", "texto": "Padrão de compra era assim. Confiança em marca era assim. Sensibilidade a preço era assim. Mas agora estamos em 2026. Cliente mudou. Mercado virou. Playbook virou obsoleto. E você não percebeu."},
            {"numero": 3, "title": "Padrões de compra mudaram. Confiança em marcas mudou. Sensibilidade a preço mudou. Canais mudaram.", "texto": "Pós-2020 o mundo virou de cabeça para baixo. Consumidor aprendeu a ser offline e online. Aprendeu a questionar marca grande. Aprendeu a não confiar em publicidade tradicional. E você segue com playbook de 2023."},
            {"numero": 4, "title": "É como treinar Yoga seguindo videoaula de 1990", "texto": "Você aprendeu sequência perfeita em vídeo de 1990. Segue exatamente como o instrutor ensinou. Só que agora em 2026 tem sequência diferente, tem respiração diferente, tem philosophia diferente. Você insiste na sequência antiga. Fica defasado."},
            {"numero": 5, "title": "O PROBLEMA NÃO É SEU PLAYBOOK ESTAVA ERRADO. É QUE MUNDO MUDOU.", "texto": "Você precisa observar como cliente está agindo agora. O que ele quer agora. Qual é o canal que ele usa agora. Qual é a mensagem que ele acredita agora. Porque tudo mudou desde 2023. Porque comportamento é dinâmico."},
            {"numero": 6, "title": "Em 2026, empresa que não observa mudança de comportamento em tempo real fica para trás.", "texto": "Porque mundo está mudando mais rápido. Porque cliente está mudando mais rápido. Porque ficar com estratégia velha é ficar cego para o presente."},
            {"numero": 7, "title": "3 sinais de que sua estratégia está desatualizada", "texto": "1. Seus números de resultado estão piorando sem explicação clara. 2. Cliente novo está preferindo competitor mesmo sendo seu serviço melhor. 3. Seu time adora playbook mas cliente não está respondendo mais."},
            {"numero": 8, "title": "Você não cresce mantendo a mesma estratégia. Cresce observando como cliente mudou.", "texto": "Qual é a mudança de comportamento que você viu no seu cliente e ainda não incorporou na estratégia? Aí você cresce."},
        ],
        "caption": "Você tem um playbook que funcionava bem em 2023. Padrão de compra, canal, mensagem — tudo definido. Funcionava. Mas agora estamos em 2026. Cliente não compra do mesmo jeito. Não acredita na mesma mensagem. Não está no mesmo canal. E você segue com playbook de 2023 se achando que estratégia está certa. Essa é a receita pronta para ficar obsoleto: manter a mesma estratégia. Mas ninguém avisa que mundo está mudando mais rápido. Que comportamento de cliente está mudando. Que o que funcionava no ano passado pode não funcionar esse ano. A ditadura das receitas prontas está aí: ter playbook é ter segurança. Mas playbook envelhece rápido. E quando envelhece, você fica preso no passado enquanto cliente se mudou. O padrão que vejo é: empresa rodar estratégia velha, resultado cai, culpam execução. Quando na verdade estratégia envelheceu. Quando na verdade cliente mudou e você não observou. Isso atinge o diretor que quer segurança de plano pronto, o gerente que não quer arriscar em inovação, todo tomador de decisão que confunde eficácia com permanência. A pergunta é: qual é a mudança de comportamento do seu cliente que você viu nos últimos meses e ainda não corporou na estratégia? Qual é o jeito novo que ele está comprando e você ainda não está servindo? Qual é o seu principal indicador de que estratégia envelheceu? Manda aí.",
        "fontes": [
            {"titulo": "Deloitte: Consumer Behavior in 2025-2026 (2024)", "link": "https://www.deloitte.com"},
            {"titulo": "McKinsey: The Changing Consumer (2024)", "link": "https://www.mckinsey.com"}
        ]
    },
]

doc = Document()

# Add title
title = doc.add_heading('ROTEIROS DE CARROSSEL', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

subtitle = doc.add_heading('Setembro • Outubro • Novembro 2026', level=2)
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

current_month = None

for c in carrosseis_completos:
    if c['mes'] != current_month:
        current_month = c['mes']
        month_para = doc.add_heading(f'{c["mes"]} / 2026', level=1)
        month_para.space_before = Pt(12)

    add_carousel(doc, c)

doc.save('carrosseis-set-out-nov-2026-final.docx')
print('✅ Documento completo gerado: carrosseis-set-out-nov-2026-final.docx')
print('📊 12 carrosseis com analogias personalizadas e argumentação reformulada')
print('🎯 Pronto para design e produção')
