#fibonacci
temp = 0
temp_2 = 1
fibonacci = 0

limite = int(input("Digite o limite:"))

while fibonacci < limite:
   print(fibonacci, end="/")
   fibonacci = temp + temp_2
   temp = temp_2
   temp_2 = fibonacci
