#sem dicionario
matricula1 = 2026001
nome1 = "Ana silva"
telefone1 = "9999-8888"


#com dicionario 
aluno ={
    "matricula": 2026001,
    "nome":"Ana silva",
    "telefone": "9999-8888" 
}
 
  print(aluno)

 contato = {
    "@camilaqueiroz": "Camila Queiroz",
    "@brunamarquezine": "Bruna Marquezine",
    "@sheronmendes": "Sheron M.",
    "@paolaoliveira": "Paola O."
    "@joaobaptysta": "joao b."
}

print(contato)
print(type(contato))

#acesso direto
print(contato["@camilaqueiroz"])

#acesso seguro com get()
print(contato.get("@camilaqueiroz"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "não encontrado"))

#add novo elemento 
contato["@brunamarquezine"] = "Bruna"
print("Após add:",contato)

#atualiza elemento existente
contato["@paolaoliveira"] = "Paola oliveira"
print("Após add:", contato)

contato.update({
    "@brunamarquezine": "Bruna Marquezine",
    "@sheronmendes": "Sheron M.",
})

print("Após atualização:", contato)

#pop: remove e retorna
removido = contato.pop("@paolaoliveira")
print(f"removido:{removido}")
print("Após o del:", contato)

#del remove sem retornar
del contato["@sheronmendes"]
print("Após o del:", contato)


#clear esvazia tudo 
copia = dict(contato)
contato.clear()
print("Após clear:", contato)
print("cópia:", copia)

print("Número de contatos:", len(contato)) #tamanho dicio

#verificar existência 

if "@joaobaptysta"  in contato:
  print(f"Encontrado: {contato{'@joaobaptysta'}}")

 if "@inexistente" in contato:
    print("Existe")
  else:
   print("Não existe")
