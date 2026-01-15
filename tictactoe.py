import random
import sys
import os
from tkinter import*
import time



def death_move_detection():
    #spaces
    
    #available_spaces give list of possible moves
    
    #for each possible move
    for possible_move in available_spaces():
        spaces[possible_move] = 2
        possible_wins = death_count()
        if len(possible_wins) >= 2:
            print("Double threat found")
            print("Move taken in", possible_move)
            return True
        else:
            spaces[possible_move] = 0
    print("Double threat not found")
    return False

def score_board():
    global spaces
    score = 0
    #rows
    row1 = [spaces[0], spaces[1], spaces[2]]
    row2 = [spaces[3], spaces[4], spaces[5]]
    row3 = [spaces[6], spaces[7], spaces[8]]

    #columns
    col1 = [spaces[0], spaces[3], spaces[6]]
    col2 = [spaces[1], spaces[4], spaces[7]]
    col3 = [spaces[2], spaces[5], spaces[8]]

    #diagonals
    diag1 = [spaces[0], spaces[4], spaces[8]]
    diag2 = [spaces[2], spaces[4], spaces[6]]

    lines = [row1, row2, row3, col1, col2, col3, diag1, diag2]

    for line in lines:
        if line.count(2) == 2 and line.count(0) == 1:
            score += 10
        if line.count(1) == 2 and line.count(0) == 1:
            score -= 8

    return score
    




def available_spaces():
    #create an empty list called 'available_spaces'
    available_spaces = []
    #for each item in spaces
    n = 0
    for item in spaces:
        #if the contents of the item is 0
        if item == 0:
            #append the index of that item to the list 'available_spaces'
            available_spaces.append(n)
        n += 1
    #return the final list
    return available_spaces

def take_the_win():
    global spaces
    spaces = [0, 0, 1,
                    2, 2, 0,
                    1, 0, 0]
    num = 0

def detect_win():
    """
    Detects if a player has won.
    spaces: list of 9 integers (0 = empty, 1 = player, 2 = computer)
    Returns: 'player', 'computer', or False
    """
    global spaces
    winner = 0  # 0 means no winner yet
    game_over = False

    # check diagonals
    if spaces[0] == spaces[4] == spaces[8] != 0:
        game_over = True
        winner = spaces[0]

    if spaces[6] == spaces[4] == spaces[2] != 0:
        game_over = True
        winner = spaces[6]

    # check horizontals
    for x in range(0, 3):
        start = x * 3
        if spaces[start] == spaces[start + 1] == spaces[start + 2] != 0:
            game_over = True
            winner = spaces[start]


    # check verticals
    for x in range(0, 3):
        start = x  # start positions 0, 1, 2 (top row of grid)
        if spaces[start] == spaces[start + 3] == spaces[start + 6] != 0:
            game_over = True
            winner = spaces[start]


    # convert winner number into text: 1 => player, 2 => computer
    if winner == 1:
        return 'player'
    elif winner == 2:
        return 'computer'
    else:
        return False

def exitConfirm():
    rosot = Tk()
    rosot.wm_title('ARE YOU SURE YOU WANT TO EXIT?')
    rosot.minsize(width=400, height=350)

    exeitbutton = Button(rosot, text='Exit', command=exitConfirmer)  
    exeitbutton.config(width=10, height=5)
    exeitbutton.grid(row=3, column=3, columnspan=5)
    
def exitConfirmer():
    sys.exit(0)

def start(): #prepares root window
    #declare global called 'root'from createstart.py import start
    global root
    global score_label
    #build tkinter window
    root = Tk()
    root.wm_title('TINK TANK TONK')
    root.minsize(width=400, height=350)
    root.update_idletasks()
    print("width: ",root.winfo_width())

    exitbutton = Button(root, text='Exit', command=exitConfirmer)  
    exitbutton.config(width=4, height=2)
    exitbutton.grid(row=0, column=7, columnspan=1)

    print(root.winfo_height())
    print(root.winfo_width())


    score_label = Label(root, text="Score: 0")
    score_label.grid(row=6, column=0, columnspan=5)

    Button(root, text='Restart', command=restart).grid(row=6, column=0, columnspan=5)

        # create scoreboard labels to the right of the grid
    global player_score_label, computer_score_label, ties_score_label

    player_score_label = Label(root, text="Player: 0")
    player_score_label.grid(row=0, column=6, sticky='w')
    computer_score_label = Label(root, text="  Computer: 0")
    computer_score_label.grid(row=2, column=6, sticky='w')
    ties_score_label = Label(root, text="Ties: 0")
    ties_score_label.grid(row=4, column=6, sticky='w')

    #call update_board function
    # schedule the evade behaviour (keeps window away from the mouse)
    update_board()

    #building grid (horizonal and vertical lines) using loop (use a 'for' loop?)
    #loop to make variable r go 0, 2,
    for r in [0,1,2,3,4]:
        Label(root, text='|').grid(row=r, column=1)
        Label(root, text='|').grid(row=r, column=3)
    for c in [0,2,4]:
        Label(root, text='|').grid(row=c, column=1)
        Label(root, text='|').grid(row=c, column=3)
    #end of loop
    #loop to make c go 0,1,2,3,4
    #.....?
        Label(root, text='-').grid(row=1,column=c)
        Label(root, text='-').grid(row=3,column=c)
    #end of loop

    #call update_board function
    update_board()

    # start the Tk event loop (mainloop) after UI setup
    root.mainloop()


