from constants import *
from models import *

#First define pokemons with its stats
#Definicion de los primetos atributos de los pokemon
pokemon1 = Pokemon("Bulbasaur", 100, "grass", "poison")
pokemon2 = Pokemon("Charmander", 100, "fire", None)
pokemon1.current_hp = 45
pokemon2.current_hp = 39
#Stats

pokemon1.stats = {      #Stats inicales del primer pokemon
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45
}

pokemon2.stats = {      #Stats inicales del segundo pokemon
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

#Attacks
#Este es el primer ataque del pokemon (uno y dos)
pokemon1.attacks = [Attack("scratch", "normal", PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("scratch", "normal", PHYSICAL, 10, 10, 100)]


def ask_command(pokemon): #Comando para hacer la peticion al usuario para que seleccione un comando
    command = None  #INICIALIZACION 
    while not command:
        tmp_command = input("What should "+pokemon.name+" do? ").split(" ") #El usuario escribe lo que hara el pokemon
        if len(tmp_command) == 2:# si lo que escribe el usuario tiene un espacio en blanco
            try:                 # revisa que se digito "attack" y el numero del ataque 
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4: #La respuesta correcta 
                    command = Command({DO_ATTACK: int(tmp_command[1])})         #seria attack 0
            except Exception:
                pass
    return command #Se regresa el comando 

#Start battle

battle = Battle(pokemon1, pokemon2)

while not battle.is_finished(): #Mientras que la battala no termine
    #Main pokemon battle loop   # seguira el loop de la pelea
    #First ask for the commands
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    #Generate new turn
    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        # Execute turn
        battle.execute_turn(turn)
        battle.print_current_status()