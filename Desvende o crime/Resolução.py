print("Vamos lhe fazer algumas perguntas sobre o caso 404\nResponta com sinceridade!")

r1 = int(input("\nVocê telefonou para a vítima?\n [1]Sim [0]Não:\t"))
r2 = int(input("\nVocê esteve no local do crime?\n [1]Sim [0]Não:\t"))
r3 = int(input("\nVocê mora perto da vítima?\n [1]Sim [0]Não:\t"))
r4 = int(input("\nVocê devia dinheiro pra vítima?\n [1]Sim [0]Não:\t"))
r5 = int(input("\nVocê já brigou com a vítima?\n [1]Sim [0]Não:\t"))

total = r1 + r2 + r3 + r4 + r5

if total == 5:
  print("\nConclusão: Assasino!")
elif total == 4 or total == 3:
  print("\nConclusão: Cúmplice")
elif total == 2:
  print("\nConclusão: Suspeito")
elif total == 0 or total == 1:
  print("\nConclusão: Inocente")
else:
  print("\nErro!")