def restart(): #restarts game
    global spaces
    spaces = [0,0,0,0,0,0,0,0,0]
    Label(root, text=[]).grid(row=5, column=0, columnspan=5)
    Label(root, text="           Game restarted           ").grid(row=5, column=0, columnspan=5)
    # allow scoreboard to persist but mark this new match as not finalised
    global match_finalised
    match_finalised = False
    update_board()
    
def take_moves (usermove): #facilitates move
    print("Usermove requested:", usermove)
        #player move
    global turn
    
    turn = turn + 1
    print("Available spaces:", available_spaces())
    if usermove in available_spaces(): #if space requested by GUI is available (which it should be!)
        spaces[usermove] = 1 #save user move
    else:
        print("Error in function take_moves: impossible move requested.")
        sys.exit(0)
    if detect_win()==False: #if nobody has won yet, let the computer take a move
        if len(available_spaces())>0: #computer move
            #logic for computer to take moves
            possible_move = ai()
            if possible_move == "none found":
                # try to block the player if they have two in a row
                block_move = block_player()
                if block_move == "none found":
                    if death_move_detection() == False:
                        print("Taking a random move")
                        move = random.choice(available_spaces()) #just random selection
                else:
                    print("Blocking player move at position", block_move)
                    move = block_move
            else:
                print("Taking the win found, taking move")
                move = possible_move
            spaces[move] = 2 #save computer move
        else:
            game_over = True #no spaces available, must be the end of the game
    update_board() #refresh board


def update_board():  # function to check if anyone has won and update the board
    # check if anyone has won
    global labels
    global win_text
    global buttons
    global winner
    global player_wins, computer_wins, ties
    global player_score_label, computer_score_label, ties_score_label
    global match_finalised
    # if detect win returns false, no winner, otherwise winner's name is returned
    win_result = detect_win()
    if win_result != False:  # if someone has won
        winner = win_result  # get name of winner
        Label(root, text="                Winner is: " + winner + "                   ").grid(row=5, column=0, columnspan=5)
        if not match_finalised:  # only tally once per finished match
            if winner == 'player':
                player_wins += 1
                player_score_label.config(text=f"Player: {player_wins}")
            elif winner == 'computer':
                computer_wins += 1
                computer_score_label.config(text=f"Computer: {computer_wins}")
            match_finalised = True
    elif not (0 in spaces):  # if nobody has won AND there are no blank spaces...
        # ....it must be a draw
        Label(root, text='        Draw!         ').grid(row=5, column=0, columnspan=5) # output 'draw'
        if not match_finalised:  # only tally once per finished match
            ties += 1
            ties_score_label.config(text=f"Ties: {ties}")
            match_finalised = True

    # clear out TK buttons for refresh
    for button in buttons:
        button.grid_forget()

    # clear out TK labels for refresh
    for label in labels:
        label.grid_forget()

    # clear the lists in-place so references remain valid (no need for global)
    del buttons[:]
    del labels[:]

    # create and position buttons and labels using loops
    x = 0  # x position
    y = 0  # y position
    n = 0  # index of button/label
    for space in spaces:
        if space == 0:  # space not used yet, display button
            button = Button(root, text="  ", command=lambda n=n: take_moves(n))
            button.config(width=10, height=5)
            button.config(font=("Arial", 20))
            button.grid(row=y, column=x)
            buttons.append(button)
        else:  # space has been used, so we should display value
            label = Label(root, text=decode_symbol(space))  # convert 1/2 into X/O
            label.config(font=("Arial", 20))
            label.config(width=10, height=5)
            label.grid(row=y, column=x)
            labels.append(label)
        x = x + 2  # move across 2
        if x > 4:  # if end of row
            x = 0  # ...move to start
            y = y + 2  # ...of next row
        n = n + 1  # increment button/label index
    # `root.mainloop()` is started by `start()` so this function can be
    # called repeatedly to refresh the UI without re-entering the event loop.
    
def decode_symbol(code): #change code to symbol i.e. 0/1/2 => space/X/O
    import sys
    if code == 0:
        return "[]"
    elif code == 1:
        return "X"
    elif code == 2:
        return "O"
    else:
        print("Error decdoding symbol")


