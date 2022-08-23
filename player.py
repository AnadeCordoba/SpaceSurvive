# This file holds code to program the player of the games
#
#
class Player:
    def __init__(self, name):
        self.name= name

    def speak(self):
        print(f'Hola, me llamo {self.name}')


print("Bienvenido a la Alfa de SpaceSurvive")
print()

name= input("Introduce tu nombre de jugador: ")

jugador = Player(name)
jugador.speak()

