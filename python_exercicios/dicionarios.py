#dicionario padrao
dicionario = {"nome":"Ayrton", "idade": 30, "pet": "Gato"}
print(dicionario["nome"]) #imprime o valor dentro da chave selecionada

#usando a funcao dict
dicionario_2 = dict(nome = "Ayrton", idade = 30, pet = "Gato")
print(dicionario_2) #imprime todo o dicionario

#quebra o dict em tuplas
itens = dicionario.items()
print(itens)