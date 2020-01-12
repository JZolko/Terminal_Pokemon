"""
    This progam is made to emulate the battle in the pokemon games. The two users will select a pokemon to battle.  The users are given options to 
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================


def read_file_moves(fp):  
    '''
        This sorts through the move csv and gets certain stats of the move
        to ultimately calculate damage
    '''
    lst = []
    reader = csv.reader(fp)
    next(reader, None) # skips header
    
    for line in reader: # goes through each line and skips the ones with empty values
        if int(line[2]) != 1 or int(line[9] == 1) or not(line[4]) or not(line[6]):
            pass
        else:
            lst.append(    Move(line[1],element_id_list[int(line[3])],int(line[4]), int(line[6]), int(line[9]))   )
    return lst #  returns list of moves

def read_file_pokemon(fp):
    '''
        This goes through the pokemon csv file and gets certain stats of the
        pokemon
    '''
    lst, final = {}, []
    reader = csv.reader(fp)
    next(reader, None) # skips header
    
    for line in reader: # goes through each line and skips the ones with empty values
        if int(line[11]) != 1 or int(line[0]) in lst.keys():
            pass
        else:
            lst[int(line[0])] = ( line )
    for item in lst: # assigns values
        name, type1, type2, hp, att, ddef, sat, sdef =\
        lst[item][1], lst[item][2], lst[item][3], lst[item][5], lst[item][6],\
        lst[item][7], lst[item][8], lst[item][9]
        final.append(Pokemon(name.lower(), type1.lower(), type2.lower(), None,\
                             int(hp), int(att), int(ddef), int(sat), int(sdef)))
    
    return final # returns the list of pokemon


def choose_pokemon(choice,pokemon_list):
    '''
        looks at either an int as the index or the actual name of the
        pokemon to return it to be used in battle
    '''
    for count, pkmon in enumerate(pokemon_list): # if its the name of the pokemon
        #print(type(pkmon))
        if choice.isalpha() and choice.lower() == pkmon.get_name():
            lst = deepcopy(pokemon_list)
            # returns a deep copy of the pokemon to make it a unique instance
            # returns the index of the name
            return deepcopy(lst[count])

        if choice.isdigit() and int(choice) < len(pokemon_list):
            lst = deepcopy(pokemon_list)
            # returns a deep copy of the pokemon to make it a unique instance
            # returns the index of the int
            return deepcopy(lst[int(choice)-1])
    return None # if it doesnt exist, returns none


def add_moves(pokemon,moves_list):
    '''
        This adds a random move of any element and then adds
        at max 3 more moves with matching elements
    '''
    r_mov = randint(0, (len(moves_list)-1)) # gets the random int for the first
    pokemon.add_move(moves_list[r_mov]) # element doesnt matter
    
    for i in range(len(moves_list)):#goes through list of moves
        r_mov = randint(0, (len(moves_list)-1)) # random int for each move
        #print(type(moves_list[r_mov]))
        
        if ((moves_list[r_mov].get_element() == pokemon.get_element1()\
        or moves_list[r_mov].get_element() == pokemon.get_element2())\
        and not(moves_list[r_mov] in pokemon.get_moves()))\
        :#and pokemon.get_number_moves() < 4:
            pokemon.add_move(moves_list[r_mov])
            # if the move has matching elements to at least one element

   
            if pokemon.get_number_moves() == 4:
                return True # only returns 4 moves
    else: # if all moves are exhausted, returns false if moves not full
        return False
    
def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        This one was pretty wack.
        This takes the player number and attacks the opposite pokemon
        using the attack method
        returs based on the health of the pokemon
    '''
    print("Player {}'s turn".format(player_num)) # prints turn number
    if player_num == 1:
        print(player_pokemon) # if the player num is 1, does everyhing
                              # according to the primary player
    else:
        print(opponent_pokemon) # if the int is 2
    print("Show options: 'show ele', 'show pow', 'show acc'")
    opt = input("Select an attack between 1 and {} or show option or 'q': "\
                .format(player_pokemon.get_number_moves())).lower()
    
    if player_num == 1: # goes through primaty player
        while not(opt.isdigit()): # if the input isnt an attack
            if opt == 'show ele': # prints elements of pk moves
       
                print(player_pokemon.show_move_elements())
            elif opt == 'show pow': # prints power of pk moves
    
                print(player_pokemon.show_move_power())
            elif opt == 'show acc':# prints accuracy of pk moves
    
                print(player_pokemon.show_move_accuracy())
            elif opt == 'q': # quits out, opponent wins by default
                    print("Player {} quits, Player {} has won the pokemon battle!"\
                          .format(1,2))
                    return True # a dub is had

            print("Show options: 'show ele', 'show pow', 'show acc'")
            
            opt = input("Select an attack between 1 and {} or show option or 'q': "\
                        .format(player_pokemon.get_number_moves())).lower()
        
        if opt.isdigit(): # selects the move that is used agaist the opponent
            opt = int(opt)
            
            
            # prints respective hp
            print("selected move:",player_pokemon.get_moves()[opt-1].get_name())
            
            
            print("\n{} hp before:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
            
            # pk attacks other pk
            player_pokemon.attack(player_pokemon.get_moves()[opt-1], opponent_pokemon)
            
            # prints respective hp
            print("{} hp after:{}\n".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
            
            # if the opposing pk is fainted
            if opponent_pokemon.get_hp() <= 0:
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(2,1))
                return True
            
            else:
                return False

    elif player_num == 2: # if the 'opponent' is playing

        while not(opt.isdigit()): #  if the input isnt an attack
            if opt == 'show ele': # prints elements of pk moves
       
                print(opponent_pokemon.show_move_elements())
            elif opt == 'show pow':# prints power of pk moves
    
                print(opponent_pokemon.show_move_power())
            elif opt == 'show acc':# prints accuracy of pk moves
    
                print(opponent_pokemon.show_move_accuracy())
            elif opt == 'q': # quits out, opponent wins by default
                    print("Player {} quits, Player {} has won the pokemon battle!".format(2,1))
                    return True # a dub is had

            print("Show options: 'show ele', 'show pow', 'show acc'")
            opt = input("Select an attack between 1 and {} or show option or 'q': ".format(opponent_pokemon.get_number_moves())).lower()
        if opt.isdigit():# selects the move that is used agaist the opponent
            opt = int(opt)
            
            # prints the selected move
            print("selected move:",opponent_pokemon.get_moves()[opt-1].get_name())
            
            # prints the hp before attack
            print("\n{} hp before:{}".format(player_pokemon.get_name(), player_pokemon.get_hp()))
            
            
            # attacks the other pokemon
            opponent_pokemon.attack(opponent_pokemon.get_moves()[opt-1], player_pokemon)
            
            # prints hp after the attack
            print("{} hp after:{}\n".format(player_pokemon.get_name(), player_pokemon.get_hp()))
            
            # if the pk faints
            if player_pokemon.get_hp() <= 0:
            
                print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(1,2))
                
                return True
            
            else:
                return False
    

    
def main():
    cont = ''
    p1, p2 = [], []
    player_num, m = 1, 0
    mov = open('moves.csv', 'r') # opens the move file
    pk = open('pokemon.csv', 'r') # opens the pk file
    moves_list = read_file_moves(mov) # makes the moves list
    pokemon_list = read_file_pokemon(pk) # makes the pokemon list
    w = False # win set to nah
    acceptable = ['y', 'n', 'q'] # good inputs that dont reprompt
    yeet = False
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp not in acceptable: # if it isnt y n or q
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
    
    if usr_inp == 'n' or usr_inp == 'q': # exits program
        print("Well that's a shame, goodbye ")
        return
    
    else: # if the player wants to have a good time
        
        while True: # loops until dub is had
            if w: # if there is a continuation after Win
                player_num = 1
                w = False
                yeet = True
            
            if player_num == 1 and not(p1): # if there isnt a pk for player 1
                choice = input("Player {}, choose a pokemon by name or index: ".format(player_num)).lower()
                ppk = choose_pokemon(str(choice),pokemon_list)
                print('pokemon{}:\n'.format(player_num), ppk) # prints pk name & stats
            
                while not(ppk): # if pk doesnt exist
                    print("Invalid option, choose a pokemon by name or index: ")
                    choice = input("Player {}, choose a pokemon by name or index: ".format(player_num)).lower()
                    ppk = choose_pokemon(str(choice),pokemon_list)
            
            if player_num == 2 and not(p2): # if player 2 doesnt have a pk
                choice = input("Player {}, choose a pokemon by name or index: ".format(player_num)).lower()
                ppk = choose_pokemon(str(choice),pokemon_list)
                print('pokemon{}:\n'.format(player_num), ppk) # prints pk name and stats
                
                while not(ppk): # if pk doesnt exist
                    print("Invalid option, choose a pokemon by name or index: ")
                    choice = input("Player {}, choose a pokemon by name or index: ".format(player_num)).lower()
                    ppk = choose_pokemon(str(choice),pokemon_list)
                
            
            
            if player_num == 1 and not(p1): # adds pk and moves to the player
                p1.append(ppk)
                add_moves(p1[0], moves_list) # adds moves to pk
            
            if player_num == 2 and not(p2): # adds pk and moves to opponent
                p2.append(ppk)
                add_moves(p2[0], moves_list) # adds moves to pk

            if p1 and p2: # if both pk exist
                if m == 0 or w: # if there is a continuation of a game
                    player_num = 1
                    w = False
                w = turn(player_num, p1[0], p2[0]) # attack function to attack
                m += 1
                
                
                # if there is a continuation of the program it prints the stats regardless
                if yeet and p1 and p2 and cont and (cont != 'n') and player_num == 2:
                    
                    print('Player 1 hp after:', p1[0].get_hp())
                    
                    
                    print('Player 2 hp after:', p2[0].get_hp())
                
                if w: # if the game is won
                    cont = input("Battle over, would you like to have another? ").lower()
                    # if the user wants to continue
                    if cont != 'n':
                        p1.pop() # deletes pokemon to start fresh
                        p2.pop()
                        m = 0 # continuation enabled
                    
                    else: # if they wanna be lame and not enjoy pokemon
                        print("Well that's a shame, goodbye ")
                        break
            
            
            # this goes back and forth from player one to player 2
            # i couldnt think of anything else and it works so yeah
            if player_num == 1:
                player_num = 2
            
            
            elif player_num == 2:
                player_num = 1           
            
            
if __name__ == "__main__":
    main()

