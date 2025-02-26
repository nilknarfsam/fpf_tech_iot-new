palavra = list(input("Palavra: ").lower())

count_vogal = 0
count_consoante = 0 

for x in palavra:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x=='u':
         count_vogal+=1
    else:
         count_consoante+=1

print(f"Vogais: {count_vogal}")
print(f"Consoantes: {count_consoante}")