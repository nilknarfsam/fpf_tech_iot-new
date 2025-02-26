#nota de 0 a 10
nota = False

while True:
    nota = float(input("Nota: "))

    if nota < 0 or nota > 10:
        print("Valor invalido.")
    else:
        print (f"Nota inserida: {nota}")
        break

print("/n/n")

#impares entre 1 a 50
for x in range(50):
    if x % 2 != 0:
        print (x)
