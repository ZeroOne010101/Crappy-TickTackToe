import random
import os

# making the board
board = []
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append('#')

# the players
players = ['O','X']





# Availability components
available = {
                '1' : ['1','2','3'],
                '2' : ['1','2','3'],
                '3' : ['1','2','3']
            }

def is_available(instring):
    if instring[2] in available[instring[0]]:
        return True
    else:
        return False
    
def make_unavailable(instring):
    global available
    available[instring[0]][int(instring[2])-1] = ''




# Input Loop
# decide which player starts randomly
player = random.choice(players)
def pturn():
    global player
    while True:
        pin = input(f'it\'s {player}\'s turn! format: row column: ')
        try:
            if is_available(pin):
                board[int(pin[0])-1][int(pin[2])-1] = player
                make_unavailable(pin)
                if player == 'X': player = 'O'
                else: player = 'X'
                break
            else:
                print('There is already a mark there.')
        except:
            print('Input not supported')
    return ''



# Victory condition
game_decided = False
def check_for_victory():
    global game_decided
    for i in range(3):
        for player in players:
            if player in board[0][i] and player in board[1][i] and player in board[2][i]:
                game_decided = True
                return f'The Game has been decided! {player} wins!'
            elif player in board[i][0] and player in board[i][1] and player in board[i][2]:
                game_decided = True
                return f'The Game has been decided! {player} wins!'
            elif player in board[0][0] and player in board[1][1] and player in board[2][2]:
                game_decided = True
                return f'The Game has been decided! {player} wins!'
            elif player in board[0][2] and player in board[1][1] and player in board[2][0]:
                game_decided = True
                return f'The Game has been decided! {player} wins!'
    return ''
    
    

# Board-string constructor    
def boarddraw():
    boardstring = ''
    for i in range(3):
        for j in range(3):
            boardstring += f'{board[i][j]} '
        boardstring += '\n'
    return boardstring




def main():
    while not (game_decided):
        print(boarddraw())
        print(f'{pturn()}\n')
        _=os.system("clear")
        print(check_for_victory())
        
if __name__ == '__main__':
    main()
