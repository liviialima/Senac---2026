numero = int(input("digite um número inteiro para gerar a tabuada: "))

print(f"\ntabuada do {numero}: ")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")