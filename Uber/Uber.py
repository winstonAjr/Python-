print("Consulte o valor do seu Uber")

km = float(input("\nPrimeiro, me diga quantos quilômetros são:\t"))

temp = float(input("\nAgora, só me diz agora quantos minutos são:\t"))

valor = 2 + 1.4 * km + 0.26 * temp

if valor >= 4:
  print(f"\nProntinho, o valor da sua corrida é de:\nR${valor}")
else:
  print("\nProntinho, o valor da sua corrida é de:\nR$ 4,00\nObs:Esse é nosso valor minímo!")