import random
import getpass


#Step 3 – Creating the separate functions for various purposes.
    
  #1. Defining the function to draw the hand diagrams.
def draw_diagrams(ch):
    if(ch=="rock"):
        print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
    elif(ch=="paper"):
        print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
    elif(ch=="scissors"):
        print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)
    else:
        print("WRONG INPUT! CHOOSE AGAIN PLEASE!\n")
  #2. Defining the function to play with the computer.
def begin_game_computer(n):
    score1=0
    score2=0
    for i in range(n):
        print("---------------------------------------------------------------------------")
        print("ROUND NUMBER: ",i+1)
        check = True
        while check:
            p_ch = input("Choose your option: ")
            if(p_ch.lower() in choices):
                check=False
            else:
                print("Wrong Input! Enter Again!")
        c_ch = choices[random.randint(0,2)]
         
        print("\nYOUR CHOICE: ")
        draw_diagrams(p_ch.lower())
        print("\nCOMPUTER's CHOICE: ")
        draw_diagrams(c_ch.lower())
         
        winner = check_win(p_ch,c_ch)
        if(winner==1):
            print("YOU WIN THE ROUND HURRAY!\n")
            score1+=1
        elif(winner==2):
            print("Oh no! Computer wins the round!\n")
            score2+=1
        else:
            print("DRAW ROUND!\n")
    print("---------------------------------------------------------------------------")
    print("FINAL SCORES ARE AS FOLLOWS: ")
    print("YOUR SCORE: ",score1)
    print("COMPUTER's SCORE: ",score2)
    if(score1>score2):
        print("---------------------------------------------------------------------------")
        print("HURRAY YOU WIN! Congratulations!")
        print("---------------------------------------------------------------------------")
    elif(score1<score2):
        print("---------------------------------------------------------------------------")
        print("Computer wins this time! Better Luck next time!")
        print("---------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------")
        print("It's a draw game!")
        print("---------------------------------------------------------------------------")

    # Using The input of both the players and Checking who wins the round by the below function for each of the round(in a for loop)
def check_win(c1,c2):
    if(c1=='rock' and c2=='paper'):
        return 2
    elif(c1=='paper' and c2=='rock'):
        return 1
    elif(c1=='paper' and c2=='scissors'):
        return 2
    elif(c1=='scissors' and c2=='paper'):
        return 1
    elif(c1=='rock' and c2=='scissors'):
        return 1
    elif(c1=='scissors' and c2=='rock'):
        return 2
    elif(c1==c2):
        return 0 

    # Updating the score values: 
  #3. Defining the function to play along with a friend.
def begin_game_friend(n):
    score1=0
    score2=0
    for i in range(n):
        print("---------------------------------------------------------------------------")
        print("ROUND NUMBER: ",i+1)
         
        check = True
        while check:
            p1_ch = getpass.getpass(prompt="Choose your option player 1: ",stream=None)
            if(p1_ch.lower() in choices):
                check=False
            else:
                print("Wrong Input! Enter Again!")
         
        check = True
        while check:
            p2_ch = input("Choose your option player 2: ")
            if(p2_ch.lower() in choices):
                check=False
            else:
                print("Wrong Input! Enter Again!")
         
        print("\nPLAYER 1 CHOICE: ")
        draw_diagrams(p1_ch.lower())
        print("PLAYER 2 CHOICE: ")
        draw_diagrams(p2_ch.lower())
         
        winner = check_win(p1_ch,p2_ch)
        if(winner==1):
            print("Player 1 wins the round!\n")
            score1+=1
        elif(winner==2):
            print("Player 2 wins the round!\n")
            score2+=1
        else:
            print("DRAW ROUND!\n")
     
    print("---------------------------------------------------------------------------")
    print("FINAL SCORES ARE AS FOLLOWS: ")
    print("PLAYER 1 SCORE: ",score1)
    print("PLAYER 2 SCORE: ",score2)
    if(score1>score2):
        print("---------------------------------------------------------------------------")
        print("PLAYER 1 WINS! Congratulations!")
        print("---------------------------------------------------------------------------")
    elif(score1<score2):
        print("---------------------------------------------------------------------------")
        print("PLAYER 2 WINS! Congratulations")
        print("---------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------")
        print("It's a draw game!")
        print("---------------------------------------------------------------------------")


#Step 2 – Printing Greeting Messages and asking the player about how it wants to play the game.

def Info ():
    print ("\tHELLO THERE! WELCOME TO ROCK PAPER SCISSORS GAME!")
    print ("INSTRUCTIONS:\nBoth the players have three choices namely rock, paper and scissors.")
    print ("\nGAME RULES:")
    print ("\tSCISSORS beats PAPER")
    print ("\tPAPER beats ROCK")
    print ("\tROCK beats SCISSORS")
    print ("--------------------------------------------------------------------------")
    print ("Choose between the two options: ")
    print ("\t 1. Play with the computer")
    print ("\t 2. Play with a friend")
    print ("\t 3. Exit Game")

Info ()
choices = ["rock","paper","scissors"]
wrong = True
while wrong:
    try:
        n= int (input ("Enter your choice of Gameplay: "))
        if(n==1):
            wrong = False
            x = int (input ("Enter number of rounds you want to play: "))
            begin_game_computer(x)
        elif(n==2):
            wrong = False
            x = int (input ("Enter number of rounds you want to play: "))
            begin_game_friend(x)
        elif(n==3):
            wrong=False
            print ("\nThank you for playing! \nBye!")
        else:
            print ("Choose Again!")
    except (ValueError):
        print ("INVALID INPUT! Choose Again!")
        wrong=True

#Step 3 – Creating the separate functions for various purposes.
    
  #1. Defining the function to draw the hand diagrams.

  #2. Defining the function to play with the computer.

    # Using The input of both the players and Checking who wins the round by the below function for each of the round(in a for loop)

    # Updating the score values: 
  #3. Defining the function to play along with a friend.























































