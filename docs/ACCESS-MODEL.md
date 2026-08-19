# ColorHugs — modelo de acesso

Como o material se arruma, quem tem acesso a quê, e o que se vende à parte.

Estado: `[DEFINED]` quanto à estrutura. **Os preços não estão definidos** e a
infra-estrutura de contas, pagamentos e verificação **não existe** — ver a última
secção.

---

## O princípio

A fronteira não é o tipo de ficheiro nem o preço. **É quem tem de estar na sala
para o material ser seguro.**

O projecto já tinha decidido isto sem lhe chamar arrumação comercial: *uma peça
que abre uma coisa e a deixa aberta só pode existir onde há alguém para a
apanhar*. **Essa frase é a fronteira**, e ela separa *sozinho* de *acompanhado*,
não *grátis* de *pago*.

---

## Dois eixos, e são independentes

| | |
| --- | --- |
| **Quem és** | família · professor · profissional (por especialidade) |
| **Como pagas** | subscrição individual · licença institucional |

**São independentes de propósito.** Um professor pode ser assinante individual ou
usar assentos comprados pela escola. Uma clínica pode querer comprar assentos de
profissional. **Se os dois eixos não estiverem separados desde o princípio, mais
tarde não se separam.**

---

## Os níveis

### Público — sem conta

As páginas informativas, a montra e **um pacote grátis**. É o que ganha o
endereço de correio e mostra a qualidade. **Nada que abra nada.**

### Free — com conta, sem pagar

Duas ou três actividades representativas de cada área do interactivo, mais o
pacote grátis. **Free não é anonimato:** é o nível sem pagamento, com o mesmo
perfil autorizado e os mesmos controlos.

### Premium — famílias

O interactivo completo e **todos os imprimíveis de família**.

### Professores — individual ou instituição

O interactivo completo, os imprimíveis de família, e **a linha de professores**.
O mesmo conteúdo nos dois casos; muda quem paga e quantos usam.

### Profissional — verificado, por especialidade

**Tudo o que o Premium tem, mais o conjunto clínico da sua especialidade.**

---

## O núcleo comum e o módulo de especialidade

**Todas as profissões recebem o mesmo núcleo:** o interactivo completo e os
imprimíveis de família. **O que difere é o conjunto clínico.**

Isto tem uma consequência técnica que não é evidente e que decide a base de
dados: **os ficheiros são etiquetados por especialidade, não por nível.** Um
sistema que apenas saiba *este utilizador é profissional* entrega material de
psicologia a um terapeuta da fala. Tem de saber **qual** profissional.

**Hoje existe um conjunto clínico: o de psicologia.** A arquitectura aceita os
outros; o lançamento tem um.

---

## A verificação, e as duas forças que ela tem

| Profissão | Como se verifica | Força |
| --- | --- | --- |
| **Psicologia** | cédula confirmada contra o registo público da Ordem | confirmação |
| **Terapia da fala, terapia ocupacional, psicomotricidade** | cédula pedida como documento | dissuasão |

**Estas duas não valem o mesmo, e quem desenhar o processo tem de o saber.** Pedir
um documento apanha o casual e não apanha o determinado.

**O que faz o trabalho a sério é a folha de licença**, que transforma o uso
indevido em incumprimento. A verificação filtra; a licença responsabiliza.

**Em qualquer dos casos é trabalho humano por cada inscrição.** Sem ele, a
exclusividade é uma frase — e a folha de licença assume uma coisa que não se
verificou.

---

## A alocação, peça a peça

| Material | Público | Free | Premium | Professores | Profissional |
| --- | :-: | :-: | :-: | :-: | :-: |
| Páginas informativas | ✓ | ✓ | ✓ | ✓ | ✓ |
| Pacote grátis | ✓ | ✓ | ✓ | ✓ | ✓ |
| Interactivo — amostra | | ✓ | ✓ | ✓ | ✓ |
| Interactivo — completo | | | ✓ | ✓ | ✓ |
| Páginas de colorir | | | ✓ | ✓ | ✓ |
| Baralho das sete famílias | | | ✓ | ✓ | ✓ |
| *Quem És Tu?* | | | ✓ | ✓ | ✓ |
| *Antes de Precisar* | | | ✓ | ✓ | ✓ |
| Cartas aos pais — versão família | | | ✓ | ✓ | ✓ |
| Linha de professores | | | | ✓ | |
| Cadernos de aplicação | | | | | ✓ |
| Cadernos de exploração | | | | | ✓ |
| Cartas aos pais — versão consulta | | | | | ✓ |
| Peças de sessão | | | | | ✓ |
| Baralho terapêutico | | | | | ✓ |
| O Depósito | | | | | ✓ |
| Peças de registo | | | | | ✓ |
| Enquadramento, consentimento, licença | | | | | ✓ |

---

## Três consequências que não são óbvias

**Os cadernos de exploração ficam no Profissional, apesar de serem fichas de
criança.** Das doze folhas do Zangado, uma está marcada como sendo do clínico e
outra dos pais: **o caderno de exploração não é um produto autónomo — é a parte
da criança de um caderno que pressupõe alguém a conduzir.** Uma família Premium
não fica sem nada: tem o interactivo, as páginas de colorir, o baralho e os dois
livros.

**O baralho das sete famílias aparece em três sítios ao mesmo tempo** — Premium,
Profissional, e à venda em papel. **Não é duplicação: é o mesmo conteúdo com três
formas de entrega**, que é a tese do modelo comercial. O que não pode acontecer é
a mesma pessoa pagar duas vezes pela mesma forma.

**O Profissional é um superconjunto, e o que o torna seguro não é o preço — é a
credencial.** Uma família não deixa de comprar o pacote de psicólogos por ser
caro; não o compra porque **não passa na verificação.**

---

## Venda avulsa

Para quem não está em nível nenhum:

- **pacotes individuais de imprimíveis**, para quem quer um e não uma subscrição;
- **os objectos físicos** — o baralho impresso, o baralho terapêutico, *O
  Depósito*. **São coisas e não ficheiros**, e vendem-se como coisas: têm stock,
  portes e devoluções, que é outro negócio.

---

## O que isto exige e que não existe

**Nada disto funciona na montagem actual.** O site é exportação estática no
GitHub Pages: serve ficheiros e não conhece ninguém.

- **Autenticação** e perfis de adulto com perfis de criança associados.
- **Pagamentos e subscrições**, com um fornecedor.
- **Verificação de direitos do lado do servidor**, por nível e por especialidade.
- **Entrega protegida dos ficheiros.** *Um PDF numa pasta pública não fica
  protegido por estar atrás de uma página com senha.*
- **Verificação profissional**, com uma pessoa a fazê-la.

**As actividades do interactivo podem avançar já; o portão comercial é um projecto
próprio**, com custo mensal e com decisões que não são de conteúdo.
