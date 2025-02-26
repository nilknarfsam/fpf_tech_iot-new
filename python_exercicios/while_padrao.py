#contador
num = 0
while num < 10:
    print (num)
    num += 1

print("\n")

#break
num = 0
while num < 10:
    num += 1
    if num == 3:
        break
    print (num)

print("\n")

#continue
num = 0
while num < 10:
    num += 1
    if num == 3:
        continue
    print (num)