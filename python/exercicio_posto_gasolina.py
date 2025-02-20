tipo = 'x'
valor_final = 0
preco_gasosa = 2.51
preco_alcool = 1.9


while tipo != 'A' and tipo != 'G':
    print ("Tipo de combustivel\nG - Gasolina\nA - Alcool")
    tipo = input("Sua escolha: ")

litros = float(input("Quantidade de litros: "))

if tipo == 'G':
    if litros <= 20:
        valor_final = litros * (preco_gasosa - (preco_gasosa*0.04)) 
    else:
        valor_final = litros * (preco_gasosa - (preco_gasosa*0.06))
else:   
    if litros <= 20:
        valor_final = litros * (preco_gasosa - (preco_gasosa*0.03)) 
    else:
        valor_final = litros * (preco_gasosa - (preco_gasosa*0.05))


print(f"Valor final: {valor_final}")