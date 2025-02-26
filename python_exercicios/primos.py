cont = 0
num = int(input("Seu número: "))

for x in range(1, num + 1):  
    if num % x == 0:
        cont += 1
        if cont > 2: 
            print("Não é primo.")
            
            print("Divisivel por:", end=" ")
            for y in range(1, num + 1):
                if num % y == 0:
                    print(y, end=" ")
            break
else:
    print("É primo.")
