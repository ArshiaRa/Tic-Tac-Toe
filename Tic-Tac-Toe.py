
def Check(board , symbol):
    if board[0][0] + board[0][1] + board[0][2] == symbol:
        return True
    elif board[1][0] + board[1][1] + board[1][2] == symbol:
        return True
    elif board[2][0] + board[2][1] + board[2][2] == symbol:
        return True
    elif board[0][0] + board[1][0] + board[2][0] == symbol:
        return True
    elif board[0][1] + board[1][1] + board[2][1] == symbol:
        return True
    elif board[0][2] + board[1][2] + board[2][2] == symbol:
        return True
    elif board[0][2] + board[1][1] + board[2][0] == symbol:
        return True
    elif board[2][2] + board[1][1] + board[0][0] == symbol:
        return True
    else:
        return False
    
def Result(board):
    global resume
   
    Xnumber = sum(x.count('X') for x in board)
    Onumber = sum(y.count('O') for y in board)
    if Check(board , "XXX"):
        print("X wins")
        resume = False
    elif Check(board , "OOO"):
        print("O wins")
        resume = False
    elif Xnumber + Onumber == 9:
        print("Draw")
        resume = False
        
def show():
    print("---------")
    print("| " + cells2[0][2] + " " + cells2[1][2] + " " + cells2[2][2] + " |")
    print("| " + cells2[0][1] + " " + cells2[1][1] + " " + cells2[2][1] + " |")
    print("| " + cells2[0][0] + " " + cells2[1][0] + " " + cells2[2][0] + " |")
    print("---------")
    
cells=["_","_","_","_","_","_","_","_","_"]
Player_X = True
Player_O = False
resume = True
cols = 3
rows = 3
cells2 = [[0 for i in range(cols)] for j in range(rows)]

print("---------")
print(f"""| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |""")
print("---------")

cells2[0][0] = cells[6]
cells2[0][1] = cells[3]
cells2[0][2] = cells[0]
cells2[1][0] = cells[7]
cells2[1][1] = cells[4]
cells2[1][2] = cells[1]
cells2[2][0] = cells[8]
cells2[2][1] = cells[5]
cells2[2][2] = cells[2]
error2 = "You should enter numbers!"
print("Enter the coordinates:")
while resume:
    try:
        a, b = input().split()
    except ValueError:
            print("You should enter numbers!")
            continue
    if not a or not b :
        print("You should enter numbers!")
        continue
    if not( a.isdigit() and b.isdigit()):
        print("You should enter numbers!")
        continue
    elif int(a) > 3 or int(b) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif cells2[int(a) - 1][int(b) - 1] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    else:
        if Player_X:
            cells2[int(a) - 1][int(b) - 1] = 'X'
            Player_X = False
            Player_O = True
        else:
            cells2[int(a) - 1][int(b) - 1] = 'O'
            Player_X = True
            Player_O = False
        show()
        Result(cells2)
        
        

    



