altura = float(input("Digite a sua altura"))
altura = altura * 100

print(f"Sua altura é de {altura}cm")
print("Sua altur é: ", altura, "cm")

nome = "Livia"
idade = 16

texto = "Meu nome é {} e tenho {} anos".format(nome,idade)
texto = "Meu nome é {} e tenho {} anos".format(n=nome, i=idade)
texto = "Meu nome é %s e tenho %d anos" %(nome,idade)
print(texto)
