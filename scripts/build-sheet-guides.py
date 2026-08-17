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

ANGRY = [
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


DYNAMICS = {1: [('4–6', '**A carta e o espelho.** Pôr a carta do zangado ao lado do espelho da primeira página e perguntar se são parecidos. Serve para ligar a personagem a ela própria sem ter de o dizer.'), ('6–8', '**Ler ao contrário.** Ler as três frases e perguntar, a cada uma, se alguém em casa diria o contrário. Traz o discurso da família para a sala sem perguntar pela família.'), ('8–9', '**Explicar a outra pessoa.** Pedir que explique a curva a um adulto presente, por palavras dela. Quem explica percebe melhor do que quem ouve.'), ('qualquer', '**Guardar para o fim.** Reler esta página na última sessão da família e perguntar se mudou alguma coisa.')], 2: [('6–8', '**Só desenhos.** O adulto escreve as colunas e a criança desenha uma cara ou um sítio em cada linha. A tabela funciona sem uma palavra.'), ('7–9', '**Ordenar por facilidade.** Depois de preenchida, pedir que aponte a linha mais fácil de contar e a mais difícil. É informação sobre ela, não sobre as situações.'), ('8–9', '**A linha que falta.** Perguntar se há uma situação que não escreveu. A que fica de fora costuma ser a que interessa.'), ('com a família', '**A mesma tabela pelos pais.** Cada um preenche a sua e comparam-se. As diferenças são o material da conversa.')], 3: [('4–6', '**Dar-lhe voz.** Perguntar o que a Zanga diria se pudesse falar, e escrever isso ao lado do desenho.'), ('4–7', '**Onde é que ela mora.** Pedir que desenhe onde a Zanga fica quando não está com ela. Externaliza um passo mais.'), ('6–8', '**A Zanga de outra pessoa.** Pedir que desenhe a Zanga de um adulto da casa. Costuma dizer mais do que a dela.'), ('7–9', '**O que a Zanga quer.** Perguntar o que a Zanga está a tentar conseguir. Aproxima da função sem usar a palavra.')], 4: [('7–9', '**Ordenar por frequência.** Pôr as três cartas da mais dita à menos dita. Não é intensidade: é uso.'), ('7–9', '**Uma semana a marcar.** Levar as três cartas e assinalar a que usou cada dia. Voltar com o registo.'), ('8–9', '**As palavras dos outros.** Perguntar qual das três usaria a mãe, o pai, o professor. Mapeia o vocabulário da casa.'), ('com a família', '**Cada um escolhe a sua.** Os adultos escolhem também, e dizem uma vez em que a sentiram.')], 5: [('7–9', '**Três montes.** Escrever cinco situações em papéis e pedir que as distribua pelas três cartas-mãe. Mostra-lhe a ambiguidade sem lha explicar.'), ('7–9', '**Trocar a palavra.** Escolher uma situação e procurar outra palavra que sirva melhor que *chateado*.'), ('8–9', '**Quando é que não serve.** Perguntar se há vezes em que dizer chateada não chega. Abre para as outras duas.'), ('com a família', '**O que ouvem quando ela diz.** Perguntar aos adultos o que percebem quando ela diz chateada. Muitas vezes percebem a errada.')], 6: [('7–9', '**O mapa do dia.** Marcar numa linha do dia as horas em que a irritação costuma aparecer. Costuma haver duas.'), ('7–9', '**O que muda quando muda.** Procurar uma vez em que aquilo que costuma irritar não irritou, e ver o que estava diferente.'), ('8–9', '**Três coisas que já tentou.** Listar e classificar cada uma como *ajudou*, *não ajudou*, *não sei*.'), ('com a família', '**Combinar um sinal.** Escolher com os adultos um gesto que ela possa fazer antes de a irritação crescer.')], 7: [('6–8', '**Desenhar o depois.** Em vez de contar a vez, desenhar o momento em que já tinha passado.'), ('7–9', '**Quem estava lá.** Marcar na folha quem estava presente e quem percebeu. Nem sempre são os mesmos.'), ('8–9', '**A versão do outro.** Contar a mesma vez do ponto de vista de quem lá estava. Exigente, e só quando a relação já aguenta.'), ('com a família', '**O que fizeram a seguir.** Perguntar aos adultos o que fizeram quando passou, não durante.')], 8: [('6–8', '**Experimentar na sala.** Fazer ali mesmo a estratégia escolhida, sem estar zangada. Ensaiar a frio é metade do trabalho.'), ('6–9', '**Onde é que dá.** Verificar se a estratégia escolhida é possível na escola, no carro, na sala de aula. Muitas não são.'), ('8–9', '**Plano B.** Escolher uma segunda para quando a primeira não der.'), ('com a família', '**Combinar quem ajuda.** Se a estratégia é *ir ter com alguém*, essa pessoa tem de saber que foi escolhida.')], 9: [('6–8', '**Ensaiar em voz alta.** Dizer o que escreveu no balão, à colega, antes de dizer a quem é.'), ('6–9', '**Reparar sem falar.** Procurar uma coisa que se faça em vez de se dizer. Para crianças a quem as palavras custam.'), ('8–9', '**Se correr mal.** Preparar o que fazer se a outra pessoa não aceitar. Evita que uma tentativa falhada feche o assunto.'), ('com a família', '**Os adultos também compõem.** Perguntar se algum deles se lembra de ter composto alguma coisa com ela.')]}


def page(sheet):
    rows = "\n".join(f"| **{f}** | {sheet[f]} |" for f in FIELDS)
    questions = "\n".join(f"- {q}" for q in sheet["questions"])
    # Dynamics that grow out of this sheet, banded by age. The general ones stay
    # in section 6; these are what the sheet itself opens up (D-197).
    dynamics = "\n".join(
        f"| {band} | {text} |" for band, text in DYNAMICS[sheet["n"]]
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


def build() -> str:
    body = "".join(page(s) for s in ANGRY)
    return f"""## 9. Fichas — orientação de aplicação

Uma página por ficha. **As fichas em si não estão aqui**: vivem no caderno de
exploração da criança, e uma licença dá acesso aos dois ficheiros — imprimi-las
duas vezes só produz duas cópias que podem ficar desencontradas.

Cada página diz para que serve a ficha, como se aplica, o que perguntar, o que
notar e o que evitar, e tem espaço para o registo da sessão em que foi usada.
**Por código, nunca por nome.**

{body}"""


if __name__ == "__main__":
    print(build())
