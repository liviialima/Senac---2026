aluno = {}

aluno["nome"] = input("Qual seu nome:")
aluno["nota1"] =  float(input("Qual a nota 01?:"))
aluno["nota2"] = float(input("Qual a nota 02?:"))
  

media = (aluno["nota1"] + aluno["nota2"] ) /2

aluno ["media"] = media
if media >=7:
  print("Passou")
elif media >=5:
  print("media")
else:
  print("Reprovou")

print("\n Dados")
print("Nome:", aluno["nome"])
print("media:", aluno["media"])




