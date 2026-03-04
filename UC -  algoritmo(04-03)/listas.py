nome1 = "Ana"
nome2 = "Brino"
nome3 = "Caio"

nomes = ["Ana","Brino","Caio"]
print(nomes)

dados = ["Carol",0,1.70, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

lista = ["cachorro","gato"]
print("Original:",lista)

lista.append("Coelho") #add no fim da lista
print("Atualizado:",lista)

lista.insert(1,"Grilo")  #add na posição determinada
print("Atualizado:",lista)

lista.extend(["Macaco","ovelha"]) #add mais de um dado de uma vez
print("Lista final",lista)