import sys

name1 = input("Player 1, what is your name? ")
name2 = input("Player 2, what is your name? ")

player1 = input("%s, please input 'Rock', 'Paper', or 'Scissors': " %name1).lower()

player2 = input("%s, please input 'Rock', 'Paper', or 'Scissors': " %name2).lower()

def compare(p1,p2,name1,name2):
    if p1 == p2:
        return("Its a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return(f"{name1}'s Rock Wins!")
        elif p2 == 'paper':
            return( f"{name2}'s Paper Wins!")
    elif p1 == 'scissors':
        if p2 == 'rock':
            return( f"{name2}'s Rock Wins!")
        elif p2 == 'paper':
            return (f"{name1}'s Scissors Wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            return(f"{name1}'s Paper Wins!")
        elif p2 == 'scissors':
            return(f"{name2}'s Scissors Wins!")
    else:
        return("Invalid input, please enter either Rock, Paper or Scissors. Please Try Again!")
        sys.exit()

print(compare(player1,player2,name1, name2))