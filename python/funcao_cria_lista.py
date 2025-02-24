#funcao
def criar_list_inteiro(qt):
    lista = []
    
    for i in range(qt):
        try: #importante isso aqui try/except
            lista.append(int(input("Valor int: ")))
        except ValueError:
            print("Numero invalido.")
    return lista

l = criar_list_inteiro(int(input("Limite: ")))

par = 0
impar = 0

for i in l:
    if i % 2 == 0:
        par += i
    else:
        impar += i

print ("Soma par: ", par)
print ("Soma impar: ", impar)