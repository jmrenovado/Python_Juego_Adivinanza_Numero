
import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza de números!")
    print("Debes adivinar un número entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        adivinanza = input("Introduzca un número del 1 al 100: ")
        if input("¿Desea salir del juego? (s/n): ").lower() == "s":
            print("Gracias por jugar, ¡hasta la próxima!")
            break

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganado! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos."
                )
        else:
            print("Por favor introduzca un número válido entre el 1 al 100")


juego_adivinanza()
