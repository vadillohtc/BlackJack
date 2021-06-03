# generate random integer values
from random import randint
from sys import stdin
from types import SimpleNamespace

#Comienzo del juego
print("Bienvenido a BlackJack Maniacs")
cartas={"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "J":10, "Q":10, "K":10, "A":11}

#print(cartas.keys())
#print(cartas.values())


def nueva_carta():
    value = randint(1, 12)
    if value == 1:
        carta = "2"
    elif value == 2:
        carta = "3"
    elif value == 3:
        carta = "4"
    elif value == 4:
        carta = "5"
    elif value == 5:
        carta = "6"
    elif value == 6:
        carta = "7"
    elif value == 7:
        carta = "8"
    elif value == 8:
        carta = "9"
    elif value == 9:
        carta = "J"
    elif value == 10:
        carta = "Q"
    elif value == 11:
        carta = "K"
    elif value == 12:
        carta = "A"
    return carta

total_jugador = 0
total_casino = 0

print("Tu primera carta es:")
carta_1_jugador = nueva_carta()
print(carta_1_jugador)
valor_carta_1_jugador = cartas.get(carta_1_jugador)
total_jugador += valor_carta_1_jugador
print("Tu segunda carta es:")
carta_2_jugador = nueva_carta()
print(carta_2_jugador)
valor_carta_2_jugador = cartas.get(carta_2_jugador)
total_jugador += valor_carta_2_jugador
print("El total de tu jugada es " + str(total_jugador))

print("La carta del casino es:")
carta_1_casino = nueva_carta()
print(carta_1_casino)
valor_carta_1_casino = cartas.get(carta_1_casino)
total_casino += valor_carta_1_casino
carta_2_casino = nueva_carta()
valor_carta_2_casino = cartas.get(carta_2_casino)
total_casino += valor_carta_2_casino
if total_jugador == 21:
    print("BLACKJACK!!")
else:
    print("¿Quieres una tercera carta? Si/No")
    respuesta_1 = input()

    if respuesta_1 == "No" or respuesta_1 == "no":
        while total_casino < total_jugador:
            total_casino += cartas.get(nueva_carta())
        print("El total de la jugada del casino es  " + str(total_casino))
        if total_casino > 21:
            print("La banca se ha pasado. Enhorabuena has ganado!!")
        elif total_jugador > total_casino:
            print("Enhorabuena has ganado!!")
        elif total_jugador < total_casino:
            print("Lo sentimos, prueba de nuevo")
        else:
            print("Parece que tenemos un empate!")

    if respuesta_1 == "Si" or respuesta_1 == "si":
        carta_3_jugador = nueva_carta()
        print("Tu tercera carta es " + str(carta_3_jugador))
        valor_carta_3_jugador = cartas.get(carta_3_jugador)
        total_jugador += valor_carta_3_jugador
        if total_jugador > 21 and carta_1_jugador == "A" or total_jugador > 21 and carta_2_jugador == "A" or total_jugador > 21 and carta_3_jugador == "A":
            total_jugador -= 10
            print("El total de tu jugada es: " + str(total_jugador))
            print("¿Quieres una cuarta carta? Si/No")
            respuesta_2 = input()
            if respuesta_2 == "No" or respuesta_2 == "no":
                while total_casino < total_jugador:
                    total_casino += cartas.get(nueva_carta())
                print("El total de la jugada del casino es  " + str(total_casino))
                if total_casino > 21:
                    print("La banca se ha pasado. Enhorabuena has ganado!!")
                elif total_jugador > total_casino:
                    print("Enhorabuena has ganado!!")
                elif total_jugador < total_casino:
                    print("Lo sentimos, prueba de nuevo")
                else:
                    print("Parece que tenemos un empate!")

            if respuesta_2 == "Si" or respuesta_2 == "si":
                carta_4_jugador = nueva_carta()
                print("Tu cuarta carta es " + str(carta_4_jugador))
                valor_carta_4_jugador = cartas.get(carta_4_jugador)
                total_jugador += valor_carta_4_jugador
                if total_jugador > 21 and carta_1_jugador == "A" or total_jugador > 21 and carta_2_jugador == "A" or total_jugador > 21 and carta_3_jugador == "A" or total_jugador > 21 and carta_4_jugador == "A":
                    total_jugador -= 10
                    print("El total de tu jugada es " + str(total_jugador))
                    while total_casino < total_jugador:
                        total_casino += cartas.get(nueva_carta())
                    print("El total de la jugada del casino es  " + str(total_casino))
                    if total_casino > 21:
                        print("La banca se ha pasado. Enhorabuena has ganado!!")
                    elif total_jugador > total_casino:
                        print("Enhorabuena has ganado!!")
                    elif total_jugador < total_casino:
                        print("Lo sentimos, prueba de nuevo")
                    else:
                        print("Parece que tenemos un empate!")
                else:                
                    if total_jugador > 21:
                        print("Te has pasado! Intentalo de nuevo.")
                    else:
                        while total_casino < total_jugador:
                            total_casino += cartas.get(nueva_carta())
                        print("El total de la jugada del casino es  " + str(total_casino))
                        if total_casino > 21:
                            print("La banca se ha pasado. Enhorabuena has ganado!!")
                        elif total_jugador > total_casino:
                            print("Enhorabuena has ganado!!")
                        elif total_jugador < total_casino:
                            print("Lo sentimos, prueba de nuevo")
                        else:
                            print("Parece que tenemos un empate!")
        else:
            if total_jugador > 21:
                print("Te has pasado! Intentalo de nuevo.")       
            else:
                print("El total de tu jugada es: " + str(total_jugador))
                print("¿Quieres una cuarta carta? Si/No")
                respuesta_2 = input()
                if respuesta_2 == "No" or respuesta_2 == "no":
                    while total_casino < total_jugador:
                        total_casino += cartas.get(nueva_carta())
                    print("El total de la jugada del casino es  " + str(total_casino))
                    if total_casino > 21:
                        print("La banca se ha pasado. Enhorabuena has ganado!!")
                    elif total_jugador > total_casino:
                        print("Enhorabuena has ganado!!")
                    elif total_jugador < total_casino:
                        print("Lo sentimos, prueba de nuevo")
                    else:
                        print("Parece que tenemos un empate!")

                if respuesta_2 == "Si" or respuesta_2 == "si":
                    carta_4_jugador = nueva_carta()
                    print("Tu cuarta carta es " + str(carta_4_jugador))
                    valor_carta_4_jugador = cartas.get(carta_4_jugador)
                    total_jugador += valor_carta_4_jugador
                    print("El total de tu jugada es " + str(total_jugador))
                    if total_jugador > 21:
                        print("Te has pasado! Intentalo de nuevo.")
                    else:
                        print("El total de la jugada del casino es  " + str(total_casino))
                        if total_casino > 21:
                            print("La banca se ha pasado. Enhorabuena has ganado!!")
                        elif total_jugador > total_casino:
                            print("Enhorabuena has ganado!!")
                        elif total_jugador < total_casino:
                            print("Lo sentimos, prueba de nuevo")
                        else:
                            print("Parece que tenemos un empate!")


#añadir una 5ª carta
#convertir los A en 1
#permitir hacer split
#añadir monetización