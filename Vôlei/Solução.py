print("VAMOS VER QUEM GANHOU ESSA PARTIDA")
#"e" seguido de número, representa a pontuação das equipes;
#"p" seguido de número, representa a pontos de cada equipe.
set_ = 1 
e1 = 0 
e2 = 0

while set_ <=5:
  if e1 == 3:
    print("\nEquipe 1 ganhou!")
    break
  elif e2 == 3:
    print("\nEquipe 2 ganhou!\n")
    break

  elif set_ > 4:
      print("#5 SET (Desempate):")
      p1 = int(input("Quantos pontos a equipe 1 fez?\t"))

      while p1 < 0 or p1 > 15:
        print("O mínimo de ponto deve estar entre 0 e 15")
        p1 = int(input("Quantos pontos a equipe 1 fez?\t"))

      p2 = int(input("Quantos pontos a equipe 2 fez?\t"))
      while p2 < 0 or p2 > 15 or p2 == p1:
        print("O mínimo de ponto deve estar entre 0 e 15, Se Equipe 1 tiver feito 15, não poder 15 aqui")
        p2 = int(input("Quantos pontos a equipe 2 fez?\t"))
      if p1 > p2 :
        print("\nEquipe 1 ganhou!")
        break
      else:
        print("\nEquipe 2 ganhou!")
        break
    
  print(f"\n#{set_} SET:\n")
  p1 = int(input("Quantos pontos a equipe 1 fez?\t"))
  while p1 < 0 or p1 > 25:
    print("O mínimo de ponto deve estar entre 0 e 25")
    p1 = int(input("Quantos pontos a equipe 1 fez?\t"))

  p2 = int(input("Quantos pontos a equipe 2 fez?\t"))
  while p2 < 0 or p2 > 25 or p2 == p1:
    print("O mínimo de ponto deve estar entre 0 e 25\nSe Equipe 1 fez 25, aqui não pode mais")
    p2 = int(input("Quantos pontos a equipe 2 fez?\t"))
  
  set_ += 1

  if p1 > p2:
    e1 += 1

  elif p2 > p1:
    e2 += 1