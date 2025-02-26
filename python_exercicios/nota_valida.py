while True:
    nota = float(input("Nota: "))
    if 0 <= nota <= 10:
        break
    print("Nota invalida. Digite novamente.")

print(f"Nota digitada: {nota}")
