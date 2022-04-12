#"m" seguido de um número, representa as manobras;
#"c" seguido de um número, representa as corridas.
print("VAMOS CONFERIR A SUA PONTUAÇÃO FINAL")

m1 = float(input("Qual a nota da primera manobra? "))
while m1 < 0 or m1 > 10:
  print("* A nota deve estar entre 0 e 10 *")
  m1 = float(input("Qual a nota da primera manobra? "))

m2 = float(input("Qual a nota da segunda manobra? "))
while m2 < 0 or m2 > 10:
  print("* A nota deve estar entre 0 e 10 *")
  m2 = float(input("Qual a nota da segunda manobra? "))

m3 = float(input("Qual a nota da terceira manobra? "))
while m3 < 0 or m3 > 10:
  print("* A nota deve estar entre 0 e 10 *")
  m3 = float(input("Qual a nota da terceira manobra? "))

m4 = float(input("Qual a nota da quarta manobra? "))
while m4 < 0 or m4 > 10:
  print("* A nota deve estar entre 0 e 10 *")
  m4 = float(input("Qual a nota da quarta manobra? "))

m5 = float(input("Quala nota da quinta manobra? "))
while m5 < 0 or m5 > 10:
  print("* A nota deve estar entre 0 e 10 *")
  m5 = float(input("Quala nota da quinta manobra? "))

c1 = float(input("Qual nota a da primeira corrida? "))
while c1 < 0 or c1 > 10:
  print("* A nota deve estar entre 0 e 10 *")
  c1 = float(input("Qual nota a da primeira corrida? "))

c2 = float(input("Qual nota a da segunda corrida? "))
while c2 < 0 or c2 > 10:
  print("* A nota deve estar entre 0 e 10 *")
  c2 = float(input("Qual nota a da segunda corrida? "))

notas = [m1, m2, m3, m4, m5, c1, c2]
notas.sort(key=int)
notas = notas[1:6] 
#tentei das formas que sabia, mas não consegui. Então saí procurando uma solução. Que foi essa. Se puder me explica melhor com funciona. Só entendi que tira os valores que são colocador no formato [x:y].
média = sum(notas)/5
#Esse comando "sum" não lembro ter visto com a senhora, mas mesmo assim procurei por aí e achei. Bem de boa.

print(f"O resultado é:{média}")