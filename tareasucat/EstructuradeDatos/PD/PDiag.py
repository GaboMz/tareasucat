"""
SEMANA 1  JUEGO DIAGNOSTICO
"""
##ESTUDIANTE : MOISES GABRIEL MALPARTIDA ZABALETA
def jugar_ahorcado():
    palabra = "UCATEC"
    adivinadas = []
    intentos = 6

    while intentos > 0:
        progreso = ""

        # PROGRESO
        for letra in palabra:
            if letra in adivinadas:
                progreso = progreso + letra + " "
            else:
                progreso = progreso + "_ "

        print("Palabra: " + progreso)
        print("Intentos restantes: " + str(intentos))
        letra_usuario = input("Ingresa una letra: ").strip().upper()


        # PRIMERA VALIDACION 
        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        if letra_usuario in adivinadas:
            print("La letra ya fue usada. Intenta con otra.")
            continue
        adivinadas.append(letra_usuario)


        # VERIFICACION DE PALABRA
        if letra_usuario in palabra:
            print("Correcto.")
        else:
            print("Incorrecto.")
            intentos = intentos - 1


        # CONDICIONAL DE VICTORIA
        ganado = True
        for letra in palabra:
            if letra not in adivinadas:
                ganado = False
                break      
        if ganado:
            print("Ganaste. La palabra era: " + palabra)
            break

        #CONDICIONAL DE DERROTA
        if intentos == 0:
            print("Perdiste. La palabra correcta era: " + palabra)

if __name__ == "__main__":
    jugar_ahorcado()