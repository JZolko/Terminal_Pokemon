"""
    SOURCE HEADER GOES HERE!
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
            This returns the name of the move
        '''

        return self.name
        
    def __repr__(self):
        '''
            This also returns the name of the move, but is somehow different than the __str__()????
        '''
        return self.name
    
    def get_name(self):
        '''
            This is also a way to get the name of the move
        '''
        return self.name
    
    def get_element(self):
        '''
            This gets the element of the move and returns it
            element is used to determine effectiveness
        '''
        return self.element
    
    def get_power(self):
        '''
            This gets the power of the move
            which is used in the calculation for total move damage
        '''
        return self.power
    
    def get_accuracy(self):
        '''
            this returns the accuracy of the move
            this is compared to a random int to get hit chance
        '''
        return self.accuracy
    
    def get_attack_type(self):
        '''
            this returns the attack type of a move
            this is used in the attack formula to caculate total damage
        '''
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves
    
    def __str__(self):
        '''
            This returns the different stats of the pokemon as well as the
            moves and name of the pokemon
        '''
        out1 = '{:<15s}{:<15d}{:<15d}{:<15d}{:<15d}{:<15d}\n'\
        .format(self.name,self.hp,self.patt,self.pdef,self.satt, self.sdef)
        out2 = '{:<15s}{:<15s}\n'.format(self.element1, self.element2)
        out3 = ''
        for item in self.moves:
            out3 +='{:<15s}'.format(str(item)) # sorts through list of moves
        out = out1+out2+out3
        return out
    def __repr__(self):
        '''
            This returns the name of the pokemon
        '''
        return self.name


    def get_name(self):
        '''
            This also returns the name of the pokemon
        '''
        return self.name
    
    def get_element1(self):
        '''
            This returns the first element of the pokemon
            Compares to move element to determine damage
        '''
        return self.element1
    
    def get_element2(self):
        '''
             This returns the second element of the pokemon
             Compares to move element to determine damage
        '''
        return self.element2
    
    def get_hp(self):
        '''
            returns only a 0 or greater int for the 
            pokemon's health stat
        '''
        if self.hp > 0:
            return self.hp
        else:
            return 0
    def get_patt(self):
        '''
            THis returns the patt stat of the pokemon
        '''
        return self.patt

    def get_pdef(self):
        '''
            This returns the pdef stat of the pokemon
        '''
        return self.pdef
    
    def get_satt(self):
        '''
            this returns the satt stat of the pokemon
        '''
        return self.satt

    def get_sdef(self):
        '''
            this returns the sdef stat of the pokemon
        '''
        return self.sdef
    
    def get_moves(self):
        '''
            this returns a list of moves of the pokemon
        '''
        return self.moves

    def get_number_moves(self):
        '''
            This returns the number of moves that a pokemon has
        '''
        i = 0
        for item in self.moves:
            i += 1
        return i

    def choose(self,index):
        '''
            This chooses a pokemon and returns it
            only if it exists
        '''
        try:
            out = self.moves
            
            out = out[index]
            
            return out
        except IndexError:
            return None

        
    def show_move_elements(self):
        '''
            this shows the move elemets of a pokemon's moves
            with special formatting
        '''
        out = ''
        for item in self.moves:
            out += '{:<15s}'.format(str(item.get_element()))
        return out


    def show_move_power(self):
        '''
            This returns the power of a pokemon's moves
            with special formatting
        '''
        out = ''
        for item in self.moves:
            out += '{:<15s}'.format(str(item.get_power()))
        return out

    def show_move_accuracy(self):
        '''
            This returns the accuracy of the pokemon's moves
            with special formatting
        '''
        out = ''
        for item in self.moves:
            out += '{:<15s}'.format(str(item.get_accuracy()))
        return out

        
        
    def add_move(self, move):
        '''
            This adds a move to the pokemon if the max
            number of moves hasn't been reached
        '''
        if self.get_number_moves() < 4:
            self.aadd_move = self.moves.append(move)
            return self.add_move
        else:
            pass
    
    def subtract_hp(self, damage):
            #self.hp - damage if (damage < self.hp) else 0
        
            if damage < self.hp:
                self.hp = self.hp - damage
            else:
                self.hp = 0   
    
    def attack(self, move, opponent):
        '''
            This looks at the pokemon;'s elements and move element
            to determine damage done
            **Uses sick formula to return damage**
        '''
        pwr = move.get_power()
        attyp = move.get_attack_type()
        if attyp== 2:
            a, d = self.patt, opponent.pdef
        elif attyp == 3:
            a, d = self.satt, opponent.sdef
        else:
            print("Invalid attack_type, turn skipped.")
            return
        acc = randint(1, 100)
        if acc > move.get_accuracy():
            print('Move missed!')
            return
        mod = 1.0
        # if any of the elements are in the respectice dicts:
        # the modifier is changed based on effectiveness
        if opponent.element1 in is_effective_dictionary[move.element]: 
            mod = mod*2
        elif opponent.element1 in not_effective_dictionary[move.element]:
            mod = mod/2
        elif opponent.element1 in no_effect_dictionary[move.element]:
            mod = 0
        if opponent.element2 in is_effective_dictionary[move.element]:
            mod = mod*2
        elif opponent.element2 in not_effective_dictionary[move.element]:
            mod = mod/2
        elif opponent.element2 in no_effect_dictionary[move.element]:
            mod = 0
        # the mod value determines the effectiveness of the attack
        if mod > 1 and mod != 0:
            print("It's super effective!!!!")
        elif mod < 1 and mod != 0:
            print("Not very effective...")
        elif mod == 0:
            print('No effect!')
        if self.element1 == move.element or self.element2 == move.element:
            mod = mod * 1.5
            
        damage = ((float(pwr*(a/d)*20)/50)+2)*mod
        damage = int(damage)
        opponent.hp = opponent.hp - damage
        #print(damage)
        #print(opponent.subtract_hp(damage))
        #print(opponent.hp)
    