def initialise():
    #declare spaces global
    global spaces
    spaces = [0,0,0,0,0,0,0,0,0]
    #declare game_over global and present values
    global game_over
    game_over = True
    #declare global buttons (holder for Tk button variables)
    global buttons
    buttons = []
    #declare global labels  (holder for Tk label variables)
    global labels
    labels = []
    global turn
    turn = 0
        # scoreboard counters
    global player_wins, computer_wins, ties
    player_wins = 0
    computer_wins = 0
    ties = 0

    # GUI label placeholders for scoreboard
    global player_score_label, computer_score_label, ties_score_label
    player_score_label = None
    computer_score_label = None
    ties_score_label = None

    # flag to ensure we only tally a finished match once
    global match_finalised
    match_finalised = False

    global score_label
    score_label = None
    

    #call start function to start running the program
    start()
    
def ai():
    global spaces


    #row

    row1 = [spaces[0], spaces[1], spaces[2]]
    row2 = [spaces[3], spaces[4], spaces[5]]
    row3 = [spaces[6], spaces[7], spaces[8]]

    #column

    col1 = [spaces[0], spaces[3], spaces[6]]
    col2 = [spaces[1], spaces[4], spaces[7]]
    col3 = [spaces[2], spaces[5], spaces[8]]

    #diagonal

    diag1 = [spaces[0], spaces[4], spaces[8]]
    diag2 = [spaces[2], spaces[4], spaces[6]]

    #row

    if row1.count(2) == 2 and row1.count(0) == 1:
        win_available_at = row1.index(0)
        print("row 1 available win @ position", win_available_at)
        return win_available_at

    if row2.count(2) == 2 and row2.count(0) == 1:
        win_available_at = row2.index(0) + 3
        print("row 2 available win @ position", win_available_at)
        return win_available_at
        
    if row3.count(2) == 2 and row3.count(0) == 1:
        win_available_at = row3.index(0) + 6
        print("row 3 available win @ position", win_available_at)
        return win_available_at
        
    #column
        
    if col1.count(2) == 2 and col1.count(0) == 1:
        win_available_at =col1.index(0) *3
        print("col 1 available win @ position", win_available_at)
        return win_available_at

    if col2.count(2) == 2 and col2.count(0) == 1:
        win_available_at = (col2.index(0) *3) + 1
        print("col 2 available win @ position", win_available_at)
        return win_available_at
        
    if col3.count(2) == 2 and col3.count(0) == 1:
        win_available_at = (col3.index(0) *3) + 2
        print("col 3 available win @ position", win_available_at)
        return win_available_at

    #diagonal

    if diag1.count(2) == 2 and diag1.count(0) == 1:
        win_available_at =diag1.index(0) *4
        print("diag 1 available win @ position", win_available_at)
        return win_available_at

    if diag2.count(2) == 2 and diag2.count(0) == 1:
        win_available_at = (diag2.index(0) *2) + 2
        print("diag 2 available win @ position", win_available_at)
        return win_available_at
    return "none found"
    
def block_player():
    """
    If the player (1) has two in a row and the third cell is empty,
    return the index (0-8) where the bot should play to block.
    If no immediate block is needed, return "none found".
    """
    global spaces

    #row
    row1 = [spaces[0], spaces[1], spaces[2]]
    row2 = [spaces[3], spaces[4], spaces[5]]
    row3 = [spaces[6], spaces[7], spaces[8]]

    #column
    col1 = [spaces[0], spaces[3], spaces[6]]
    col2 = [spaces[1], spaces[4], spaces[7]]
    col3 = [spaces[2], spaces[5], spaces[8]]

    #diagonal
    diag1 = [spaces[0], spaces[4], spaces[8]]
    diag2 = [spaces[2], spaces[4], spaces[6]]

    # rows
    if row1.count(1) == 2 and row1.count(0) == 1:
        block_at = row1.index(0)
        print("Blocking row 1 at position", block_at)
        return block_at

    if row2.count(1) == 2 and row2.count(0) == 1:
        block_at = row2.index(0) + 3
        print("Blocking row 2 at position", block_at)
        return block_at

    if row3.count(1) == 2 and row3.count(0) == 1:
        block_at = row3.index(0) + 6
        print("Blocking row 3 at position", block_at)
        return block_at

    # columns
    if col1.count(1) == 2 and col1.count(0) == 1:
        block_at = col1.index(0) * 3
        print("Blocking col 1 at position", block_at)
        return block_at

    if col2.count(1) == 2 and col2.count(0) == 1:
        block_at = (col2.index(0) * 3) + 1
        print("Blocking col 2 at position", block_at)
        return block_at

    if col3.count(1) == 2 and col3.count(0) == 1:
        block_at = (col3.index(0) * 3) + 2
        print("Blocking col 3 at position", block_at)
        return block_at

    # diagonals
    if diag1.count(1) == 2 and diag1.count(0) == 1:
        block_at = diag1.index(0) * 4
        print("Blocking diag 1 at position", block_at)
        return block_at

    if diag2.count(1) == 2 and diag2.count(0) == 1:
        block_at = (diag2.index(0) * 2) + 2
        print("Blocking diag 2 at position", block_at)
        return block_at

    return "none found"

