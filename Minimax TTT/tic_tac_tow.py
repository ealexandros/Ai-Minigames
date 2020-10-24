from p5 import *
from game_functionality import GameFunctionality

# Change this variable if the window is to big for you..
TABLE_SIZE = 700

LINE_WEIGHT = 13.5
LINE_MARGIN = TABLE_SIZE/40

CIRCLE_RADIUS = 120
X_MARGIN = TABLE_SIZE/12

winner = False

def setup():
    size(TABLE_SIZE, TABLE_SIZE)

def draw():
    background(235)

    # Making the Grid lines.
    for i in range(1, 3):
        stroke_weight(LINE_WEIGHT)
        line((i*TABLE_SIZE/3, LINE_MARGIN), (i*TABLE_SIZE/3 ,TABLE_SIZE-LINE_MARGIN))

        stroke_weight(LINE_WEIGHT)
        line((LINE_MARGIN, i*TABLE_SIZE/3), (TABLE_SIZE-LINE_MARGIN ,i*TABLE_SIZE/3))

        # Drawing every time the players Pawns
        draw_players_pawn()

def mouse_clicked(event):
    turn = game.player_turn
    global winner

    if(turn == True and winner == False):
        if(event.x < TABLE_SIZE/3 and event.y < TABLE_SIZE/3):
            game.entry(0, 0, 1)
        elif(event.x < 2*TABLE_SIZE/3 and event.y < TABLE_SIZE/3):
            game.entry(0, 1, 1)
        elif(event.x < 3*TABLE_SIZE/3 and event.y < TABLE_SIZE/3):
            game.entry(0, 2, 1)
        elif(event.x < TABLE_SIZE/3 and event.y < 2*TABLE_SIZE/3):
            game.entry(1, 0, 1)
        elif(event.x < 2*TABLE_SIZE/3 and event.y < 2*TABLE_SIZE/3):
            game.entry(1, 1, 1)
        elif(event.x < 3*TABLE_SIZE/3 and event.y < 2*TABLE_SIZE/3):
            game.entry(1, 2, 1)
        elif(event.x < TABLE_SIZE/3 and event.y < 3*TABLE_SIZE/3):
            game.entry(2, 0, 1)
        elif(event.x < 2*TABLE_SIZE/3 and event.y < 3*TABLE_SIZE/3):
            game.entry(2, 1, 1)
        elif(event.x < 3*TABLE_SIZE/3 and event.y < 3*TABLE_SIZE/3):
            game.entry(2, 2, 1)

    if(game.player_won() != -1):
        winner = True

def draw_players_pawn():
    '''
    This function just draws all the X's and O's on the table based
    on the game.board parameter, which is a [3][3] table.

    If the value is 1 it draws an X else-if it is a 0 it draws a 0.
    '''
    board_table = game.board

    for i in range(1, 4):
        for j in range(1, 4):
            if(board_table[j-1][i-1] == 1):
                stroke_weight(LINE_WEIGHT-6)
                line(((i-1)*TABLE_SIZE/3+X_MARGIN, (j-1)*TABLE_SIZE/3+X_MARGIN),
                    (i*TABLE_SIZE/3-X_MARGIN, j*TABLE_SIZE/3-X_MARGIN))
                stroke_weight(LINE_WEIGHT-6)
                line((i*TABLE_SIZE/3-X_MARGIN, (j-1)*TABLE_SIZE/3+X_MARGIN), 
                    ((i-1)*TABLE_SIZE/3+X_MARGIN, j*TABLE_SIZE/3-X_MARGIN))
            elif(board_table[j-1][i-1] == 0):
                no_fill()
                circle((i*TABLE_SIZE/3-TABLE_SIZE/6, j*TABLE_SIZE/3-TABLE_SIZE/6), CIRCLE_RADIUS)

if(__name__ == "__main__"):
    game = GameFunctionality()
    run()