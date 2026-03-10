paciente = {}

paciente["nome"] = input("Qual seu nome:")
paciente["idade"] = int(input("Qual a sua idade:"))
paciente["peso"] = float(input("Qual seu peso:"))
paciente["altura"] = float(input("Qual a sua altura:"))

paciente["imc"] = imc

print("\n Dados")
print("Nome:", paciente["nome"])
print("Peso:", paciente["peso"])
print("Altura:", paciente["altura"])
print("Idade:", paciente["idade"])
print("imc:", round(paciente["imc"], 2))