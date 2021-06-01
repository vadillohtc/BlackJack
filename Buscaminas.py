# generate random integer values
from random import randint

#Comienzo del juego
print("Bienvenido a BlackJack Maniacs")
cartas = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "J":10, "Q":10, "K":10, "A":1}
#print(cartas.keys())
#print(cartas.values())


total_jugador = 0
total_casino = 0

print("Tu primera carta es:")
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

print(nueva_carta())
