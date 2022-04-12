#"r" significa rodadas;
#"a" acompanhado de algum número, significa atleta.

print("VAMOS TESTAS OS 16 ATLETAS\nE CLASSIFICAR OS MELHORES!")
r = 1
print(f"\n#{r} Rodada:")
a1 = float(input("Qual o tempo, em segundos, do atleta 1?\nR:\t"))
a2 = float(input("Qual o tempo, em segundos, do atleta 2?\nR:\t"))
while r <= 8:
  if a1 < a2:
    print("Atleta 1 classificado!")
    r += 1
    if r <= 8:
      print(f"\n#{r} Rodada:")
      a1 = float(input("Qual o tempo, em segundos, do atleta 1?\nR:\t "))
      a2 = float(input("Qual o tempo, em segundos, do atleta 2?\nR:\t "))
    else:
      continue
  elif a2 < a1:
    print("Atleta 2 classificado!")
    r += 1
    if r <= 8:
      print(f"\n#{r} Rodada:")
      a1 = float(input("Qual o tempo, em segundos, do atleta 1? "))
      a2 = float(input("Qual o tempo, em segundos, do atleta 2? "))
    else:
      continue
  else:
    print("\nEmpatou!\nDigite os valores da partida de desempate:")
    print(f"\n#{r} Rodada:(desempate):")
    a1 = float(input("Qual o tempo, em segundos, do atleta 1?\nR:\t "))
    a2 = float(input("Qual o tempo, em segundos, do atleta 2?\nR:\t "))
else:
  print("Prontinho! Esses foram os melhores!")