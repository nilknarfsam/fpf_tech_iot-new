#nome, sexo, salario

continuar = 'y'
count = 0

salario_m = 0
salario_f = 0

nome = list()
sexo = list()
salario = list ()

while True:
    print (f"Funcionario [0{count+1}]")
    print ("-----------------")

    nome.append(input("Nome: "))
    sexo.append(input("Sexo (m/f): ").lower())
    salario.append(float(input("Salario: ")))

    count+=1

    continuar = input("Continuar (s/n)?: ").lower()

    if continuar == 'n':
        break
    else:
        print("\n")

#somas
for x in sexo:
    if x == 'f':
        salario_f += salario[sexo.index(x)]
    else:
        salario_m += salario[sexo.index(x)]

#resultados
print (f"Salario homens: {salario_m}")
print (f"Salarios mulheres: {salario_f}")
print (f"Numero de funcionários: {count}")