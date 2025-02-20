nome = 'Ayrton'

for x in nome:
    print (x)

print("\n")

for x in range(3):
    print (x+1)

print("\n")

nombre = 'Araujo'
for i in enumerate(nombre):
    print(i)

print("\n")

#tupla
nombre = 'Yolo!'
for i, j in enumerate(nombre):
    print(f"L {i}: {j}")

print("\n")

#list inside list
nombre = [1,2,3,[4,5,6]]
for i, j in enumerate(nombre):
    print(f"L {i}: {j}")