def artificialé_intellegensamos():
    global spaces


    #row

    row1 = [spaces[0], spaces[1], spaces[2]]
    row2 = [spaces[3], spaces[4], spaces[5]]
    row3 = [spaces[6], spaces[7], spaces[8]]

    #column

    col1 = [spaces[0], spaces[3], spaces[6]]
    col2 = [spaces[1], spaces[4], spaces[7]]
    col3 = [spaces[2], spaces[5], spaces[8]]

    #diagonal

    diag1 = [spaces[0], spaces[4], spaces[8]]
    diag2 = [spaces[2], spaces[4], spaces[6]]

    #row

    if row1.count(2) == 2 and row1.count(0) == 1:
        win_prevented_at = row1.index(0)
        print("row 1 available win @ position", win_prevented_at)
        return win_prevented_at

    if row2.count(2) == 2 and row2.count(0) == 1:
        win_prevented_at = row2.index(0) + 3
        print("row 2 available win @ position", win_prevented_at)
        return win_prevented_at
        
    if row3.count(2) == 2 and row3.count(0) == 1:
        win_prevented_at = row3.index(0) + 6
        print("row 3 available win @ position", win_prevented_at)
        return win_prevented_at
        
    #column
        
    if col1.count(2) == 2 and col1.count(0) == 1:
        win_prevented_at =col1.index(0) *3
        print("col 1 available win @ position", win_prevented_at)
        return win_prevented_at

    if col2.count(2) == 2 and col2.count(0) == 1:
        win_prevented_at = (col2.index(0) *3) + 1
        print("col 2 available win @ position", win_prevented_at)
        return win_prevented_at
        
    if col3.count(2) == 2 and col3.count(0) == 1:
        win_prevented_at = (col3.index(0) *3) + 2
        print("col 3 available win @ position", win_prevented_at)
        return win_prevented_at

    #diagonal

    if diag1.count(2) == 2 and diag1.count(0) == 1:
        win_prevented_at =diag1.index(0) *4
        print("diag 1 available win @ position", win_prevented_at)
        return win_prevented_at

    if diag2.count(2) == 2 and diag2.count(0) == 1:
        win_prevented_at = (diag2.index(0) *2) + 2
        print("diag 2 available win @ position", win_prevented_at)
        return win_prevented_at
    return "none found"


def death_count():
    global spaces

    possible_death_moves = []
    #row

    row1 = [spaces[0], spaces[1], spaces[2]]
    row2 = [spaces[3], spaces[4], spaces[5]]
    row3 = [spaces[6], spaces[7], spaces[8]]

    #column

    col1 = [spaces[0], spaces[3], spaces[6]]
    col2 = [spaces[1], spaces[4], spaces[7]]
    col3 = [spaces[2], spaces[5], spaces[8]]

    #diagonal

    diag1 = [spaces[0], spaces[4], spaces[8]]
    diag2 = [spaces[2], spaces[4], spaces[6]]

    #row

    if row1.count(2) == 2 and row1.count(0) == 1:
        win_available_at = row1.index(0)
        print("row 1 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)

    if row2.count(2) == 2 and row2.count(0) == 1:
        win_available_at = row2.index(0) + 3
        print("row 2 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)
        
    if row3.count(2) == 2 and row3.count(0) == 1:
        win_available_at = row3.index(0) + 6
        print("row 3 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)
        
    #column
        
    if col1.count(2) == 2 and col1.count(0) == 1:
        win_available_at =col1.index(0) *3
        print("col 1 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)

    if col2.count(2) == 2 and col2.count(0) == 1:
        win_available_at = (col2.index(0) *3) + 1
        print("col 2 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)
        
    if col3.count(2) == 2 and col3.count(0) == 1:
        win_available_at = (col3.index(0) *3) + 2
        print("col 3 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)

    #diagonal

    if diag1.count(2) == 2 and diag1.count(0) == 1:
        win_available_at =diag1.index(0) *4
        print("diag 1 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)

    if diag2.count(2) == 2 and diag2.count(0) == 1:
        win_available_at = (diag2.index(0) *2) + 2
        print("diag 2 available win @ position", win_available_at)
        possible_death_moves.append(win_available_at)
    return possible_death_moves
    
    

    
initialise()