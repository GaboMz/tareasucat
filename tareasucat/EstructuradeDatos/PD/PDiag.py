palabra = "PYTHON"
adivinadas = []
intentos = 6

print("AHORCADO")

while intentos > 0:
    progreso = ""

    for letra in palabra:
        if letra in adivinadas:
            progreso = progreso + letra + " "
        else:
            progreso = progreso + "_ "


    print("\npalabra:", progreso)
    print("intentos:", intentos)
    letra_usuario = input("ingresa una letra ").upper()


    if letra_usuario in adivinadas:
        print(" la letra ya fue usada")
        continue

    adivinadas.append(letra_usuario)

    if letra_usuario in palabra:
        print("correcto")
    else:
        print("incorrecto")
        intentos = intentos - 1

    if progreso.replace(" ", "") == palabra:
        print("ganaste la palabra es", palabra)
        break

if intentos == 0:
    print("\nperdiste la palabra es", palabra)