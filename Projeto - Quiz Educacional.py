print('Bem vindo ao quiz!')

pergunta1 = input(
  "1) Assinale a alternativa que apresenta o significado da Educação Ambiental.: \n a) Compreende os processos por meio dos quais o indivíduo e a coletividade constroem valores sociais, conhecimentos, habilidades, atitudes e competências voltadas para a conservação do meio ambiente, que favorecem a qualidade de vida e a sustentabilidade. \n b) Compreende os processos por meio do qual um indivíduo constrói valores sociais, conhecimentos, atitudes e competências voltadas para a conservação do meio ambiente, essencial somente para a sustentabilidade \n c) A educação ambiental é um componente essencial que deve estar presente, somente, no processo educativo das crianças. \n d) A concepção da educação ambiental em sua totalidade, visa a vinculação entre a ética, a educação, o trabalho e as práticas sociais para os estudos de um meio ambiente menos sustentável. \n e) . \n R: "
)

cont = 0

if pergunta1 == "A" or pergunta1 == "a":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'A', não {pergunta1!r}")
  cont = cont - 1


pergunta2 = input(
  "2) Qual o Estado que mais produz lixo diariamente no Brasil?: \n a) Rio de Janeiro. \n b) São Paulo. \n c) Minas Gerais. \n d) Ceará. \n e) Bahia. \n R: "
)

if pergunta2 == "B" or pergunta2 == "b":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'B', não {pergunta2!r}")
  cont = cont - 1

pergunta3 = input(
  "3) Uma das formas de colaborar com a preservação do meio ambiente é reduzir a produção de resíduos. Mas como? \n a) Reutilizando os materiais e objetos sempre que possível. \n b) Apoiando iniciativas de reciclagem. \n c) Incentivando a participação individual e coletiva, permanente e responsável, na preservação do equilíbrio do meio ambiente, entendendo-se a defesa da qualidade ambiental como um valor inseparável do exercício da cidadania. \n d) Estimulando a cooperação entre as diversas regiões do País, com vistas à construção de uma sociedade ambientalmente equilibrada, fundada nos princípios da liberdade, igualdade, solidariedade, democracia, justiça social, responsabilidade e sustentabilidade. \n e) Todas as anteriores. \n R: "
)

if pergunta3 == "E" or pergunta3 == "e":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'E', não {pergunta3!r}")
  cont = cont - 1


pergunta4 = input(
  "4) Qual alternativa abaixo apresenta uma vantagem da energia solar? \n a) Não é renovável. \n b) Não polui. \n c) É eficaz em qualquer clima. \n d) . \n e) . \n R: "
)

if pergunta4 == "B" or pergunta4 == "b":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'B', não {pergunta4!r}")
  cont = cont - 1

pergunta5 = input(
  "5) O que é coleta seletiva? \n a) Destinação de resíduos para lixões e aterros. \n b) Processo de envio de todo o lixo produzido para cooperativas ou entrega para catadores de rua. \n c) Processo de separação e recolhimento dos resíduos para o reaproveitamento por meio de reciclagem. \n d) . \n e) . \n R: "
)

if pergunta5 == "C" or pergunta5 == "c":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'C', não {pergunta5!r}")
  cont = cont - 1

pergunta6 = input(
  "6) O que é reciclagem? \n a) Processo de limpeza, separação e organização de um material que é descartado e não pode ser reutilizado. \n b) Coleta de entulho. \n c) Todo tipo de lixo coletado. \n d) Quando transformam materiais usados em novos produtos para a sua reutilização. \n e) Nome dado para o processo do descarte do lixo. \n R: "
)

if pergunta6 == "D" or pergunta6 == "d":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'D', não {pergunta6!r}")
  cont = cont - 1

pergunta7 = input(
  "7) O que deve ser feito com os lixos eletrônicos - pilhas, baterias, celulares, tablets, entre outros? \n a) Jogar no lixo destinado aos metais. \n b) Jogar no lixo comum. \n c) Recolher, organizar e armazenar em casa o máximo de tempo que der. \n d) Descartar no caminhão do lixo. \n e) Procurar locais específicos para seu descarte. \n R:"
)

if pergunta7 == "E" or pergunta7 == "e":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'E', não {pergunta7!r}")
  cont = cont - 1

pergunta8 = input(
  "8) A pontuação numa prova de 25 questões é a seguinte: +4 por questão respondida corretamente e –1 por questão respondida de forma errada. Para que um aluno receba nota correspondente a um número positivo, deverá acertar no míni: \n a) 3 questões \n b) 4 questões \n c) 5 questões \n d) 6 questões \n e) 7 questões \n R: "
)

if pergunta8 == "A" or pergunta8 == "a":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'A', não {pergunta8!r}")
  cont = cont - 1

pergunta9 = input(
  "9) A pontuação numa prova de 25 questões é a seguinte: +4 por questão respondida corretamente e –1 por questão respondida de forma errada. Para que um aluno receba nota correspondente a um número positivo, deverá acertar no míni: \n a) 3 questões \n b) 4 questões \n c) 5 questões \n d) 6 questões \n e) 7 questões \n R: "
)

if pergunta9 == "A" or pergunta9 == "a":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'A', não {pergunta9!r}")
  cont = cont - 1

pergunta10 = input(
  "10) A Coleta Seletiva é um mecanismo de recolha dos resíduos, os quais são classificados de acordo com sua origem e depositados em contentores indicados por cores. Marque a alternativa que corresponde corretamente o material e a cor de seu contentor: \n a) Azul: papéis e papelões; Verde: vidros; Vermelho: plásticos; Amarelo: metais; Marrom: resíduos orgânicos; \n b) Azul: plásticos; Verde: metais; Vermelho: papéis e papelões; Amarelo: vidros; Marrom: resíduos orgânicos; \n Azul: papéis e papelões; Verde: resíduos orgânicos; Vermelho: plásticos; Amarelo: metais; Marrom: vidros;  \n d) Azul: papéis e papelões; Verde: vidros; Vermelho: plásticos; Amarelo: metais; Marrom: resíduos orgânicos;  \n e) Azul: vidros; Verde: papéis e papelões; Vermelho: resíduos orgânicos; Amarelo: plásticos; Marrom: metais;   \n R: "
)

if pergunta10 == "A" or pergunta10 == "a":
  print("Correto!")
  cont = cont + 1
else:
  print(f"A resposta é 'A', não {pergunta10!r}")
  cont = cont - 1

print('A sua pontuação final foi:', (cont))
