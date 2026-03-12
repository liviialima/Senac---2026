valorporhora= float(input("Digite o valor:"))
hora = float(input("Digite as horas trabalhadas:"))

def calcularsalario(valorporhora, hora):
 salario = valorporhora * hora
 return salario 

resultado = calcularsalario(valorporhora, hora)
print(f"Seu salario é: {resultado}")