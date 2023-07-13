'''
Algorithm:     Roll two dice. Each die has six faces representing values 1, 2, ..., and 6,
               respectively. Check the sum of the two dice. If the sum is 2, 3, or 12
               (called craps), you lose; if the sum is 7 or 11 (called natural), you win;
               if the sum is another value (i.e., 4, 5, 6, 8, 9, or 10), a point is established.
               Continue to roll the dice until either a 7 or the same point value is rolled.
               If 7 is rolled, you lose. Otherwise, you win.
'''

import random

#Deals with the initial rolling of the dice. Sum of 7 or 11 wins. Sum of 2,3, or 12 loses.
#Any other number establishes the point value that will win the game.
def initial(roll):

    sumOfRolls = roll

    if sumOfRolls == 7 or sumOfRolls == 11:
        results = 'You win!'
    elif sumOfRolls == 2 or sumOfRolls == 3 or sumOfRolls == 12:
        results = 'You lose!'
    else:
        print("The sum of your rolls is " + str(sumOfRolls) + ". " +
              "This is the point value. Continuing to roll until a win or loss...")
        results = compare(sumOfRolls)
        
    return results

#Deals with the continued rolling of the dice if a point value is established.
#A sum equaling to the point value wins. A sum of 7 loses.
def compare(roll):
    
    pointValue = roll
    go = 'yes'

    while go == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        rollSum = dice1 + dice2
        print("You have rolled: " + str(dice1) + ", " + str(dice2) +" for a sum of " +
              str(rollSum) + ".")
        if rollSum == pointValue:
            results = 'You win!'
            go = 'no'
        elif rollSum == 7:
            results = 'You lose!'
            go = 'no'
        else:
            go = 'yes'

    return results
            
#Let's the player decide if they would like to continue playing after a win or lose
def restart():
    print()
    play = input("Would you like to play again? Enter yes or no: ")
    print()
    
    if play == 'yes' or play == 'Yes' or play == 'YES':
        game(play)
    else:
        print("You have cancelled the game.")
        exit()

"""
Streamlines the restarting of the game by calling the game() function instead of main() 
so that the instructions only display the first time the program runs.
"""
def game(value):

    answer = value
    
    if answer == 'yes' or answer == 'Yes' or answer == 'YES':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        rollSum = dice1 + dice2
        print("You have rolled: " + str(dice1) + ", " + str(dice2) +" for a sum of " +
              str(rollSum) + ".")

        results = initial(rollSum)
        print(results)
        restart()
    else:
        print("You have cancelled the game.")
        exit() 


#Gives the instructions for the game and initiates the game.
def main():

    print("Casino Game: Craps")
    print()
    print("Instructions: In this game you roll two dice. If the initial roll has a sum of" +
          " 7 or 11, you win! If the initial roll has a sum of 2, 3, or 12, you lose! " +
          "Any other number establishes a point value that must be rolled again in order" +
          " to win. If a 7 is rolled instead, you lose.")
    print()

    answer = input("Would you like to play? Enter yes or no: ")
    print()
    game(answer)
    
    
main()
