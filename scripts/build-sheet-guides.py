#!/usr/bin/env python3
"""
The technical pages — one per worksheet, for the clinician.

**The worksheets themselves are no longer bound into the workbook.** They live
in the child's exploration book, and a licence buys both files; printing them
twice only creates two copies that can fall out of step (D-194).

What the workbook carries instead is a page *about* each worksheet: what it is
for, how to run it, what to ask, what to be careful of, what to notice — and
space to write what happened when it was used, with the child identified by code
rather than by name.

Written here rather than by hand because there are nine of them per family and
sixty-three in total: the shape must be identical every time, and a table
written out sixty-three times drifts.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Every page has the same seven rows, in the same order. The order is the order
# a clinician needs them: what and for whom, then what to do, then what to
# watch, then what to be careful of.
FIELDS = ["Idade", "Base", "Objectivo", "Como aplicar", "A notar", "Cuidados"]

SHEETS = {}
DYNAMICS = {}

SHEETS["angry"] = [
    {
        "n": 1,
        "title": "A Zanga",
        "Idade": "6 aos 9 anos",
        "Base": "Psicoeducação. Sem nível de evidência próprio: reformula em "
                "linguagem infantil o que a secção 1 sustenta.",
        "Objectivo": "Dar à criança um enquadramento antes de lhe pedir seja o "
                     "que for. Três afirmações e um esquema; nada para preencher.",
        "Como aplicar": "Ler com ela, em voz alta, sem parar para perguntar. É a "
                        "única página do caderno que não faz perguntas.",
        "A notar": "Se alguma das três afirmações a surpreende. *A zanga não é "
                   "má* costuma ser a que provoca reacção — em crianças que já "
                   "ouviram o contrário muitas vezes.",
        "Cuidados": "Não transformar a leitura numa lição. Se ela quiser falar a "
                    "meio, a página fica onde está.",
        "questions": [
            "Já tinhas pensado que a zanga podia servir para alguma coisa?",
            "Alguma coisa aqui te parece diferente do que te costumam dizer?",
        ],
    },
    {
        "n": 2,
        "title": "O que acontece antes",
        "Idade": "7 aos 9 anos",
        "Base": "Comportamental — análise de antecedentes. **Estabelecido** "
                "quanto à ligação entre situação e resposta; a aplicação nesta "
                "forma é razoável.",
        "Objectivo": "Procurar o padrão que a criança ainda não vê. Não é "
                     "inventário: cinco linhas chegam.",
        "Como aplicar": "Uma linha de cada vez, sem ordem cronológica. Com "
                        "crianças mais novas, o adulto escreve enquanto ela "
                        "conta — que é o que acontece de facto numa sessão.",
        "A notar": "Se as linhas se parecem umas com as outras. **Um padrão que "
                   "se repete é o achado; cinco situações sem nada em comum "
                   "também é um achado, e diferente.**",
        "Cuidados": "Não corrigir a versão dela dos acontecimentos. O que "
                    "interessa aqui é o que ela viu, não o que se passou.",
        "questions": [
            "O que estava a acontecer mesmo antes?",
            "Onde é que estavas? Quem é que lá estava?",
            "O que é que o corpo fez primeiro?",
            "Olha para as cinco: há alguma coisa parecida?",
        ],
    },
    {
        "n": 3,
        "title": "A Zanga vem visitar",
        "Idade": "4 aos 7 anos",
        "Base": "Externalização, terapia narrativa. **Prática** — muito usada "
                "com crianças, com pouca investigação controlada.",
        "Objectivo": "Separar a criança do problema. A diferença é gramatical e "
                     "é toda: não *estou zangada*, mas *a Zanga veio*.",
        "Como aplicar": "Dar a folha e o lápis e dizer pouco. O desenho é dela; "
                        "as perguntas vêm depois de estar feito.",
        "A notar": "Se a Zanga desenhada é assustadora ou engraçada. As duas "
                   "coisas são úteis e dizem coisas diferentes. Reparar também "
                   "no tamanho relativo — uma Zanga que enche a moldura não é o "
                   "mesmo que uma que cabe num canto.",
        "Cuidados": "**Externalizar não é responsabilizar a Zanga pelo que a "
                    "criança fez.** Se ela disser *foi a Zanga que bateu*, a "
                    "resposta é que a Zanga apareceu **e** a mão foi dela.",
        "questions": [
            "De que tamanho é? De que cor?",
            "Faz barulho?",
            "Como é que sabes que ela está a chegar?",
            "O que é que a faz ir embora?",
            "Ela vem mais a alguns sítios do que a outros?",
        ],
    },
    {
        "n": 4,
        "title": "As palavras finas",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário emocional. **Razoável** quanto ao valor de "
                "distinguir estados; a lista é do material e é por língua.",
        "Objectivo": "Apresentar as três palavras juntas e ligar cada uma a um "
                     "momento real.",
        "Como aplicar": "As três cartas ficam à vista. Um momento por caixa, "
                        "escrito, desenhado ou assinalado.",
        "A notar": "Se as três situações são com a mesma pessoa. E se alguma "
                   "caixa fica vazia — a palavra que falta diz alguma coisa.",
        "Cuidados": "**A seta não é uma escala.** Diz que a zanga às vezes passa "
                    "de uma palavra para outra; não pede à criança que se "
                    "classifique. Se ela começar a graduar-se, voltar ao nome.",
        "questions": [
            "Qual destas dizes mais vezes? Em casa e na escola.",
            "Há alguma que nunca disseste em voz alta?",
            "Alguém em tua casa usa alguma destas palavras?",
        ],
    },
    {
        "n": 5,
        "title": "Chateado",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário emocional, específico do português europeu. "
                "**Prática.**",
        "Objectivo": "Desambiguar. *Chateado* serve para zanga leve, para "
                     "tristeza e para tédio, e a criança que o diz pode estar em "
                     "qualquer uma das três.",
        "Como aplicar": "As três cartas-mãe à frente dela — zangado, triste, "
                        "aborrecido. Primeiro a última vez que disse; depois uma "
                        "vez em que foi outra.",
        "A notar": "Se escolhe sempre a mesma. **Uma criança que usa *chateado* "
                   "só para tristeza tem menos vocabulário de zanga do que "
                   "parecia; uma que o usa só para zanga pode não estar a nomear "
                   "a tristeza de todo.**",
        "Cuidados": "Não sugerir qual das três era. A escolha tem de ser dela, "
                    "ou a ficha mede a nossa hipótese.",
        "questions": [
            "Quando dizes chateada, o que é que costuma ter acontecido?",
            "Há vezes em que dizes chateada e por dentro estás triste?",
            "É mais com alguém ou com alguma coisa?",
        ],
    },
    {
        "n": 6,
        "title": "Irritado",
        "Idade": "7 aos 9 anos",
        "Base": "Comportamental — identificação de gatilhos repetidos. "
                "**Razoável.**",
        "Objectivo": "Encontrar o que se repete. A irritação costuma ter um "
                     "alvo próximo e recorrente.",
        "Como aplicar": "Três perguntas curtas: o que irrita quase sempre, onde "
                        "acontece mais, o que já ajudou.",
        "A notar": "**Se nomeia sempre a mesma pessoa, isso é o achado**, e muda "
                   "a conversa seguinte — com ela e provavelmente com quem a traz.",
        "Cuidados": "Se o alvo repetido for um adulto de casa, a ficha passa a "
                    "ser material de sessão e não de trabalho para casa.",
        "questions": [
            "O que é que te irrita quase sempre?",
            "Acontece mais em casa ou na escola?",
            "É sempre com a mesma pessoa?",
            "Há alguma coisa que já tenhas experimentado e que ajudou?",
        ],
    },
    {
        "n": 7,
        "title": "Furioso",
        "Idade": "7 aos 9 anos",
        "Base": "Narrativo. **Prática.**",
        "Objectivo": "Trabalhar o depois, não o tamanho. A criança usa esta "
                     "palavra para pedir que se leve a sério.",
        "Como aplicar": "Uma vez contada, quem percebeu, o que aconteceu quando "
                        "passou.",
        "A notar": "**Se alguém percebeu.** Uma criança que diz que ninguém "
                   "percebeu está a dizer duas coisas ao mesmo tempo.",
        "Cuidados": "Não pedir a intensidade nem comparar com as outras duas "
                    "palavras. A pergunta útil é o que se seguiu.",
        "questions": [
            "Consegues contar-me uma vez em que estiveste furiosa?",
            "Alguém percebeu que era mesmo grande? Quem?",
            "O que aconteceu depois de passar?",
        ],
    },
    {
        "n": 8,
        "title": "Da próxima vez",
        "Idade": "6 aos 9 anos",
        "Base": "Resolução de problemas. **Das mais bem estudadas** para "
                "dificuldades de comportamento nesta idade — gerar alternativas "
                "e escolher uma.",
        "Objectivo": "Escolher uma resposta a experimentar, e registar depois "
                     "como correu.",
        "Como aplicar": "Duas partes, em momentos diferentes: a escolha na "
                        "sessão, o resultado depois de experimentar.",
        "A notar": "**Se escolhe uma das cinco ou inventa outra.** Uma ideia "
                   "dela vale mais do que qualquer uma das nossas: é a única que "
                   "já vem com a situação dela dentro.",
        "Cuidados": "**Nunca perguntar *o que é que devias ter feito*.** É uma "
                    "repreensão disfarçada de ficha, e a criança percebe à "
                    "primeira. A pergunta é para a frente. Também não é "
                    "reavaliação cognitiva — é o que faz a seguir, não olhar "
                    "para a situação de outra maneira.",
        "questions": [
            "Da próxima vez, o que queres experimentar?",
            "Achas que dá para fazer isso onde costuma acontecer?",
            "Precisas de alguém para te ajudar a fazer isso?",
        ],
    },
    {
        "n": 9,
        "title": "Compor as coisas",
        "Idade": "6 aos 9 anos",
        "Base": "Reparação. **Prática**, com apoio indirecto: é o que a "
                "distinção entre culpa e vergonha prevê.",
        "Objectivo": "Escolher o que dizer a quem ficou magoado, e prever o caso "
                     "de a outra pessoa não querer ouvir já.",
        "Como aplicar": "**Não no dia.** Enquanto a activação desce, compor ainda "
                        "não é possível. É material para a sessão seguinte.",
        "A notar": "Se escreve sobre o que fez ou sobre o que sentiu. **Uma "
                   "criança que só consegue explicar-se ainda não chegou à outra "
                   "pessoa** — e isso é informação, não falha.",
        "Cuidados": "**A palavra *desculpa* não aparece na ficha, e não deve ser "
                    "sugerida.** Um pedido de desculpa mandado produz "
                    "obediência, não reparação.",
        "questions": [
            "O que queres dizer a essa pessoa?",
            "E se ela não quiser falar já, o que podes dizer mais tarde?",
            "Há alguma coisa que queiras fazer em vez de dizer?",
        ],
    },
]


DYNAMICS["angry"] = {1: [('4–6', '**A carta e o espelho.** Pôr a carta do zangado ao lado do espelho da primeira página e perguntar se são parecidos. Serve para ligar a personagem a ela própria sem ter de o dizer.'), ('6–8', '**Ler ao contrário.** Ler as três frases e perguntar, a cada uma, se alguém em casa diria o contrário. Traz o discurso da família para a sala sem perguntar pela família.'), ('8–9', '**Explicar a outra pessoa.** Pedir que explique a curva a um adulto presente, por palavras dela. Quem explica percebe melhor do que quem ouve.'), ('qualquer', '**Guardar para o fim.** Reler esta página na última sessão da família e perguntar se mudou alguma coisa.')], 2: [('6–8', '**Só desenhos.** O adulto escreve as colunas e a criança desenha uma cara ou um sítio em cada linha. A tabela funciona sem uma palavra.'), ('7–9', '**Ordenar por facilidade.** Depois de preenchida, pedir que aponte a linha mais fácil de contar e a mais difícil. É informação sobre ela, não sobre as situações.'), ('8–9', '**A linha que falta.** Perguntar se há uma situação que não escreveu. A que fica de fora costuma ser a que interessa.'), ('com a família', '**A mesma tabela pelos pais.** Cada um preenche a sua e comparam-se. As diferenças são o material da conversa.')], 3: [('4–6', '**Dar-lhe voz.** Perguntar o que a Zanga diria se pudesse falar, e escrever isso ao lado do desenho.'), ('4–7', '**Onde é que ela mora.** Pedir que desenhe onde a Zanga fica quando não está com ela. Externaliza um passo mais.'), ('6–8', '**A Zanga de outra pessoa.** Pedir que desenhe a Zanga de um adulto da casa. Costuma dizer mais do que a dela.'), ('7–9', '**O que a Zanga quer.** Perguntar o que a Zanga está a tentar conseguir. Aproxima da função sem usar a palavra.')], 4: [('7–9', '**Ordenar por frequência.** Pôr as três cartas da mais dita à menos dita. Não é intensidade: é uso.'), ('7–9', '**Uma semana a marcar.** Levar as três cartas e assinalar a que usou cada dia. Voltar com o registo.'), ('8–9', '**As palavras dos outros.** Perguntar qual das três usaria a mãe, o pai, o professor. Mapeia o vocabulário da casa.'), ('com a família', '**Cada um escolhe a sua.** Os adultos escolhem também, e dizem uma vez em que a sentiram.')], 5: [('7–9', '**Três montes.** Escrever cinco situações em papéis e pedir que as distribua pelas três cartas-mãe. Mostra-lhe a ambiguidade sem lha explicar.'), ('7–9', '**Trocar a palavra.** Escolher uma situação e procurar outra palavra que sirva melhor que *chateado*.'), ('8–9', '**Quando é que não serve.** Perguntar se há vezes em que dizer chateada não chega. Abre para as outras duas.'), ('com a família', '**O que ouvem quando ela diz.** Perguntar aos adultos o que percebem quando ela diz chateada. Muitas vezes percebem a errada.')], 6: [('7–9', '**O mapa do dia.** Marcar numa linha do dia as horas em que a irritação costuma aparecer. Costuma haver duas.'), ('7–9', '**O que muda quando muda.** Procurar uma vez em que aquilo que costuma irritar não irritou, e ver o que estava diferente.'), ('8–9', '**Três coisas que já tentou.** Listar e classificar cada uma como *ajudou*, *não ajudou*, *não sei*.'), ('com a família', '**Combinar um sinal.** Escolher com os adultos um gesto que ela possa fazer antes de a irritação crescer.')], 7: [('6–8', '**Desenhar o depois.** Em vez de contar a vez, desenhar o momento em que já tinha passado.'), ('7–9', '**Quem estava lá.** Marcar na folha quem estava presente e quem percebeu. Nem sempre são os mesmos.'), ('8–9', '**A versão do outro.** Contar a mesma vez do ponto de vista de quem lá estava. Exigente, e só quando a relação já aguenta.'), ('com a família', '**O que fizeram a seguir.** Perguntar aos adultos o que fizeram quando passou, não durante.')], 8: [('6–8', '**Experimentar na sala.** Fazer ali mesmo a estratégia escolhida, sem estar zangada. Ensaiar a frio é metade do trabalho.'), ('6–9', '**Onde é que dá.** Verificar se a estratégia escolhida é possível na escola, no carro, na sala de aula. Muitas não são.'), ('8–9', '**Plano B.** Escolher uma segunda para quando a primeira não der.'), ('com a família', '**Combinar quem ajuda.** Se a estratégia é *ir ter com alguém*, essa pessoa tem de saber que foi escolhida.')], 9: [('6–8', '**Ensaiar em voz alta.** Dizer o que escreveu no balão, à colega, antes de dizer a quem é.'), ('6–9', '**Reparar sem falar.** Procurar uma coisa que se faça em vez de se dizer. Para crianças a quem as palavras custam.'), ('8–9', '**Se correr mal.** Preparar o que fazer se a outra pessoa não aceitar. Evita que uma tentativa falhada feche o assunto.'), ('com a família', '**Os adultos também compõem.** Perguntar se algum deles se lembra de ter composto alguma coisa com ela.')]}


def page(family, sheet):
    rows = "\n".join(f"| **{f}** | {sheet[f]} |" for f in FIELDS)
    questions = "\n".join(f"- {q}" for q in sheet["questions"])
    # Dynamics that grow out of this sheet, banded by age. The general ones stay
    # in section 6; these are what the sheet itself opens up (D-197).
    dynamics = "\n".join(
        f"| {band} | {text} |" for band, text in DYNAMICS[family][sheet["n"]]
    )
    return f"""<div class="guide" markdown="1">

