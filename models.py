from constants import *


class Battle:   #Definicion del combate

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1    #Se inicializan los primeros pokemon
        self.pokemon2 = pokemon2
        self.actual_turn = 0

    def is_finished(self): #Metodo para encontrar si la batalla termino
        finished = self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0
        if finished:    # si alguno de los hp de algun pokemon es menor a 0
            self.print_winner() # se imprimira el resultado del ganador
        return finished

    def print_winner(self): # el metodo para obtener el pokemon ganador
        if self.pokemon1.current_hp <= 0 < self.pokemon2.current_hp:
                print("\n"+ self.pokemon2.name + " won in " + str(self.actual_turn)+" turns!!")
        #si los hp del pokemon 1 son menor que 0 y los del pokemon 2 son mayores a 0
        #El pokemon 2 gana
        
        elif self.pokemon2.current_hp <= 0 < self.pokemon1.current_hp:
                print("\n"+ self.pokemon1.name + " won in " + str(self.actual_turn)+" turns!!")
        #si los hp del pokemon 2 son menor que 0 y los del pokemon 1 son mayores a 0
        #El pokemon 1 gana
        else:
            print("DOUBLE KO!") #Si ninguna de estas condiciones se cumple es un empate

    def execute_turn(self, turn): #Metodo para los turnos
        # Logic to execute a turn inside a battle
        command1 = turn.command1 #Un turno se define en el comando que se digite
        command2 = turn.command2
        attack1 = None 
        attack2 = None
        if DO_ATTACK in command1.action.keys():
            attack1 = self.pokemon1.attacks[command1.action[DO_ATTACK]]
        #Si el comando es el ataque, se manda a realizar la accion de ataque
        if DO_ATTACK in command2.action.keys():
            attack2 = self.pokemon2.attacks[command2.action[DO_ATTACK]]

        # Execute attacks
        self.pokemon2.current_hp -= attack1.power #Se bajan los hp al cual un pokemon 
        self.pokemon1.current_hp -= attack2.power #realizo un ataque
        self.actual_turn += 1 #Se sube un turno

    def print_current_status(self):
        print("-------------------------")
        print(self.pokemon1.name + " has " + str(self.pokemon1.current_hp) + " left!")
        print(self.pokemon2.name + " has " + str(self.pokemon2.current_hp) + " left!")
        print("-------------------------")
    # este metodo es para imprimir el estado de los hp de los pokemon

class Pokemon:
    #Se inicializa la clase pokemon con sus atributos
    def __init__(self, name, level, type1, type2):
        self.type2 = type2
        self.type1 = type1
        self.level = level
        self.name = name
        self.attacks = []
        self.stats = {}
        self.current_status = 0
        self.current_hp = 0


class Attack:

    def __init__(self, name, t, category, pp, power, accuracy):
        self.name = name
        self.type = t
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy


class Turn:

    def __init__(self):
        self.command1 = None
        self.command2 = None

    def can_start(self):
        return self.command1 is not None and self.command2 is not None


class Command:

    def __init__(self, action):
        self.action = action