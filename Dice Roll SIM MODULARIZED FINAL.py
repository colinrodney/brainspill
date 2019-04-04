# Dice Roll Simulator
# Tested/ Working 04/04/2019
# 5 Small projects for the Python Beginner
# Northwestern University Knight Lab



''' Create simple dice rolling simulator

Development Outline
- Import modules
    - random module
    
- Define functions
    - setup function to roll dice 

- Test / Debug
    -
'''

import random

##def throw(x,y): # x = lower bound-(1) / y = upper bound-(6)
##    ''' Rolls dice - die 1 and 2 take randomly generated values '''
##    dice_one = random.randint(x,y)
##    dice_two = random.randint(x,y)
##    return(dice_one,dice_two)
##    # once completed - script returns value(s) to point of function call (Line 32)


def main(): # chg 330 PM
    ''' Dice Roll Simulator'''
    ready = True
    
    while ready: # negates ready from False > True by use of not keyword...
        roll = input("Ready to roll? Y = Yes / N = No: ")
        if roll.lower() == 'y': # .lower() method returns a copy of value of roll in lowercase.
            result = throw(1,6) # invokes throw() function sending 1 and 6 as arguments

            if result[0] ==  1 and result[1] == 1: # result of random throw @ both index positions is 1 and 1:
                print("You've rolled a ", result[0] , "and a " , result[1], "  \n- SNAKE EYES!")
                ready = not ready
                roll_again()
                       
            elif result[0] ==  result[1]: # result of throw @ both index positions are equivalent and NOT 1 and 1
                print("You've rolled a ", result[0] , "and a " , result[1], " \n- 2 OF A KIND!")
                ready = not ready
                roll_again()
                           
            else: # result of throw @ both index positions all other conditions
                print("You've rolled a ", result[0] , "and a " , result[1])
                ready = not ready
                roll_again()
                
        else:
            ready = not ready
            print('It was fun playing with you!' "\n" 'to play again type main() and press enter.')

def throw(x,y): # x = lower bound-(1) / y = upper bound-(6)
    ''' Rolls dice - die 1 and 2 take randomly generated values '''
    dice_one = random.randint(x,y)
    dice_two = random.randint(x,y)
    return(dice_one,dice_two)
    # once completed - script returns value(s) to point of function call (Line 32)

                      
def roll_again():
    ''' Offers user option to roll again'''
    main() # thsi will chg ready flag from False > True since ready is True in main()

    
# function calls
main()




    
    
    
    

    
