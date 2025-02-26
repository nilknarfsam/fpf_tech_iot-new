lista = [1,2,3,4,5,6,7,8,9,10]

par = 0
impar = 0

for x in lista:
    if x % 2 == 0:
        par += x
    else:
        impar += x

print ("Soma par: ", par)
print ("Soma impar: ", impar)