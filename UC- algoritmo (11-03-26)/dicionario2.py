contato ={
    "@camila":"Camila",
    "@paola":"Paola",
    "@joão":"João"
}

#Obter chave
print("Chaves:")
for insta in contato.keys():
    print(insta)

#obter valores
print("\n Valores:")
for nome in contato.values():
    print(nome)

#obter pares
print("\n Pares:")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")

    contato = {
    "@camila":1.70,
    "@paola":1.80,
    "@joão":1.60
}
 
print("Ordenando por chaves:")
for insta in sorted(contato.keys()):
 print(f"{insta} --> {contato[insta]:.2f}m")

from operator import itemgetter
print("\n ordenado por valor (altura):")
for insta, estatura in sorted(contato.items(), key = itemgetter(1)):
  print(f"{insta} -->{estatura:.2f}m")




 