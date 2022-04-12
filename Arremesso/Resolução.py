print("VAMOS VER SE VOCÊ BATEU\nO RECORD DO AREMESSO DE PESO!\n")
#sx é o sexo;
#va é a distância do arremesso.
while True:
  sx = int(input("Qual o seu sexo?\n[0]Masculino [1]Feminino\n\nResposta:\t"))
  va = float(input("\nQuantos metros foi o seu arremesso?\n\nResposta:\t"))

  if sx == 0:
    if va < 23.37:
      print(f"\nVocê não bateu o record,\nmas você fez seu melhor com {va}m")
      break
    else:
      print(f"\nParabéns! Você ultrapassou o record!\nCom a diferença de {va - 23.37}m\nO novo record é de {va} ")
      break
  elif sx == 1:
    if va < 22.41:
      print("\nVocê não bateu o record, mas você fez seu melhor")
      break
    else:
      print(f"\nParabéns! Você ultrapassou o record!\nCom a diferença de {va - 22.41}m")
      break
  else:
    print("\nOps!Algo deu errado\nTente novamente\n")