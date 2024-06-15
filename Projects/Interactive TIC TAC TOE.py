#display something visual to the user
# let the user update through itneraction
# update variables
# display the updated visual

# create rows with a func and get the position row1[1] = 'X' - center position, for that use int(input)

#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
import random
def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    
test_board = [' ']*10
print(display_board(test_board))

#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)

player1_marker, player2_marker = player_input()

#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position] = marker
    
#**Step 4: Write a function that takes in a board and checks to see if someone has won. **
def win_check(board,mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] and board[7]) or (board[8] == mark and board[5] and board[2]) or (board[9] == mark and board[6] and board[3]) or (board[1] == mark and board [5] == mark and board[9] == mark) or (board[7] == mark and board [5] and board[3])

#Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board,position):
    return board[postion] == ''

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)' ))
    return position

#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    input("Play again? Enter Yes or No: ")
    return choice == 'Yes'

#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

