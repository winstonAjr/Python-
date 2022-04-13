#"at" representa o número de atleta
#"st" representa a distância do salto
#"sts" representa quantos saltos por atleta serão feitos
#"sm" representa o maior salto
#"win" representa o qual atleta tem a maior distância
print("Vamos fazer algumas comparações\nMas primeiro\n")
at = int(input("Digite quantos atletas você testar?\n"))
sm = 0
sts = 3
for c in range(0,sts):
  c += 1
  for d in range(0,at):
    d+=1
    print(f"Salto #{c} Atleta {d} ")
    st = float(input("Qual a distância do salto?\n"))
    if st > sm :
      win = d
      sm = st
print(f"O ganhador foi o #{win}\nCom a potuação igual a {sm}")