### Ficha {sheet['n']} — {sheet['title']}

| Orientação | |
| --- | --- |
{rows}

**Questões de exploração**

{questions}

**Dinâmicas a partir desta ficha**

| | |
| --- | --- |
{dynamics}

<div class="record" markdown="1">

| Aplicação | |
| --- | --- |
| Código / processo | |
| Idade | |
| Data | |

| Registo da sessão |
| --- |
| |
| |
| |

</div>

</div>

"""


def build(family: str = "angry") -> str:
    if family not in SHEETS:
        raise SystemExit(f"unknown family: {family}")
    body = "".join(page(family, s) for s in SHEETS[family])
    return f"""## 9. Fichas — orientação de aplicação

Uma página por ficha. **As fichas em si não estão aqui**: vivem no caderno de
exploração da criança, e uma licença dá acesso aos dois ficheiros — imprimi-las
duas vezes só produz duas cópias que podem ficar desencontradas.

Cada página diz para que serve a ficha, como se aplica, o que perguntar, o que
notar e o que evitar, e tem espaço para o registo da sessão em que foi usada.
**Por código, nunca por nome.**

{body}"""




# ---------------------------------------------------------------------------
# Triste — ten sheets (D-222, D-233).
#
# The three moulds anger uses and this family does not: externalising, *da
# próxima vez*, and repair. What replaces the last of them is *o que eu posso
# pedir*, because a family that ends in description tells the child there is
# nothing she can do.
# ---------------------------------------------------------------------------

SHEETS["sad"] = [
    {
        "n": 1,
        "title": "A Tristeza",
        "Idade": "6 aos 9 anos",
        "Base": "Psicoeducação. Sem nível de evidência próprio: reformula em "
                "linguagem infantil o que a secção 1 sustenta.",
        "Objectivo": "Dar-lhe um enquadramento antes de lhe pedir seja o que "
                     "for. Três afirmações e o esquema; nada para preencher.",
        "Como aplicar": "Ler com ela, em voz alta, sem parar para perguntar. É a "
                        "única página do caderno que não faz perguntas.",
        "A notar": "Qual das três a surpreende. **A tristeza não é má** costuma "
                   "ser a que provoca reacção; *não passa por a empurrarmos* "
                   "costuma ser a que alivia, sobretudo em crianças que já "
                   "tentaram e acham que falharam.",
        "Cuidados": "Não transformar a leitura numa lição. E não acrescentar "
                    "*mas vai passar* — a página já o diz, e repeti-lo com "
                    "ênfase é o consolo a virar animação.",
        "questions": [
            "Já tinhas pensado que a tristeza podia servir para alguma coisa?",
            "Alguma coisa aqui te parece diferente do que te costumam dizer?",
        ],
    },
    {
        "n": 2,
        "title": "Quando é que ela aparece",
        "Idade": "5 aos 8 anos",
        "Base": "Comportamental — padrão temporal. **Estabelecido** quanto à "
                "ligação entre contexto e resposta; esta aplicação é razoável.",
        "Objectivo": "Procurar as alturas que se repetem. **Não procura causas**: "
                     "procura horas, sítios e transições.",
        "Como aplicar": "Uma linha de cada vez. Com crianças mais novas o adulto "
                        "escreve enquanto ela conta. Se ela começar a explicar "
                        "porquê, deixar — mas não perguntar.",
        "A notar": "Se as alturas se agrupam. O deitar, o domingo à tarde, a "
                   "saída da escola e as transições entre casas são as mais "
                   "frequentes, e cada uma leva a conversa a um sítio diferente.",
        "Cuidados": "**Nunca perguntar *porque é que estavas triste*.** Uma "
                    "criança que não sabe inventa uma causa para satisfazer quem "
                    "perguntou, e a partir daí passa a repeti-la.",
        "questions": [
            "Há alguma altura do dia em que aparece mais?",
            "E algum dia da semana?",
            "O que estava a acontecer mesmo antes?",
        ],
    },
    {
        "n": 3,
        "title": "O que me faz companhia",
        "Idade": "4 aos 7 anos",
        "Base": "Co-regulação e objecto de conforto. **Base estabelecida** para a "
                "primeira, **razoável** para o objecto, prática para a forma "
                "concreta de cada uma.",
        "Objectivo": "Descobrir o que a acompanha — não o que a anima. As seis "
                     "figuras são as mesmas que ela viu no ecrã.",
        "Como aplicar": "Pôr as seis à frente e deixar assinalar quantas quiser. "
                        "A caixa do fim é para a dela, e vale mais do que as "
                        "seis nossas.",
        "A notar": "Quantas precisam de outra pessoa. Uma criança que só escolhe "
                   "as que não dependem de ninguém está a dizer alguma coisa "
                   "sobre quem tem disponível — e uma que só escolhe as que "
                   "dependem também.",
        "Cuidados": "**Nenhuma escolha é melhor do que outra**, e a manta não é "
                    "um consolo menor do que a mãe. Se ela não escolher nenhuma, "
                    "isso é resposta e não recusa.",
        "questions": [
            "Qual destas já usas sem ninguém te dizer?",
            "Há alguma que gostavas e que não dá para ter?",
            "Há alguma tua que não esteja aqui?",
        ],
    },
    {
        "n": 4,
        "title": "O que as pessoas dizem",
        "Idade": "7 aos 9 anos",
        "Base": "Princípios de interacção pais-criança. **Estabelecido** quanto "
                "ao efeito da resposta do adulto; esta aplicação é razoável.",
        "Objectivo": "Tornar a distinção concreta: separar o que ajuda do que "
                     "não ajuda, e chegar ao que ela gostava de ouvir e ninguém "
                     "diz.",
        "Como aplicar": "As duas primeiras caixas existem para tornar a terceira "
                        "perguntável. Não apressar a terceira.",
        "A notar": "**Se aparecer uma frase que também é sua, isso é o material a "
                   "funcionar.** Não a defender, não explicar a intenção — "
                   "anotar e usar depois.",
        "Cuidados": "**Esta folha vai para casa com ela.** É quem aplica que "
                    "decide o que sai da sala; se houver risco de a frase chegar "
                    "à pessoa descrita e isso ser mau para ela, a folha fica no "
                    "processo e faz-se a dinâmica falada.",
        "questions": [
            "Quem é que diz a coisa que ajuda?",
            "E a que não ajuda — achas que essa pessoa sabe?",
            "Se pudesses ensinar-lhes uma frase, qual era?",
        ],
    },
    {
        "n": 5,
        "title": "As palavras finas",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário emocional. **Razoável** quanto a diferenciação "
                "emocional; o conjunto concreto é do ColorHugs.",
        "Objectivo": "Pôr as quatro à frente e ver quais reconhece. **Não são "
                     "graus** — são coisas diferentes, e a ficha diz-lho.",
        "Como aplicar": "Uma caixa por palavra, sem ordem. Se uma ficar vazia, "
                        "deixá-la vazia.",
        "A notar": "Qual fica por preencher. E se usa *sozinho* para tudo — é a "
                   "palavra mais larga das quatro.",
        "Cuidados": "**Não ordenar por tamanho**, nem sugeri-lo. Nesta família a "
                    "ordenação por intensidade nem sequer faz sentido, e "
                    "propô-la ensinaria uma coisa falsa sobre as palavras.",
        "questions": [
            "Qual destas dizes mais vezes?",
            "Há alguma que nunca tinhas ouvido?",
            "Alguma delas é de uma pessoa em concreto?",
        ],
    },
    {
        "n": 6,
        "title": "Desiludido",
        "Idade": "7 aos 9 anos",
        "Base": "Comportamental — expectativa e resultado. **Prática** nesta "
                "forma.",
        "Objectivo": "Ver a desilusão como distância entre o que se esperava e o "
                     "que houve, e não como uma tristeza mais pequena.",
        "Como aplicar": "As duas primeiras caixas juntas, e só depois a terceira. "
                        "A terceira é a que interessa.",
        "A notar": "**Se alguém prometeu ou se foi ela que pensou.** Uma criança "
                   "que se desilude muitas vezes ou espera de mais, ou vive com "
                   "alguém que promete de mais — e são coisas diferentes.",
        "Cuidados": "Não corrigir a expectativa. *Também não era assim tão certo* "
                    "é uma repreensão com outro nome.",
        "questions": [
            "O que é que tu achavas que ia acontecer?",
            "Já aconteceu com a mesma pessoa mais do que uma vez?",
            "Como é que soubeste que não ia ser?",
        ],
    },
    {
        "n": 7,
        "title": "Sozinho",
        "Idade": "6 aos 9 anos",
        "Base": "Apoio social. **Razoável** quanto à ligação entre isolamento "
                "percebido e sofrimento; a aplicação é prática.",
        "Objectivo": "Separar as duas coisas que a palavra junta: estar sem "
                     "ninguém, e sentir-se só estando lá gente.",
        "Como aplicar": "A segunda caixa é a que faz o trabalho. Perguntar "
                        "**estava lá gente?** e esperar.",
        "A notar": "**Se ela se sente assim com gente à volta, é outra coisa e é "
                   "mais pesada.** Uma criança que só se sente sozinha quando "
                   "está mesmo sozinha está numa situação muito diferente.",
        "Cuidados": "Não tranquilizar com factos — *mas tu tens a tua irmã* fecha "
                    "a conversa e ensina que aquilo não se diz. Receber "
                    "primeiro, verificar depois.",
        "questions": [
            "Onde é que te sentes assim? E quando?",
            "Estava lá gente nessas alturas?",
            "Há algum sítio onde nunca te sentes assim?",
        ],
    },
    {
        "n": 8,
        "title": "Com saudades",
        "Idade": "4 aos 7 anos",
        "Base": "Representação de quem está ausente. **Prática**, com apoio "
                "indirecto na literatura sobre separação e vinculação.",
        "Objectivo": "Dar lugar à única palavra da família que não é inteiramente "
                     "má, e ver de quem ou de quê.",
        "Como aplicar": "É de desenhar, não de escrever. As perguntas por baixo "
                        "fazem-se depois do desenho, nunca antes.",
        "A notar": "**Se é de uma pessoa, de um sítio ou de um tempo.** Uma "
                   "criança com saudades de uma versão da própria família que já "
                   "não existe está a dizer outra coisa — é frequente depois de "
                   "uma separação, de uma mudança ou de um nascimento.",
        "Cuidados": "**Não assumir luto.** A mesma figura serve para uma avó que "
                    "mudou de casa e para uma avó que morreu, e o desenho não "
                    "decide qual. Se for luto, esta ficha não chega.",
        "questions": [
            "De quem, ou de quê?",
            "Ter saudades faz-te sentir bem ou mal? Ou as duas coisas?",
            "Quando é que te lembras mais?",
        ],
    },
    {
        "n": 9,
        "title": "Magoado",
        "Idade": "7 aos 9 anos",
        "Base": "Sistémica. **Prática** nesta forma.",
        "Objectivo": "É a única das quatro palavras que aponta para outra pessoa. "
                     "A ficha procura quem, e se essa pessoa sabe.",
        "Como aplicar": "A terceira caixa — o que lhe diria — fica por dizer. "
                        "**Não é a ficha da reparação**: aqui não há nada que ela "
                        "tenha de compor.",
        "A notar": "**Uma criança que diz que a pessoa não sabe está a dizer duas "
                   "coisas ao mesmo tempo**: que foi magoada, e que não conseguiu "
                   "dizê-lo. A segunda é geralmente a que se trabalha.",
        "Cuidados": "Não passar daqui para uma conversa entre as duas pessoas "
                    "sem preparação. E atenção a quem é nomeado: se for alguém "
                    "de casa, a folha pode não dever sair da sala.",
        "questions": [
            "Essa pessoa sabe que te magoou?",
            "Foi a fazer de propósito, ou achas que não deu por isso?",
            "Se pudesses dizer-lhe uma coisa, o que era?",
        ],
    },
    {
        "n": 10,
        "title": "O que eu posso pedir",
        "Idade": "6 aos 9 anos",
        "Base": "Comunicação de necessidades e procura de ajuda. **Prática** — "
                "a companhia assenta em terreno firme, o pedir não.",
        "Objectivo": "Fechar a distância entre o que ela descobriu na ficha 3 e o "
                     "que ela recebe. **É o que esta família tem em vez de *da "
                     "próxima vez*.**",
        "Como aplicar": "Depois da ficha 3, nunca antes — não há o que pedir sem "
                        "saber primeiro o que ajuda. Ensaiar a frase em voz alta "
                        "na sala.",
        "A notar": "A quem pede. E se a terceira caixa fica vazia: uma criança "
                   "que não consegue imaginar a recusa é a que mais precisa de a "
                   "ter preparada.",
        "Cuidados": "**A terceira caixa não é opcional.** Sem ela a ficha prepara "
                    "uma recusa que a criança vai ler como rejeição. Um pedido "
                    "recusado não é um pedido falhado — é um pedido com outro "
                    "tempo. E não prometer que pedir faz passar.",
        "questions": [
            "O que é que queres pedir, e a quem?",
            "Achas que essa pessoa sabe que isso te ajuda?",
            "E se ela não puder nessa altura, o que fazes?",
        ],
    },
]

DYNAMICS["sad"] = {
    1: [
        ("4–6", "**A carta e o espelho.** Pôr a carta do triste ao lado do espelho da primeira página e perguntar se são parecidos. Liga a personagem a ela própria sem o dizer."),
        ("6–8", "**Tapar uma linha.** Tapar a linha *com companhia* e perguntar o que acha que muda quando alguém está ao pé. Descobre-o em vez de o ler."),
        ("8–9", "**Explicar a outra pessoa.** Pedir que explique o esquema a um adulto presente, por palavras dela."),
        ("qualquer", "**Guardar para o fim.** Reler esta página na última sessão da família e perguntar se mudou alguma coisa."),
    ],
    2: [
        ("5–7", "**A linha do dia.** Desenhar o dia numa tira de papel e marcar com um traço as horas em que aparece. Funciona sem escrever nada."),
        ("6–8", "**A semana em cartões.** Sete cartões, um por dia, e assinalar os dias em que apareceu. Sem contagem e sem soma."),
        ("8–9", "**O dia em que não apareceu.** Procurar um dia em que não apareceu e ver o que estava diferente. Costuma render mais do que os outros."),
        ("com a família", "**A mesma tabela pelos adultos.** Cada um marca as alturas em que acha que ela fica triste. As diferenças são o material."),
    ],
    3: [
        ("4–6", "**As seis em cima da mesa.** Imprimir as seis páginas e deixá-la pegar, sem dizer nada. Muitas escolhem antes de haver pergunta."),
        ("4–7", "**Trazer a coisa.** Pedir que traga na próxima sessão a coisa macia, se existir. Muda o que se pode dizer a seguir."),
        ("6–9", "**Depende de quem.** Separar as figuras em duas pilhas: as que precisam de outra pessoa e as que não. Contar as pilhas com ela."),
        ("com a família", "**Os adultos adivinham.** Pedir-lhes que escolham as que acham que são dela, antes de verem as escolhas. A diferença é a conversa."),
    ],
    4: [
        ("7–9", "**Ensaiar a frase.** Dizer em voz alta a frase que ela gostava de ouvir, dita por si. Ouvi-la dita muda-a."),
        ("7–9", "**Quem diz o quê.** Escrever ao lado de cada frase quem a costuma dizer. Mapeia a casa sem perguntar pela casa."),
        ("8–9", "**A intenção e o efeito.** Perguntar se acha que a pessoa quis ajudar. Separar as duas coisas protege a relação."),
        ("com a família", "**A frase entregue.** Se ela quiser, dizer aos adultos a frase que gostava de ouvir. **Só se ela quiser, e nunca por decisão nossa.**"),
    ],
    5: [
        ("7–9", "**Por quem lá está.** Separar as quatro em duas pilhas: as que acontecem com gente à volta e as que acontecem sozinha."),
        ("7–9", "**A que custa mais dizer.** Escolher a que custa mais admitir em voz alta, e falar só dessa."),
        ("8–9", "**As palavras dos outros.** Perguntar qual das quatro usaria a mãe, o pai, o professor."),
        ("com a família", "**Cada um escolhe a sua.** Os adultos escolhem também, e contam uma vez em que a sentiram."),
    ],
    6: [
        ("7–9", "**Duas colunas.** O que eu esperava, o que houve — em duas colunas lado a lado. A distância fica visível."),
        ("7–9", "**Quem prometeu.** Marcar, em três desilusões, se alguém prometeu ou se foi ela que pensou. O padrão aparece depressa."),
        ("8–9", "**A desilusão pequena.** Procurar uma que já não lhe faz diferença nenhuma. Mostra-lhe que passam, sem lho dizermos."),
        ("com a família", "**As promessas em casa.** Perguntar aos adultos que promessas costumam fazer sobre tempo e disponibilidade. Sem acusação — é informação."),
    ],
    7: [
        ("6–8", "**Dois desenhos.** Desenhar duas vezes em que se sentiu sozinha: uma com gente à volta e outra sem. Se só conseguir uma, isso é a resposta."),
        ("6–9", "**O mapa dos sítios.** Marcar numa planta grosseira da casa e da escola onde é que aparece."),
        ("8–9", "**Quem é que sabe.** Perguntar se alguém sabe que ela se sente assim. É a pergunta que mais rende desta ficha."),
        ("com a família", "**O recreio.** Perguntar aos adultos o que sabem sobre os intervalos dela. Costumam não saber, e é onde isto vive."),
    ],
    8: [
        ("4–6", "**A caixa das saudades.** Uma caixa onde põe coisas que lhe lembram essa pessoa. Leva-a para casa."),
        ("4–7", "**Mandar sem enviar.** Desenhar uma coisa para essa pessoa, mesmo que não se envie. O desenho basta-se."),
        ("6–9", "**Pessoa, sítio ou tempo.** Perguntar as três e ver qual escolhe. É a pergunta clínica desta ficha."),
        ("com a família", "**As saudades dos adultos.** Perguntar-lhes de que têm saudades. Uma criança que percebe que também eles têm carrega menos sozinha."),
    ],
    9: [
        ("7–9", "**Sabe ou não sabe.** Duas colunas com as pessoas que magoaram: as que sabem e as que não. A segunda coluna é o trabalho."),
        ("7–9", "**A carta que não se envia.** Escrever ou desenhar o que diria, sem o entregar."),
        ("8–9", "**A versão do outro.** Contar a mesma vez do ponto de vista da outra pessoa. **Exigente, e só quando a relação já aguenta.**"),
        ("com a família", "**Sem nomear.** Se a pessoa nomeada estiver na sala, não trazer esta ficha. Trabalhar antes o que a impede de dizer."),
    ],
    10: [
        ("6–8", "**Ensaiar comigo.** Ela pede ao clínico o que quer pedir em casa, ali mesmo. Ensaiar a frio é metade do trabalho."),
        ("6–9", "**Onde é que dá.** Verificar se o pedido é possível na altura em que a tristeza costuma aparecer — ao deitar, no carro, à saída da escola."),
        ("8–9", "**Pedir sem palavras.** Combinar um gesto ou um objecto que sirva de pedido. Para crianças a quem dizer custa."),
        ("com a família", "**Combinar quem recebe.** A pessoa a quem ela vai pedir tem de saber que foi escolhida, e o que fazer quando não puder."),
    ],
}




# ---------------------------------------------------------------------------
# Assustado — nine sheets for the child plus the practitioner page (D-245).
#
# Externalising returns; *sair dali* is barred; and sheet 8 is the ladder, the
# only sheet in the project that orders anything. Its guidance carries the two
# cautions that matter most: the first step must be small enough to take today,
# and an attempt that fails means the step was too big, never that she cannot.
# ---------------------------------------------------------------------------

SHEETS["scared"] = [
    {
        "n": 1,
        "title": "O Medo",
        "Idade": "6 aos 9 anos",
        "Base": "Psicoeducação. Sem nível próprio: reformula em linguagem "
                "infantil o que a secção 1 sustenta.",
        "Objectivo": "Dar-lhe o enquadramento antes de lhe pedir seja o que for, "
                     "e mostrar-lhe o esquema dos dois painéis. Nada para "
                     "preencher.",
        "Como aplicar": "Ler com ela em voz alta. Tapar o painel da direita e "
                        "perguntar o que acha que acontece se ficar — é a única "
                        "pergunta desta página, e é para adivinhar, não para "
                        "responder certo.",
        "A notar": "**O Medo diz cuidado — não diz não vás** costuma ser a que "
                   "provoca reacção. Em crianças que já ouviram muitas vezes *não "
                   "tenhas medo*, a que alivia é a segunda: toda a gente tem.",
        "Cuidados": "Não acrescentar *e não há nada a temer*. Discutir se aquilo "
                    "é mesmo perigoso é a reavaliação que este material não faz.",
        "questions": [
            "Achas que as pessoas mais corajosas também têm medo?",
            "O que achas que acontece se ficarmos um bocadinho?",
        ],
    },
    {
        "n": 2,
        "title": "O Medo vem visitar",
        "Idade": "4 aos 7 anos",
        "Base": "Externalização, terapia narrativa. **Prática**, com pouca "
                "investigação controlada.",
        "Objectivo": "Pôr o Medo fora dela, como personagem, para que se possa "
                     "falar dele sem falar dela.",
        "Como aplicar": "Desenho primeiro, perguntas depois. A última pergunta — "
                        "*o que faz ele quando tu ficas na mesma* — é a que liga "
                        "ao esquema, e vale a pena guardá-la para o fim.",
        "A notar": "O tamanho que ela lhe dá, e se ele muda de tamanho conforme a "
                   "situação. **E se ele tem voz**: crianças que lhe dão frases "
                   "costumam repetir frases ouvidas em casa.",
        "Cuidados": "Externalizar não é entregar-lhe a responsabilidade. Se ela "
                    "disser *o Medo não me deixou ir*, a resposta é que **o Medo "
                    "apareceu e os pés eram dela** — as duas coisas ao mesmo "
                    "tempo, sem escolher.",
        "questions": [
            "Como é que sabes que ele está a chegar?",
            "O que é que ele te diz ao ouvido?",
            "E o que é que ele faz quando tu ficas na mesma?",
        ],
    },
    {
        "n": 3,
        "title": "O que o meu corpo faz",
        "Idade": "5 aos 8 anos",
        "Base": "Consciência interoceptiva. **Razoável** quanto à ligação entre "
                "reconhecer sinais e regular; a aplicação nesta forma é prática.",
        "Objectivo": "Reconhecer o aviso do corpo, que no medo é o mais claro de "
                     "todas as famílias — e descobrir que ele desce sozinho.",
        "Como aplicar": "Com o mapa corporal ao lado, se estiver a usá-lo. A "
                        "segunda pergunta é a importante: **se ficares, o corpo "
                        "continua igual?**",
        "A notar": "Se ela consegue nomear alguma coisa. Uma criança que não "
                   "sente nada no corpo ou não está a olhar, ou está a evitar "
                   "olhar — e são coisas diferentes.",
        "Cuidados": "Não transformar isto em vigilância dos sintomas. Uma criança "
                    "que passa a monitorizar o corpo encontra sempre alguma "
                    "coisa, e isso alimenta em vez de aliviar.",
        "questions": [
            "O que é que o corpo faz primeiro?",
            "Se ficares ali um bocadinho, continua igual?",
            "Já houve uma vez em que o corpo se assustou e afinal não era nada?",
        ],
    },
    {
        "n": 4,
        "title": "O que eu faço quando ele chega",
        "Idade": "6 aos 9 anos",
        "Base": "Comportamental — análise da resposta. **Estabelecido** quanto ao "
                "papel da evitação; esta aplicação é razoável.",
        "Objectivo": "Ver o que ela faz, e sobretudo se o que faz a deixa ficar "
                     "ou a leva embora. **É a distinção transformada em coluna.**",
        "Como aplicar": "Sem julgar nenhuma linha. A terceira coluna — *fico ou "
                        "saio* — é para ela assinalar, não para nós decidirmos.",
        "A notar": "**A mesma acção pode ser as duas coisas.** Ir ter com alguém "
                   "para conseguir ficar é aproximação; ir ter com alguém para "
                   "sair dali é fuga. A diferença nunca está na técnica, está no "
                   "que aconteceu a seguir.",
        "Cuidados": "A última pergunta — o que já não faz — costuma trazer mais do "
                    "que a tabela toda, e é onde a acomodação da família aparece "
                    "sem ninguém a nomear.",
        "questions": [
            "Isso que fazes deixa-te ficar ou leva-te embora?",
            "Há alguma coisa que já não fazes por causa do medo?",
            "Quem decide, quando isso acontece — tu ou o medo?",
        ],
    },
    {
        "n": 5,
        "title": "As palavras finas",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário emocional. **Razoável** quanto a diferenciação "
                "emocional; o conjunto é do ColorHugs.",
        "Objectivo": "Mostrar que as três se distinguem **por tempo** e não por "
                     "tamanho: nervoso é antes e perto, preocupado é antes e "
                     "longe, tímido é sobre quem se é.",
        "Como aplicar": "Uma caixa por palavra, sem ordem. Se uma ficar vazia, "
                        "deixá-la vazia.",
        "A notar": "Se usa *nervoso* só para coisas más. Metade da utilidade da "
                   "palavra está em ela também aparecer antes das boas.",
        "Cuidados": "**Não ordenar por tamanho**, nem sugeri-lo. Aqui a ordenação "
                    "por intensidade não faz sentido nenhum, e propô-la ensinaria "
                    "uma coisa falsa sobre as palavras.",
        "questions": [
            "Qual destas dizes mais vezes?",
            "Qual delas é antes de acontecer, e qual é durante?",
            "Alguma delas é uma palavra que os outros usam sobre ti?",
        ],
    },
    {
        "n": 6,
        "title": "Nervoso",
        "Idade": "6 aos 9 anos",
        "Base": "Vocabulário e antecipação. **Prática** nesta forma.",
        "Objectivo": "Recuperar a metade boa da palavra: nervoso aparece antes do "
                     "aniversário e antes da apresentação, e não só antes do que "
                     "corre mal.",
        "Como aplicar": "As duas caixas juntas, e por esta ordem — a de que não "
                        "gosta primeiro, porque é a que lhe vem à cabeça.",
        "A notar": "Se consegue preencher a segunda. **Uma criança que não "
                   "encontra nenhuma coisa boa que a deixe nervosa está a evitar "
                   "mais do que parece** — as coisas boas com nervoso dentro são "
                   "as primeiras a desaparecer.",
        "Cuidados": "Não tratar o nervoso como coisa a eliminar antes de uma "
                    "apresentação ou de um teste. Serve para preparar.",
        "questions": [
            "Uma coisa que te deixa nervosa e de que gostas na mesma?",
            "Onde é que sentes o nervoso no corpo?",
            "Ele vai-se embora quando a coisa começa?",
        ],
    },
    {
        "n": 7,
        "title": "Preocupado",
        "Idade": "7 aos 9 anos",
        "Base": "Antecipação e procura de garantias. **Razoável** quanto ao papel "
                "da procura de garantias na manutenção; a ficha é prática.",
        "Objectivo": "Ver a preocupação como medo com tempo futuro — e "
                     "**descobrir, por ela própria, que a garantia dura pouco.**",
        "Como aplicar": "A terceira pergunta é a ficha toda: *quanto tempo é que a "
                        "preocupação fica quieta?* Deixá-la responder sem "
                        "sugerir. Quase todas dizem *pouco*.",
        "A notar": "A quem pede garantias e com que frequência. **Se um adulto "
                   "responde a isto por ela na sessão, acabou de mostrar o "
                   "padrão.**",
        "Cuidados": "Não retirar as garantias de repente e sem combinar. O que se "
                    "combina é responder uma vez e depois responder à pergunta e "
                    "não à ansiedade — e isso combina-se com os adultos, não com "
                    "ela.",
        "questions": [
            "Costumas perguntar a alguém se vai correr bem?",
            "Quanto tempo é que a preocupação fica quieta depois?",
            "Há alguma preocupação que já não te aparece?",
        ],
    },
    {
        "n": 8,
        "title": "Tímido",
        "Idade": "6 aos 9 anos",
        "Base": "Temperamento e evitação social. **Estabelecido** quanto à "
                "distinção entre os dois; a ficha é prática.",
        "Objectivo": "Separar ser tímida — que não é problema nenhum — de deixar "
                     "de fazer coisas por causa disso, que é o que se trabalha.",
        "Como aplicar": "Começar pelos sítios onde fala à vontade, e não pelos "
                        "outros. A ficha abre a dizer que ser tímida não é um "
                        "problema, e essa frase é para ser lida em voz alta.",
        "A notar": "A terceira pergunta. **Uma criança a quem chamam tímida à "
                   "frente dos outros recebe uma identidade e não uma palavra**, e "
                   "o que ela diz sobre isso costuma ser a coisa mais útil da "
                   "página.",
        "Cuidados": "**Uma criança tímida com amigos não tem problema nenhum**, e "
                    "esta ficha não deve ser aplicada como se tivesse. Se houver "
                    "ausência de fala em contextos específicos, isso é sinal para "
                    "avaliar e não para aplicar mais fichas.",
        "questions": [
            "Onde é que falas à vontade sem pensar nisso?",
            "Há alguma coisa que gostavas de fazer e não fazes por vergonha?",
            "Alguém já te chamou tímida à frente dos outros?",
        ],
    },
    {
        "n": 9,
        "title": "Chegar devagar",
        "Idade": "6 aos 9 anos",
        "Base": "Aproximação gradual. **Estabelecido** — o achado mais sólido de "
                "todo este material. **Não é um protocolo de exposição.**",
        "Objectivo": "Transformar uma coisa evitada numa série de bocadinhos, "
                     "escolhidos por ela, com companhia combinada e com a falha "
                     "prevista.",
        "Como aplicar": "**O primeiro degrau tem de dar para fazer hoje.** É o "
                        "que mais corre mal: um degrau ambicioso não se dá, e "
                        "ninguém volta a tentar. Se ela propuser um grande, "
                        "aceitar e pôr um menor antes.",
        "A notar": "Se a ordem é dela e não a nossa ideia do que é mais difícil. "
                   "**E se preenche a caixa da falha**: quem não consegue "
                   "imaginar não conseguir é quem mais precisa de a ter escrita.",
        "Cuidados": "**Nunca perguntar quanto medo tem em cada degrau.** A ficha "
                    "ordena situações, não níveis. E sem prémio nem castigo: "
                    "aproximação com castigo em cima deixa de o ser.",
        "questions": [
            "Qual seria o bocadinho mais pequeno de todos?",
            "Quem vai contigo nesse?",
            "E se tentares e não conseguires, o que fazemos?",
        ],
    },
]

DYNAMICS["scared"] = {
    1: [
        ("4–6", "**A carta e o espelho.** Pôr a carta do assustado ao lado do espelho da primeira página e perguntar se são parecidos."),
        ("6–8", "**Tapar o painel da direita.** Mostrar só o lado do evitamento e pedir que adivinhe o outro. Descobre-o em vez de o ler."),
        ("8–9", "**Quem é que também tem.** Pedir que nomeie três pessoas corajosas e adivinhe o medo de cada uma. Costuma desarmar a ideia de que ter medo é falha."),
        ("qualquer", "**Guardar para o fim.** Reler esta página na última sessão e perguntar se mudou alguma coisa."),
    ],
    2: [
        ("4–6", "**Dar-lhe voz.** Perguntar o que o Medo diria se pudesse falar, e escrever isso ao lado do desenho."),
        ("4–7", "**Onde é que ele mora.** Pedir que desenhe onde o Medo fica quando não está com ela."),
        ("6–8", "**O Medo de outra pessoa.** Pedir que desenhe o Medo de um adulto da casa. Costuma dizer mais do que o dela."),
        ("7–9", "**O que ele quer.** Perguntar o que o Medo está a tentar conseguir. Aproxima da função sem usar a palavra."),
    ],
    3: [
        ("5–7", "**O mapa do corpo.** Marcar no mapa corporal onde é o aviso, e comparar com o da zanga se já o tiver feito. Não costumam ser o mesmo sítio."),
        ("5–8", "**Contar o que desce.** Ficar ali um minuto de relógio e ver o que o corpo faz. **Sem pedir nota nenhuma** — só o que mudou."),
        ("8–9", "**O falso alarme.** Procurar duas vezes em que o corpo avisou e não era nada. Serve o mecanismo sem discutir probabilidades."),
        ("com a família", "**O aviso dos adultos.** Perguntar-lhes o que os corpos deles fazem. As crianças costumam supor que os adultos não sentem."),
    ],
    4: [
        ("6–8", "**Duas pilhas.** Escrever seis situações e separá-las: as que ela faz e as que já não faz. A segunda pilha é a intervenção."),
        ("6–9", "**A mesma acção, duas leituras.** Pegar numa linha da tabela e perguntar o que aconteceu logo a seguir. É como se distingue aproximação de fuga."),
        ("8–9", "**Quem decidiu.** Percorrer as linhas e perguntar, em cada uma, se quem decidiu foi ela ou o medo."),
        ("com a família", "**O que deixámos de fazer.** Perguntar à família que coisas deixaram de fazer por causa disto. Mede a acomodação sem usar a palavra, e a lista surpreende quem a faz."),
    ],
    5: [
        ("7–9", "**Antes, durante, sempre.** Distribuir as três cartas por estes três tempos. É a estrutura desta família em vez de uma ordenação por tamanho."),
        ("7–9", "**A que os outros usam.** Perguntar qual das três já ouviu alguém dizer sobre ela."),
        ("8–9", "**O nervoso bom.** Procurar três coisas boas que dão nervoso. Se não encontrar nenhuma, ficou material para a ficha 6."),
        ("com a família", "**Cada um escolhe a sua.** Os adultos escolhem também, e contam uma vez em que a sentiram."),
    ],
    6: [
        ("6–8", "**Antes e depois.** Desenhar como estava antes de uma coisa começar e como estava a meio. O nervoso quase sempre desce quando a coisa começa."),
        ("6–9", "**A lista das coisas boas.** Cinco coisas de que gosta e ver em quantas há nervoso à mistura."),
        ("8–9", "**O nervoso dos outros.** Perguntar como é que se percebe que outra pessoa está nervosa. Treina o reconhecimento fora de si própria."),
        ("com a família", "**A véspera.** Combinar com os adultos o que se diz na véspera de uma coisa grande. *Vai correr tudo bem* costuma ser o que menos ajuda."),
    ],
    7: [
        ("7–9", "**Quanto tempo dura.** Cronometrar, a brincar, quanto tempo a preocupação fica quieta depois de alguém garantir. É a demonstração inteira."),
        ("7–9", "**A preocupação que já se foi.** Procurar uma que a preocupava o ano passado e já não. Mostra que passam, sem lho dizermos."),
        ("8–9", "**Adiar.** Combinar guardar as preocupações para um bocadinho do dia, em vez de as perseguir quando chegam. Simples de explicar e difícil de fazer."),
        ("com a família", "**Responder uma vez.** Combinar com os adultos como respondem à segunda e à terceira vez. **Isto combina-se com eles, não com ela.**"),
    ],
    8: [
        ("6–8", "**Os sítios onde falo.** Desenhar ou nomear os sítios onde fala à vontade, antes de tocar nos outros."),
        ("6–9", "**Uma coisa pequena com gente.** Escolher uma coisa social do tamanho de um degrau — pedir uma coisa ao balcão, dizer bom dia. Liga esta ficha à nona."),
        ("8–9", "**A palavra dos outros.** Perguntar o que sente quando lhe chamam tímida, e o que preferia que dissessem."),
        ("com a família", "**Não a apresentar como tímida.** Pedir aos adultos que deixem de o dizer à frente dela e de responder por ela. É a acomodação desta ficha."),
    ],
    9: [
        ("6–8", "**O degrau de hoje.** Fazer o primeiro degrau ali mesmo, na sessão, se for possível. Um degrau dado vale mais do que quatro escritos."),
        ("6–9", "**Cortar ao meio.** Pegar no primeiro degrau que ela propôs e fazer um mais pequeno antes. Quase sempre é preciso, e é melhor fazê-lo agora."),
        ("8–9", "**Onde é que dá.** Verificar onde e quando o degrau é possível — na escola, no recreio, ao fim do dia. Muitos não são."),
        ("com a família", "**Quem acompanha e o que faz.** A pessoa escolhida tem de saber que foi escolhida, e tem de saber que **não retira a coisa se ela ficar aflita**."),
    ],
}




# ---------------------------------------------------------------------------
# Envergonhado — nine sheets for the child plus the practitioner page (D-257).
#
# Two of the nine are conditional and their guidance says so in the first line
# of *Cuidados*: *Quem já sabe* is not applied without knowing who the person
# is, and *Arrependido* is not applied where there was no act.
#
# No guide here asks what the child hides. The questions are about the
# prediction, never about the content.
# ---------------------------------------------------------------------------

SHEETS["ashamed"] = [
    {
        "n": 1,
        "title": "A Vergonha",
        "Idade": "6 aos 9 anos",
        "Base": "Psicoeducação. Sem nível próprio: reformula em linguagem "
                "infantil o que a secção 1 sustenta.",
        "Objectivo": "Dar-lhe o enquadramento e mostrar-lhe o ciclo. Nada para "
                     "preencher.",
        "Como aplicar": "Ler com ela em voz alta e seguir o círculo com o dedo, "
                        "pela ordem. Tapar a coluna verde e perguntar o que acha "
                        "que faria o círculo abrir-se.",
        "A notar": "**Ela diz «tu és»** costuma ser a frase que provoca "
                   "reconhecimento — muitas crianças nunca ouviram ninguém "
                   "descrever aquilo que se passa dentro delas.",
        "Cuidados": "Não usar esta página para perguntar o que ela esconde. É "
                    "para explicar o mecanismo, e o mecanismo explica-se sem "
                    "conteúdo nenhum.",
        "questions": [
            "O que achas que faria o círculo abrir-se?",
            "Já te aconteceu alguém saber de uma coisa e continuar igual?",
        ],
    },
    {
        "n": 2,
        "title": "A Vergonha vem visitar",
        "Idade": "4 aos 7 anos",
        "Base": "Externalização, terapia narrativa. **Prática**, com pouca "
                "investigação controlada.",
        "Objectivo": "Pôr a Vergonha fora dela como personagem — o que nesta "
                     "família vale mais do que em qualquer outra, porque a "
                     "vergonha diz precisamente que ela **é** aquilo.",
        "Como aplicar": "Desenho primeiro, perguntas depois. A última — *isso que "
                        "ela diz é verdade?* — só se faz se o desenho já estiver "
                        "feito.",
        "A notar": "As frases que ela põe na boca da personagem. **Costumam ser "
                   "frases ouvidas**, e muitas vezes ouvidas em casa ou na "
                   "escola, palavra por palavra.",
        "Cuidados": "Não corrigir a personagem com factos. Se ela desenhar uma "
                    "Vergonha enorme, a resposta não é dizer que não é assim tão "
                    "grande — é perguntar onde é que ela a manda ir.",
        "questions": [
            "Onde é que ela te manda ir?",
            "O que é que ela te diz ao ouvido sobre ti?",
            "Isso que ela diz é verdade?",
        ],
    },
    {
        "n": 3,
        "title": "O que eu fiz e o que eu sou",
        "Idade": "7 aos 9 anos",
        "Base": "Distinção acto–pessoa. **Razoável** quanto ao efeito da "
                "atribuição global; a ficha é prática.",
        "Objectivo": "Separar as duas colunas que a vergonha cola. **É a "
                     "distinção da família transformada em tabela.**",
        "Como aplicar": "A coluna da direita é a que interessa, e é a que ela "
                        "preenche mais depressa. A pergunta final — *o que "
                        "dirias a um amigo* — faz-se depois de as três linhas "
                        "estarem escritas, nunca antes.",
        "A notar": "**A diferença entre o que ela diz a si própria e o que diria "
                   "a um amigo.** Quase todas são muito mais generosas com os "
                   "outros, e reparar nisso vale mais do que qualquer "
                   "explicação nossa.",
        "Cuidados": "Não discutir a coluna da direita. Argumentar contra um "
                    "rótulo global costuma reforçá-lo — o que o desfaz é ela "
                    "própria ouvir-se a dizer outra coisa a outra pessoa.",
        "questions": [
            "Se um amigo teu dissesse isso sobre ele, o que lhe dizias?",
            "Alguma dessas frases foi alguém que ta disse?",
            "Há alguma linha em que as duas colunas não combinam?",
        ],
    },
    {
        "n": 4,
        "title": "Quem continua a gostar de mim na mesma",
        "Idade": "4 aos 7 anos",
        "Base": "Vinculação e desconfirmação da previsão. **Estabelecido** quanto "
                "à disponibilidade do cuidador; o resto é razoável e prática.",
        "Objectivo": "Pedir-lhe que nomeie — e não argumentar com a previsão da "
                     "vergonha. As cinco figuras são as que ela viu no ecrã.",
        "Como aplicar": "Deixar assinalar quantas quiser, e não sugerir nenhuma. "
                        "A caixa do fim é para alguém que não esteja nas "
                        "figuras.",
        "A notar": "**Quantas pessoas consegue nomear, e se consegue alguma.** "
                   "Uma criança que só assinala *uma coisa que continua igual* "
                   "está a dizer que não consegue nomear ninguém — e essa é a "
                   "informação mais importante que esta actividade pode dar.",
        "Cuidados": "Se ela não conseguir nomear ninguém, **não preencher por "
                    "ela e não insistir**. Nomear alguém para lhe fazer a "
                    "vontade produz uma lista falsa e fecha o assunto.",
        "questions": [
            "Quem é que está lá mesmo nos dias maus?",
            "Há alguém teu que não esteja nas figuras?",
            "Alguma destas pessoas já te viu num dia mau?",
        ],
    },
    {
        "n": 5,
        "title": "As palavras finas",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário emocional. **Razoável** quanto a diferenciação "
                "emocional; o conjunto é do ColorHugs.",
        "Objectivo": "Mostrar que as três se distinguem **por alcance**: o "
                     "embaraço alcança um momento, a culpa alcança um acto, a "
                     "vergonha alcança a pessoa inteira.",
        "Como aplicar": "Uma caixa por palavra, sem ordem. Se uma ficar vazia, "
                        "deixá-la vazia.",
        "A notar": "Se usa *culpado* para coisas que não fez. É frequente, e "
                   "abre directamente a ficha seguinte.",
        "Cuidados": "**Não ordenar por tamanho.** Aqui não é o tamanho do "
                    "sentimento que muda, é o tamanho daquilo que ele condena — "
                    "e ordenar por intensidade seria quase acertar e errar no "
                    "essencial.",
        "questions": [
            "Qual destas dizes mais vezes?",
            "Qual delas passa depressa e qual é que fica?",
            "Alguma delas é sobre uma coisa que tu fizeste?",
        ],
    },
    {
        "n": 6,
        "title": "Culpado",
        "Idade": "7 aos 9 anos",
        "Base": "Distinção entre culpa por acto e culpa por acontecimento. "
                "**Razoável** quanto à distinção; a aplicação é prática.",
        "Objectivo": "Fazer a pergunta que parte esta família em duas: **foi uma "
                     "coisa que fizeste, ou uma coisa que aconteceu?**",
        "Como aplicar": "A segunda caixa é a ficha toda. Dar tempo, e não "
                        "sugerir a resposta — a criança que se culpa de um "
                        "acontecimento costuma demorar a dizê-lo.",
        "A notar": "**Culpa por um acontecimento não é culpa, é vergonha mal "
                   "arrumada**, e não se trabalha com reparação nenhuma. "
                   "Separação dos pais, doença de alguém, uma coisa que lhe foi "
                   "feita — são as três mais frequentes.",
        "Cuidados": "Se a resposta for *aconteceu*, **não seguir para a ficha "
                    "*Arrependido***. Pedir reparação por uma coisa que lhe "
                    "aconteceu confirma-lhe a culpa que ela já sente.",
        "questions": [
            "Isso foi uma coisa que tu fizeste, ou uma coisa que aconteceu?",
            "Alguém alguma vez te disse que a culpa era tua?",
            "Se tivesse acontecido a outra criança, a culpa era dela?",
        ],
    },
    {
        "n": 7,
        "title": "O que querias ter feito de outra maneira",
        "Idade": "6 aos 9 anos",
        "Base": "Geração de alternativas. **Razoável** — resolução de problemas "
                "é das melhores estudadas nesta idade; esta aplicação é prática.",
        "Objectivo": "Transformar o arrependimento em alternativa. **É a metade "
                     "virada para a frente**, e está separada da reparação "
                     "porque uma criança pode conseguir esta e não a outra.",
        "Como aplicar": "**Só depois da ficha *Culpado*, e só se a resposta lá "
                        "tiver sido *uma coisa que eu fiz*.** Nunca no dia.",
        "A notar": "Se a alternativa é dela ou é a nossa. **A dela vale mais**, "
                   "mesmo quando é pior — é a única que vem com a situação dela "
                   "dentro.",
        "Cuidados": "**Nunca perguntar *o que é que devias ter feito*.** É uma "
                    "repreensão disfarçada de ficha, e a criança percebe à "
                    "primeira. A pergunta é sobre o que **ela** queria. Não se "
                    "aplica onde não houve acto.",
        "questions": [
            "O que é que tu querias ter feito em vez disso?",
            "Se voltasse a acontecer amanhã, o que farias?",
            "Isso que querias fazer, dava mesmo para fazer?",
        ],
    },
    {
        "n": 8,
        "title": "O que querias dizer a quem ficou magoado",
        "Idade": "6 aos 9 anos",
        "Base": "Reparação. **Prática**, com apoio indirecto: é o que a distinção "
                "entre culpa e vergonha prevê.",
        "Objectivo": "Escolher o que dizer a quem ficou magoado, e prever o caso "
                     "de a outra pessoa não querer ouvir já.",
        "Como aplicar": "Depois da ficha anterior, e **nunca no mesmo dia do "
                        "acontecimento** — enquanto a coisa ainda está quente, "
                        "compor não é possível.",
        "A notar": "Se escreve sobre o que fez ou sobre o que sentiu. **Uma "
                   "criança que só consegue explicar-se ainda não chegou à outra "
                   "pessoa** — e isso é informação, não falha.",
        "Cuidados": "**A palavra *desculpa* não aparece na ficha e não deve ser "
                    "sugerida**: um pedido de desculpa mandado produz "
                    "obediência, não reparação. E não se aplica onde não houve "
                    "acto.",
        "questions": [
            "O que queres dizer a essa pessoa?",
            "E se ela não quiser falar já, o que podes dizer mais tarde?",
            "Há alguma coisa que queiras fazer em vez de dizer?",
        ],
    },
    {
        "n": 9,
        "title": "Embaraçado",
        "Idade": "6 aos 9 anos",
        "Base": "Distinção entre embaraço e vergonha. **Estabelecido** quanto às "
                "duas serem emoções diferentes; a ficha é prática.",
        "Objectivo": "Desfazer o que o português cola. Uma passa em cinco "
                     "minutos, a outra fica — e saber qual é qual muda o que se "
                     "faz a seguir.",
        "Como aplicar": "A primeira caixa antes da segunda, sempre. Uma vez que "
                        "já não faz nada é fácil de contar, e é ela que torna a "
                        "segunda perguntável.",
        "A notar": "**Se a segunda caixa fica vazia, isso não quer dizer que não "
                   "haja nada** — quer dizer que ainda não é para aqui que vem. "
                   "E se ela conta as duas com o mesmo tom, ainda não distingue "
                   "as duas coisas.",
        "Cuidados": "Não perguntar o que é a coisa da segunda caixa. **A ficha "
                    "pergunta se ainda dá aperto, não pergunta o que é.**",
        "questions": [
            "Essa primeira, hoje ainda te faz alguma coisa?",
            "Já te riste disso mais tarde?",
            "E a outra, é do mesmo tamanho que era?",
        ],
    },
    {
        "n": 10,
        "title": "Quem já sabe",
        "Idade": "6 aos 9 anos",
        "Base": "Desconfirmação da previsão. **Razoável** quanto ao efeito da "
                "revelação recebida; a ficha é prática.",
        "Objectivo": "Encontrar uma prova de que a previsão da vergonha já "
                     "falhou uma vez. **É a única ficha do projecto em que a "
                     "criança vê uma previsão sua a não se cumprir.**",
        "Como aplicar": "**Perguntar primeiro quem é a pessoa, e só depois "
                        "seguir.** A ficha só faz sentido se essa pessoa tiver "
                        "recebido bem.",
        "A notar": "O que mudou depois. **Se ela disser que não mudou nada, é "
                   "isso a prova** — e vale a pena nomeá-la em voz alta, porque "
                   "sozinha ela não a lê como prova.",
        "Cuidados": "**Não se aplica sem se saber quem é a pessoa.** Se quem já "
                    "sabe for quem a envergonhou, esta ficha aponta para o "
                    "problema e não para a saída, e o trabalho é outro — ver a "
                    "secção 10. Se ela não conseguir nomear ninguém, a ficha não "
                    "se aplica de todo.",
        "questions": [
            "Como é que essa pessoa ficou a saber?",
            "O que aconteceu depois de ela saber?",
            "Ela mudou alguma coisa contigo?",
        ],
    },
]

DYNAMICS["ashamed"] = {
    1: [
        ("4–6", "**A carta e o espelho.** Pôr a carta do envergonhado ao lado do espelho da primeira página e perguntar se são parecidos."),
        ("6–8", "**Seguir o círculo com o dedo.** Percorrer as caixas por ordem, em voz alta, e parar em *escondo* para perguntar o que acontecia se ali fosse ao contrário."),
        ("8–9", "**Tapar a coluna verde.** Mostrar só o ciclo e pedir que invente a saída antes de a ver."),
        ("qualquer", "**Guardar para o fim.** Reler esta página na última sessão e perguntar se o círculo dela mudou."),
    ],
    2: [
        ("4–6", "**Dar-lhe voz.** Escrever ao lado do desenho o que a Vergonha diz, palavra por palavra como ela a disser."),
        ("4–7", "**Onde é que ela manda ir.** Pedir que desenhe o sítio para onde a Vergonha a manda. Costuma ser o quarto, e costuma ser sozinha."),
        ("6–8", "**Quem é que fala como ela.** Perguntar se alguém que ela conhece diz coisas parecidas com as da personagem. **Perguntar, não sugerir.**"),
        ("7–9", "**A Vergonha de outra pessoa.** Pedir que desenhe a Vergonha de um adulto da casa. Costuma dizer mais do que a dela."),
    ],
    3: [
        ("7–9", "**Ler a coluna da direita em voz alta.** Ela lê, e depois lê outra vez como se fosse sobre outra pessoa. A diferença de tom é o material."),
        ("7–9", "**Quem disse isto primeiro.** Ao lado de cada frase da direita, marcar se foi ela que a inventou ou se a ouviu."),
        ("8–9", "**A frase que sobra.** Escolher a que ela nunca conseguiria dizer a um amigo, e trabalhar só essa."),
        ("com a família", "**Como falam dela.** Reparar, na sala, nas frases que usam: *ela é…* contra *ela fez…*. Faz-se sem uma única acusação, só notando."),
    ],
    4: [
        ("4–6", "**As figuras em cima da mesa.** Imprimir as cinco e deixar pegar, sem dizer nada."),
        ("4–7", "**Trazer uma prova.** Pedir que traga na próxima sessão uma coisa dessa pessoa — uma fotografia, um desenho, um objecto."),
        ("6–9", "**Ao contrário.** Perguntar de quem é que **ela** continua a gostar, sabendo o que sabe dessas pessoas. **É a dinâmica mais forte desta família**, e foi guardada para aqui porque precisa de alguém a conduzi-la."),
        ("com a família", "**Os adultos adivinham.** Pedir-lhes que escolham as figuras que acham que são dela antes de verem. A diferença é a conversa."),
    ],
    5: [
        ("7–9", "**Por alcance.** Pôr as três cartas por ordem daquilo que cada uma condena: um momento, uma coisa que fiz, eu toda."),
        ("7–9", "**Qual passa.** Separar as três em *passa* e *fica*, e ver onde ela põe cada uma."),
        ("8–9", "**A palavra que falta.** Perguntar-lhe que palavra usaria para a vergonha que não vem de nada que ela tenha feito. **Não há nenhuma em português, e ela costuma inventar uma boa.**"),
        ("com a família", "**Cada um escolhe a sua.** Os adultos escolhem também, e contam uma vez em que a sentiram."),
    ],
    6: [
        ("7–9", "**Duas pilhas.** Escrever cinco coisas de que se sente culpada e separá-las: as que fez e as que aconteceram."),
        ("7–9", "**Se fosse outra criança.** Contar a situação como se fosse de outra pessoa e perguntar de quem era a culpa."),
        ("8–9", "**Quem mais estava lá.** Nas que aconteceram, listar todas as pessoas envolvidas e ver quanto sobra para ela. Costuma sobrar muito pouco."),
        ("com a família", "**Dizer em voz alta.** Se for uma separação ou uma doença, pedir aos adultos que lhe digam explicitamente, à frente de quem aplica, que a culpa não foi dela. **Ela precisa de o ouvir deles, não de nós.**"),
    ],
    7: [
        ("6–8", "**Experimentar na sala.** Fazer ali mesmo a alternativa que ela escreveu, a brincar e sem estar em apuros. Ensaiar a frio é metade do trabalho."),
        ("6–9", "**Onde é que dava.** Verificar se aquilo que ela queria ter feito era mesmo possível naquele momento — havia tempo, havia sítio, estava lá alguém. Muitas vezes não era, e isso alivia."),
        ("8–9", "**Três em vez de uma.** Pedir três alternativas em vez de uma, mesmo que duas sejam más. Ter escolha vale mais do que ter a resposta certa."),
        ("com a família", "**A alternativa dos adultos.** Perguntar-lhes o que **eles** queriam ter feito de outra maneira naquele dia. Muda a sala inteira, e é raro alguém lho ter perguntado."),
    ],
    8: [
        ("6–8", "**Ensaiar em voz alta.** Dizer o que escreveu no balão, ao clínico, antes de dizer a quem é."),
        ("6–9", "**Reparar sem falar.** Procurar uma coisa que se faça em vez de se dizer. Para crianças a quem as palavras custam."),
        ("8–9", "**Se correr mal.** Preparar o que fazer se a outra pessoa não aceitar. Evita que uma tentativa falhada feche o assunto."),
        ("com a família", "**Os adultos também compõem.** Perguntar se algum deles se lembra de ter composto alguma coisa com ela."),
    ],
    9: [
        ("6–8", "**A história engraçada.** Pedir aos adultos ou ao clínico que contem um embaraço antigo de que hoje se riem. Mostra o *passa* em vez de o explicar."),
        ("6–9", "**Quanto tempo faz.** Nas duas caixas, escrever há quanto tempo foi cada uma. A diferença costuma ser visível."),
        ("8–9", "**O que faria passar.** Na segunda, perguntar o que teria de acontecer para deixar de doer. Quase sempre a resposta envolve outra pessoa."),
        ("com a família", "**Não repetir a história.** Combinar com os adultos não contarem o embaraço dela a terceiros como anedota. É frequente, é afectuoso, e é exactamente o mecanismo."),
    ],
    10: [
        ("6–8", "**Nomear a prova.** Depois de ela responder, dizer em voz alta: *a Vergonha disse que ia acontecer uma coisa, e não aconteceu.* Sozinha ela não lê aquilo como prova."),
        ("6–9", "**Mais alguém.** Perguntar se há mais alguém que poderia saber e continuar igual. Não para contar — só para nomear."),
        ("8–9", "**O que ela esperava.** Perguntar o que ela achava que ia acontecer quando essa pessoa soube, e comparar com o que aconteceu."),
        ("com a família", "**Continuar igual.** Se a pessoa que já sabe estiver na sala, o combinado é não voltar ao assunto de propósito e tratá-la como sempre. **A prova constrói-se com dias normais.**"),
    ],
}




# ---------------------------------------------------------------------------
# Tédio — nine sheets for the child plus the practitioner page (D-271).
#
# No externalising sheet: turning boredom into a character to be sent away is
# the opposite of what this family asks. And two guides carry cautions no other
# family needed — *Aborrecido* is the only sheet here that leads anywhere, and
# *Sem vontade* is the only child's sheet in the whole project that points
# outside the workbook.
# ---------------------------------------------------------------------------

SHEETS["bored"] = [
    {
        "n": 1,
        "title": "O Tédio",
        "Idade": "6 aos 9 anos",
        "Base": "Psicoeducação. Sem nível próprio: reformula em linguagem "
                "infantil o que a secção 1 sustenta.",
        "Objectivo": "Tirar a pressão antes de mais nada, e mostrar-lhe a tira "
                     "do tempo. Nada para preencher.",
        "Como aplicar": "Ler com ela em voz alta. Tapar a segunda tira e "
                        "perguntar o que acha que acontece se ninguém puser "
                        "nada.",
        "A notar": "**Não faz mal nenhum não ter nada para fazer** costuma "
                   "surpreender — muitas crianças ouvem o contrário todos os "
                   "dias, e algumas ficam visivelmente aliviadas.",
        "Cuidados": "**Não prometer que a ideia vem.** A página diz *às vezes*, e "
                    "esse *às vezes* é para ser lido como está. Uma criança que "
                    "espera e não inventa nada não falhou.",
        "questions": [
            "O que achas que acontece se ninguém puser nada?",
            "Já tinhas pensado que estar aborrecida podia servir para alguma coisa?",
        ],
    },
    {
        "n": 2,
        "title": "Quando é que ele aparece",
        "Idade": "5 aos 8 anos",
        "Base": "Comportamental — padrão temporal. **Razoável** nesta forma.",
        "Objectivo": "Ver as horas que se repetem, e sobretudo **o que acontece a "
                     "seguir**: se foi ela que arranjou alguma coisa ou se lhe "
                     "deram.",
        "Como aplicar": "Uma linha de cada vez. A última coluna é a que interessa "
                        "e é a que costuma ficar mais pobre — insistir um pouco "
                        "nessa.",
        "A notar": "**Se a resposta é sempre *deram-me*.** Não é acusação a "
                   "ninguém: é a medida da acomodação desta família, e aparece "
                   "sem se ter perguntado pelos adultos.",
        "Cuidados": "Não transformar a tabela numa lista de queixas sobre a "
                    "casa. O que se procura é o padrão, não o culpado.",
        "questions": [
            "Foste tu que arranjaste, ou foi alguém que te deu?",
            "Há alguma hora do dia em que aparece mais?",
            "E aos fins-de-semana?",
        ],
    },
    {
        "n": 3,
        "title": "O que me apetece agora",
        "Idade": "4 aos 7 anos",
        "Base": "Sem base própria. **Prática.** São actividades, não estratégias, "
                "e não há literatura que compare umas com as outras.",
        "Objectivo": "Mostrar o que há, sem pedir que escolha. **A primeira conta "
                     "como as outras**, e é a que dá a esta página o seu sentido.",
        "Como aplicar": "Pôr as seis à frente e não sugerir nenhuma. Se ela não "
                        "assinalar nada, deixar assim.",
        "A notar": "De que precisam as que ela escolhe — material, outra pessoa, "
                   "ou nada. **Se só escolhe as que precisam de material**, vale a "
                   "pena ver se consegue imaginar alguma coisa sem objectos. **E "
                   "se escolhe *não fazer nada de propósito*, reparar se é "
                   "escolha ou desistência**: as duas parecem-se e não são o "
                   "mesmo.",
        "Cuidados": "**Nenhuma é melhor do que outra**, e não fazer nada não é a "
                    "pior. Se a caixa do fim ficar vazia, não a preencher por ela.",
        "questions": [
            "Alguma destas já fazes sem ninguém te dizer?",
            "Há alguma que precisa de uma coisa que não tens?",
            "Há alguma tua que não esteja aqui?",
        ],
    },
    {
        "n": 4,
        "title": "A coisa que eu inventei",
        "Idade": "6 aos 9 anos",
        "Base": "Sem base própria. **Prática**, e ligada à afirmação graduada como "
                "razoável na secção 1.",
        "Objectivo": "Encontrar uma prova dela própria de que já saiu alguma coisa "
                     "do tempo vazio. **Substitui a ficha de externalização**, que "
                     "esta família não tem.",
        "Como aplicar": "Desenho primeiro, perguntas depois. Se ela não se lembrar "
                        "de nada, perguntar aos adultos presentes — costumam "
                        "lembrar-se de coisas que ela esqueceu.",
        "A notar": "Se foi sozinha ou acompanhada, e se voltou a fazer. **Uma "
                   "criança que não se lembra de nada não é uma criança sem "
                   "invenção** — é mais provável que seja uma criança cujo tempo "
                   "vazio nunca durou o suficiente.",
        "Cuidados": "Não elogiar a invenção como desempenho. É uma prova, não uma "
                    "prenda — e transformá-la em elogio põe pressão exactamente "
                    "onde esta família a quer tirar.",
        "questions": [
            "Foi ideia tua ou de mais alguém?",
            "Voltaste a fazer?",
            "O que estavas a fazer mesmo antes de te lembrares disso?",
        ],
    },
    {
        "n": 5,
        "title": "As palavras finas",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário emocional. **Razoável** quanto a diferenciação; o "
                "conjunto é do ColorHugs.",
        "Objectivo": "Mostrar que as quatro se distinguem **pelo que falta**: "
                     "estímulo, variedade, tempo, ou outra coisa.",
        "Como aplicar": "Uma caixa por palavra, sem ordem.",
        "A notar": "Se usa *aborrecido* para tudo. É frequente e é o que abre a "
                   "ficha seguinte.",
        "Cuidados": "**Não ordenar por tamanho.** E se ela preencher *sem "
                    "vontade* com facilidade e as outras com dificuldade, isso "
                    "não é vocabulário — é sinal, e vê-se na ficha 9.",
        "questions": [
            "Qual destas dizes mais vezes?",
            "Qual delas passa depressa e qual é que fica?",
            "Alguma delas é de uma pessoa em concreto?",
        ],
    },
    {
        "n": 6,
        "title": "Aborrecido",
        "Idade": "7 aos 9 anos",
        "Base": "Distinção entre sub-estimulação e dificuldade de iniciação. "
                "**Razoável** quanto às duas serem coisas diferentes; a ficha é "
                "prática.",
        "Objectivo": "**É a única ficha desta família que leva a algum lado.** "
                     "Separar *não há nada para fazer* de *não consigo começar*.",
        "Como aplicar": "A primeira caixa antes da segunda, sempre — a primeira é "
                        "fácil e é ela que torna a segunda perguntável. A "
                        "terceira faz-se devagar.",
        "A notar": "**A terceira caixa é a ficha toda.** O que ela nomeia como "
                   "impedimento aponta o caminho: cansaço, medo de correr mal, "
                   "não saber por onde, a tarefa ser grande de mais, ou nada que "
                   "ela consiga dizer.",
        "Cuidados": "**Se a resposta for *não consigo começar*, saímos do tédio**, "
                    "e o resto deste caderno não é o material indicado. O que "
                    "vier a seguir depende do que estiver a impedir, e isso não "
                    "está aqui.",
        "questions": [
            "Isso é não haver nada, ou é não conseguires começar?",
            "Há coisas de que gostas e que mesmo assim não começas?",
            "O que é que te parece estar a impedir?",
        ],
    },
    {
        "n": 7,
        "title": "Farto",
        "Idade": "6 aos 9 anos",
        "Base": "Saturação. **Prática** nesta forma.",
        "Objectivo": "Ver que farto tem alvo e o tédio não tem — e encontrar o "
                     "alvo dela.",
        "Como aplicar": "A segunda pergunta, sobre quanto tempo aguentou, dá "
                        "muitas vezes mais do que a primeira.",
        "A notar": "**Se nomeia sempre a mesma pessoa, é o achado da ficha do "
                   "*irritado* noutra família** — e vale a pena não o tratar como "
                   "tédio. Se nomeia sempre a mesma tarefa, pode ser calibração.",
        "Cuidados": "Não corrigir o alvo. *Mas tu gostas do teu irmão* fecha a "
                    "conversa e ensina que aquilo não se diz.",
        "questions": [
            "Farto de quê, ou de quem?",
            "Quanto tempo aguentaste antes de ficares assim?",
            "Há alguma coisa que faça isso ficar melhor?",
        ],
    },
    {
        "n": 8,
        "title": "Impaciente",
        "Idade": "6 aos 9 anos",
        "Base": "Espera e tolerância à demora. **Razoável** quanto à ligação com "
                "a previsibilidade; a ficha é prática.",
        "Objectivo": "É o tédio com uma coisa à vista. **A única das quatro que "
                     "tem fim previsto**, e a única em que se pode dizer "
                     "honestamente que passa.",
        "Como aplicar": "A segunda pergunta — saber ou não saber quanto falta — é "
                        "a que rende, e a resposta costuma surpreender os "
                        "adultos.",
        "A notar": "Quase todas as crianças aguentam melhor uma espera medida do "
                   "que uma indefinida. **Se ela disser o contrário, vale a pena "
                   "perceber porquê.**",
        "Cuidados": "Não transformar isto em treino de espera. A ficha descreve; "
                    "não é um exercício de tolerância.",
        "questions": [
            "Do que é que costumas estar à espera?",
            "É pior quando sabes quanto falta, ou quando não sabes?",
            "O que fazes enquanto esperas?",
        ],
    },
    {
        "n": 9,
        "title": "Sem vontade",
        "Idade": "7 aos 9 anos",
        "Base": "Distinção entre tédio e desinteresse persistente. **Estabelecido** "
                "quanto às duas serem coisas diferentes; a ficha é de notar, não "
                "de trabalhar.",
        "Objectivo": "**Notar, não tratar.** Três perguntas: é de uma coisa ou de "
                     "tudo, perdeu interesse por coisas de que gostava, e há "
                     "quanto tempo.",
        "Como aplicar": "Sem pressa e sem alarme. As três perguntas fazem-se pela "
                        "ordem em que estão, e a segunda é a que mais importa.",
        "A notar": "**Perda de interesse por coisas de que gostava é a resposta "
                   "que muda o que se faz a seguir**, mais do que a duração. "
                   "Recusa generalizada, prolongada, e que não varia com o sítio "
                   "nem com a companhia, não é tédio.",
        "Cuidados": "**É a única ficha de criança das sete famílias que não se "
                    "fecha sobre si mesma**: acaba a dizer-lhe para falar com um "
                    "adulto em quem confie. Isso é deliberado — aquilo que ela "
                    "pode estar a apanhar não é coisa que uma folha feche. Se as "
                    "respostas apontarem nesse sentido, o caminho é avaliação e "
                    "não mais fichas.",
        "questions": [
            "É de uma coisa em especial, ou é de tudo?",
            "Há alguma coisa de que gostavas muito e de que já não te apetece?",
            "Há quanto tempo é assim?",
        ],
    },
]

DYNAMICS["bored"] = {
    1: [
        ("4–6", "**A carta e o espelho.** Pôr a carta do aborrecido ao lado do espelho da primeira página e perguntar se são parecidos."),
        ("6–8", "**Tapar a segunda tira.** Mostrar só o que acontece quando se enche logo e pedir que adivinhe o outro lado."),
        ("8–9", "**Explicar aos pais.** Pedir que explique a tira a um adulto presente, por palavras dela."),
        ("qualquer", "**Guardar para o fim.** Reler esta página na última sessão e perguntar se mudou alguma coisa em casa."),
    ],
    2: [
        ("5–7", "**A linha do dia.** Desenhar o dia numa tira de papel e marcar com um traço as horas em que aparece."),
        ("6–8", "**Quem arranjou.** Ao lado de cada linha, marcar com um sinal se foi ela ou se foi outra pessoa. A coluna aparece sozinha."),
        ("8–9", "**O domingo.** Olhar só para os fins-de-semana. É onde o tempo não estruturado vive, e onde os padrões são mais claros."),
        ("com a família", "**O que fazemos quando ela diz.** Perguntar aos adultos antes de lhes dizer seja o que for. A resposta costuma ser imediata e costuma ser um ecrã."),
    ],
    3: [
        ("4–6", "**As seis em cima da mesa.** Imprimir e deixar pegar, sem dizer nada."),
        ("4–7", "**A caixa de coisas.** Pedir que traga na próxima sessão uma caixa com cinco coisas de casa que não sejam brinquedos."),
        ("6–9", "**Precisa de quê.** Separar as figuras em três pilhas: as que precisam de material, de outra pessoa, e de nada. Contar as pilhas com ela."),
        ("com a família", "**Os adultos adivinham.** Escolherem as que acham que são dela antes de verem. A diferença é a conversa."),
    ],
    4: [
        ("4–6", "**Fazer outra vez.** Se a coisa inventada ainda for possível, fazê-la ali na sessão."),
        ("6–8", "**A invenção dos adultos.** Perguntar-lhes o que inventavam quando eram pequenos e não havia nada. Costuma abrir a sala."),
        ("8–9", "**Onde é que estavas.** Procurar o sítio e a hora em que essas coisas costumam aparecer. Costuma ser sempre o mesmo sítio."),
        ("com a família", "**Guardar em vez de deitar fora.** Se a invenção existir em objecto, combinar guardá-la. Uma prova guardada vale mais do que uma prova contada."),
    ],
    5: [
        ("7–9", "**Pelo que falta.** Pôr as quatro cartas por ordem daquilo que falta em cada uma: estímulo, variedade, tempo, outra coisa."),
        ("7–9", "**Qual passa.** Separar as quatro em *passa depressa* e *fica*, e ver onde ela põe cada uma."),
        ("8–9", "**A palavra que falta.** Perguntar-lhe que palavra usaria para o tempo vazio que é bom. **Não há nenhuma em português, e a resposta dela costuma valer mais do que a nossa.**"),
        ("com a família", "**Cada um escolhe a sua.** Os adultos escolhem também, e dizem uma vez em que a sentiram."),
    ],
    6: [
        ("7–9", "**Duas pilhas.** Escrever seis situações e separá-las: *não havia nada* e *havia e não comecei*."),
        ("7–9", "**A tarefa cortada.** Pegar numa coisa que ela não consegue começar e cortá-la ao meio, e outra vez ao meio, até o primeiro passo caber num minuto."),
        ("8–9", "**O que muda quando muda.** Procurar uma vez em que ela conseguiu começar aquilo mesmo, e ver o que estava diferente."),
        ("com a família", "**Não é preguiça.** Se a resposta for *não consigo começar*, dizê-lo explicitamente aos adultos à frente dela. **É a correcção do rótulo, e tem de ser ouvida por ela.**"),
    ],
    7: [
        ("6–8", "**Quanto tempo dá.** Cronometrar, a brincar, quanto tempo ela aguenta a coisa de que se farta. Costuma ser mais do que ela pensa."),
        ("6–9", "**Variar em vez de acabar.** Procurar uma pequena mudança que faça a mesma coisa aguentar-se mais tempo."),
        ("8–9", "**Farto de quem.** Se o alvo for uma pessoa, trabalhar isso como relação e não como tédio."),
        ("com a família", "**A tarefa que se repete.** Se o alvo for uma tarefa doméstica ou escolar, ver com os adultos se está bem calibrada."),
    ],
    8: [
        ("6–8", "**Uma espera medida.** Usar um relógio ou uma ampulheta numa espera pequena e ver se muda alguma coisa."),
        ("6–9", "**A espera mais difícil.** Nomear a que custa mais, e ver se é longa ou se é indefinida. Quase sempre é indefinida."),
        ("8–9", "**O que os adultos fazem.** Perguntar como é que as pessoas grandes esperam. Costuma ser com o telemóvel, e vale a pena que seja ela a dizê-lo."),
        ("com a família", "**Dizer quanto falta.** Combinar dizer-lhe o tempo em vez de *já vai*. É pequeno e muda muito."),
    ],
    9: [
        ("7–9", "**A lista do que gostava.** Escrever cinco coisas de que gostava há um ano e marcar as que ainda lhe apetecem."),
        ("7–9", "**Varia com o sítio?** Ver se é igual em casa, na escola e em casa de outra pessoa. **Se for igual em todo o lado, não é tédio.**"),
        ("8–9", "**Há quanto tempo.** Situar o princípio num acontecimento, se houver. Muitas vezes há, e ninguém tinha ligado as duas coisas."),
        ("com a família", "**Perguntar-lhes o mesmo.** O que é que ela deixou de querer fazer, e desde quando. **Se as respostas coincidirem, isto sai deste caderno** e passa a ser avaliação."),
    ],
}




# ---------------------------------------------------------------------------
# Calmo — nine sheets for the child plus the practitioner page (D-280).
#
# The only family whose sheets start in the present rather than in memory, and
# the only one whose last sheet is written to be used in another family's
# session. No breathing anywhere, and no zone questions: calm is general
# deactivation and has nowhere to be pointed at (D-276).
# ---------------------------------------------------------------------------

SHEETS["calm"] = [
    {
        "n": 1,
        "title": "A Calma",
        "Idade": "6 aos 9 anos",
        "Base": "Psicoeducação. Sem nível próprio.",
        "Objectivo": "Dizer-lhe que a calma não faz barulho, e mostrar-lhe para "
                     "onde vai o que aqui se junta. Nada para preencher.",
        "Como aplicar": "Ler com ela. **O esquema é um mapa e é abstracto** — "
                        "seguir uma seta de cada vez, e só as das famílias que "
                        "ela já conhece.",
        "A notar": "Se percebe que isto é para depois. **É a única família cujo "
                   "sentido está fora dela**, e algumas crianças acham isso "
                   "estranho até verem a última ficha.",
        "Cuidados": "Não transformar a página numa promessa de que se vai sentir "
                    "melhor. O que se promete é ter onde ir buscar, e mais nada.",
        "questions": [
            "Achas que isto é para hoje ou para depois?",
            "Já te aconteceu lembrares-te de um sítio bom num dia mau?",
        ],
    },
    {
        "n": 2,
        "title": "O meu corpo agora",
        "Idade": "5 aos 8 anos",
        "Base": "Consciência interoceptiva. **Razoável** quanto a reconhecer "
                "estados; esta aplicação é prática.",
        "Objectivo": "**Começar no presente e não na memória.** Uma criança que "
                     "não repara na calma não tem o que recordar — por isso o "
                     "trabalho começa com o corpo que ela tem agora.",
        "Como aplicar": "Na sala, sem instrução e sem respiração. A lista de "
                        "palavras é para assinalar, não para escolher uma.",
        "A notar": "As palavras que escolhe, e **se alguma delas é de tom em vez "
                   "de zona**. Se ela responder com um sítio do corpo, anotar: é "
                   "o achado desta família e não um engano.",
        "Cuidados": "**Não é preciso que ela esteja calma**, e a ficha di-lo. "
                    "Pedir-lhe que fique transforma isto num exercício, que é "
                    "exactamente o que esta família não é.",
        "questions": [
            "O teu corpo, neste momento, está como?",
            "E quando chegaste hoje, estava igual?",
            "Se tivesses de escolher uma palavra só, qual era?",
        ],
    },
    {
        "n": 3,
        "title": "Onde e quando",
        "Idade": "4 aos 7 anos",
        "Base": "Sem base própria. **Prática.**",
        "Objectivo": "Recolher o depósito: sítios, alturas, quem lá está, e o que "
                     "o corpo faz. **Só depois da ficha 2**, porque só então ela "
                     "sabe o que anda a procurar.",
        "Como aplicar": "Uma linha de cada vez. A última pergunta — a qual "
                        "consegue ir esta semana — é a que torna isto utilizável.",
        "A notar": "**Se todos os sítios dependem de outra pessoa, ou se nenhum "
                   "depende.** E se algum é acessível hoje: um depósito feito de "
                   "sítios de férias não serve na terça-feira.",
        "Cuidados": "**Uma criança que não consegue nomear nenhum sítio calmo "
                    "pode não ter esse sítio.** Não é falha de vocabulário e não "
                    "se resolve insistindo — ver a secção 10.",
        "questions": [
            "Há algum sítio onde o teu corpo fica sempre assim?",
            "Acontece quando estás sozinha?",
            "A qual consegues ir esta semana?",
        ],
    },
    {
        "n": 4,
        "title": "Demorar-me",
        "Idade": "6 aos 9 anos",
        "Base": "Saboreio. **Razoável** — é a única das três camadas desta família "
                "com base identificável, e a literatura é sobretudo com adultos.",
        "Objectivo": "Ficar mais tempo numa coisa boa em vez de passar por ela. "
                     "**Pequena de propósito**: uma coisa boa grande não precisa "
                     "de ajuda nenhuma para ser notada.",
        "Como aplicar": "Contar devagar, com pormenores sensoriais. Se ela "
                        "despachar em duas frases, pedir outra vez mais devagar — "
                        "**é a lentidão que é o exercício, não a história.**",
        "A notar": "Se consegue demorar-se sem ficar desconfortável. E a terceira "
                   "pergunta — se alguém sabe que aquilo foi bom para ela — "
                   "costuma render mais do que as outras duas.",
        "Cuidados": "Não elogiar a história. **Elogiar transforma o saboreio em "
                    "desempenho**, e a criança passa a contar para agradar.",
        "questions": [
            "O que é que se via, o que é que se ouvia?",
            "O que é que o corpo fez nessa altura?",
            "Alguém sabe que aquilo foi bom para ti?",
        ],
    },
    {
        "n": 5,
        "title": "As palavras finas",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário emocional. **Razoável** quanto a diferenciação; o "
                "conjunto é do ColorHugs.",
        "Objectivo": "Mostrar que as três se distinguem **pelo que veio antes** — "
                     "uma coisa que passou, esforço, ou ausência de ameaça. "
                     "**Nenhuma é uma quantidade de calma.**",
        "Como aplicar": "Uma caixa por palavra, sem ordem.",
        "A notar": "Qual fica por preencher. E se ela distingue *tranquilo* de "
                   "*calmo* — a maioria não distingue, e tem razão.",
        "Cuidados": "***Tranquilo* é a palavra mais frágil do baralho** e está "
                    "registada como por resolver (D-161). Não insistir se ela "
                    "não a distinguir: o problema é da palavra e não dela.",
        "questions": [
            "Qual destas dizes mais vezes?",
            "Alguma delas vem sempre depois de outra coisa?",
            "Tranquilo é o mesmo que calmo, ou é diferente?",
        ],
    },
    {
        "n": 6,
        "title": "Tranquilo",
        "Idade": "7 aos 9 anos",
        "Base": "Vocabulário. **Prática**, e com a ressalva de D-161.",
        "Objectivo": "Salvar a palavra pela única coisa que a distingue na "
                     "prática: **é a calma depois de alguma coisa que passou.**",
        "Como aplicar": "A segunda pergunta — o que tinha acabado — é a que dá "
                        "sentido à primeira.",
        "A notar": "**Quanto tempo o corpo demorou a perceber que já tinha "
                   "passado.** É a mesma ideia da curva da activação vista do "
                   "outro lado, e liga esta família ao zangado.",
        "Cuidados": "Se ela não conseguir distinguir de *calmo*, aceitar e "
                    "seguir. **Não construir uma distinção que a língua não "
                    "sustenta.**",
        "questions": [
            "O que é que tinha acabado?",
            "Quanto tempo demorou o corpo a perceber?",
            "Houve alguma coisa que te ajudasse a perceber?",
        ],
    },
    {
        "n": 7,
        "title": "Descansado",
        "Idade": "6 aos 9 anos",
        "Base": "Vocabulário. **Prática.**",
        "Objectivo": "É a mais fácil das três de reconhecer, porque tem sempre um "
                     "antes. **Costuma ser a melhor porta de entrada nesta "
                     "família.**",
        "Como aplicar": "Se as fichas anteriores tiverem corrido mal — se ela não "
                        "reconheceu calma nenhuma — **começar por aqui e voltar "
                        "atrás depois.**",
        "A notar": "Se o descanso dela depende de ter havido esforço. A terceira "
                   "pergunta abre isso, e algumas crianças descobrem ali que "
                   "descansar não é uma recompensa.",
        "Cuidados": "Não ligar descanso a mérito. *Descansaste porque "
                    "trabalhaste* é uma frase de adulto e instala uma condição "
                    "onde não é preciso nenhuma.",
        "questions": [
            "Depois de que coisas é que ficas assim?",
            "É preciso estar cansada para ficar descansada?",
            "Onde é que costumas ficar?",
        ],
    },
    {
        "n": 8,
        "title": "Seguro",
        "Idade": "6 aos 9 anos",
        "Base": "Segurança percebida. **Estabelecido** quanto à sua relação com a "
                "regulação; a ficha é prática.",
        "Objectivo": "É o oposto exacto do assustado, e a condição das outras "
                     "duas. **Sem ela, a calma não aparece.**",
        "Como aplicar": "Pelas três perguntas por ordem. A terceira — sítio ou "
                        "pessoa — é a que separa um depósito de um problema.",
        "A notar": "**A ausência.** Se ela responder com facilidade a *onde me "
                   "sinto segura* e com dificuldade a nada mais, isso é bom "
                   "sinal; se for ao contrário, é o achado mais importante que "
                   "este caderno pode dar.",
        "Cuidados": "**Esta é a ficha que pode tirar a sessão deste caderno.** Se "
                    "aparecer um sítio ou uma pessoa concreta onde ela não se "
                    "sente segura, este material pára aí — o que se segue é "
                    "avaliação e, se for caso disso, o dever legal de comunicar. "
                    "Ver a secção 10.",
        "questions": [
            "Onde é que te sentes segura?",
            "É por causa do sítio, ou de quem lá está?",
            "Há sítios onde não te sentes?",
        ],
    },
    {
        "n": 9,
        "title": "O meu depósito",
        "Idade": "6 aos 9 anos",
        "Base": "Sem base própria. **Prática**, e é a concretização de tudo o que "
                "esta família existe para fazer.",
        "Objectivo": "Levar o que foi recolhido para as famílias que vão precisar "
                     "dele. **É a única ficha do projecto escrita para ser usada "
                     "na sessão de outra família.**",
        "Como aplicar": "No fim da família, e **com as fichas anteriores à "
                        "frente** — ela copia de lá, não inventa aqui. Se alguma "
                        "linha ficar vazia, deixar vazia.",
        "A notar": "Se o que ela põe em cada linha é diferente. **Se puser a mesma "
                   "coisa nas três, ou o depósito é pequeno ou aquela coisa é "
                   "muito boa** — e vale a pena saber qual das duas.",
        "Cuidados": "**Guardar a folha e voltar a ela nas outras famílias.** Uma "
                    "ficha de depósito que fica no processo e nunca mais se abre "
                    "não fez nada — e esta é a única do material cujo valor "
                    "depende inteiramente de ser reaberta.",
        "questions": [
            "Quando estiveres com medo, o que vais buscar?",
            "É a mesma coisa para as três, ou muda?",
            "Onde é que vais guardar esta folha?",
        ],
    },
]

DYNAMICS["calm"] = {
    1: [
        ("4–6", "**A carta e o espelho.** Pôr a carta do calmo ao lado do espelho da primeira página e perguntar se são parecidos."),
        ("6–8", "**Uma seta de cada vez.** Seguir só a família que ela conhece melhor e deixar as outras para depois."),
        ("8–9", "**Desenhar a seta que falta.** Perguntar-lhe que outra família ia buscar coisas aqui, e porquê."),
        ("qualquer", "**Guardar para o fim.** Voltar a esta página na última sessão, com a ficha 9 ao lado."),
    ],
    2: [
        ("5–7", "**Um minuto de nada.** Estar em silêncio um minuto de relógio, sem instrução nenhuma, e depois perguntar o que o corpo fez."),
        ("5–8", "**Duas palavras, duas vezes.** Uma no princípio da sessão e outra no fim, e comparar. Costuma haver diferença e ela costuma não ter reparado."),
        ("8–9", "**As palavras que faltam.** Pedir-lhe que acrescente palavras à lista. As dela costumam ser melhores do que as nossas."),
        ("com a família", "**Os adultos também.** Cada um diz duas palavras para o próprio corpo naquele momento. Mostra que isto se faz, e não só se pede."),
    ],
    3: [
        ("4–6", "**A planta da casa.** Desenhar a casa por cima e marcar onde o corpo fica assim. Costuma haver um sítio, e costuma não ser o quarto."),
        ("4–7", "**Ir lá e voltar.** Se o sítio existir no edifício, ir lá durante a sessão."),
        ("6–9", "**Sozinha ou acompanhada.** Separar os sítios em duas pilhas e ver qual é maior."),
        ("com a família", "**Onde é que ela fica assim.** Perguntar aos adultos antes de ela responder. As diferenças são o material, e costuma haver."),
    ],
    4: [
        ("6–8", "**Contar duas vezes.** A mesma coisa boa, a segunda vez mais devagar do que a primeira. A diferença é o exercício."),
        ("6–9", "**Dizer a quem lá estava.** Se a pessoa estiver na sala, contar-lhe a ela. Se não, combinar dizer-lhe durante a semana."),
        ("8–9", "**A coisa pequena.** Procurar deliberadamente a coisa boa mais pequena da semana. As grandes não precisam de ajuda para serem notadas."),
        ("com a família", "**Uma coisa boa cada um.** À vez, e devagar. É das poucas dinâmicas deste material que uma família consegue repetir sozinha."),
    ],
    5: [
        ("7–9", "**Pelo antes.** Pôr as três cartas por ordem do que veio antes de cada uma: uma coisa que passou, esforço, ausência de ameaça."),
        ("7–9", "**A palavra que ela usaria.** Perguntar que palavra usa em casa para isto. Muitas vezes não é nenhuma das três."),
        ("8–9", "**A calma sem antes.** Perguntar-lhe que palavra usaria para a calma que não veio depois de nada. **Não há nenhuma em português.**"),
        ("com a família", "**Cada um escolhe a sua.** Os adultos escolhem também, e dizem quando foi a última vez."),
    ],
    6: [
        ("7–9", "**O antes e o depois.** Desenhar dois quadrados: como estava o corpo antes de aquilo acabar, e como ficou depois."),
        ("7–9", "**O atraso.** Procurar uma vez em que a coisa já tinha acabado e o corpo ainda não sabia. **Liga esta ficha à curva do zangado.**"),
        ("8–9", "**Distinguir ou não.** Perguntar-lhe directamente se tranquilo e calmo são a mesma coisa, e aceitar a resposta que der."),
        ("com a família", "**O que ajuda a perceber que passou.** Perguntar aos adultos o que fazem quando uma coisa difícil acaba. Muitas vezes não fazem nada, e vale a pena que reparem."),
    ],
    7: [
        ("6–8", "**Antes e depois de mexer.** Fazer uma coisa que canse um bocadinho na sessão, e reparar no corpo a seguir."),
        ("6–9", "**Descansar sem ter feito nada.** Perguntar se dá. É a pergunta que desfaz a ligação entre descanso e mérito."),
        ("8–9", "**Os descansos que não descansam.** Procurar coisas que ela faz para descansar e que a deixam na mesma."),
        ("com a família", "**Como descansam os adultos.** E se descansam. Costuma abrir mais do que se espera."),
    ],
    8: [
        ("6–8", "**O mapa dos sítios seguros.** Marcar numa planta da casa e da escola. **Reparar no que fica por marcar.**"),
        ("6–9", "**Sítio ou pessoa.** Em cada sítio marcado, perguntar se seria igual sem aquela pessoa lá."),
        ("8–9", "**O que faria um sítio ficar seguro.** Perguntar sobre um sítio onde ela não se sente segura — **sem perguntar porquê.**"),
        ("com a família", "**Não usar o sítio dela como castigo.** Combinar isto explicitamente. Um sítio que serve de castigo não serve de depósito."),
    ],
    9: [
        ("6–8", "**Copiar de lá.** Pôr as fichas anteriores à frente e deixá-la copiar. Não é para inventar aqui."),
        ("6–9", "**Onde vai ficar.** Combinar um sítio concreto para guardar a folha — e que não seja o processo clínico."),
        ("8–9", "**Fotografar.** Se houver telemóvel em casa, combinar com os adultos guardar uma fotografia da folha, para quando o papel se perder."),
        ("com a família", "**Abrir noutra sessão.** Combinar com quem aplica que esta folha volta à mesa quando se trabalhar o medo, a zanga ou a tristeza. **É a única ficha do material cujo valor depende de ser reaberta.**"),
    ],
}


if __name__ == "__main__":
    import sys

    print(build(sys.argv[1] if len(sys.argv) > 1 else "angry"))
