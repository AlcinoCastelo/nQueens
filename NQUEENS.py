#NRainhas
N = int(input("Entras o numero de Rainhas que queres situar:"))
board = [[0 for i in range(N)] for i in range(N)]
#print(board)
##board = [[0, 0, 0, 0],
##         [0, 0, 0, 0],
##         [0, 0, 0, 0],
##         [0, 0, 0, 0]]

def check_col_diag(board, row, col):
    for i in range(row):
        if board[i][col]==1:
            return False
    for i, j in zip(range(row, -1, -1),range(col, -1,-1)):
        if board[i][j]==1:
            return False
    for i, j in zip(range(row, -1, -1),range(col, N)):
        if board[i][j]==1:
            return False
    return True
#Backtracking
def NQueens(board, row):
    if N==row:
        return True
    for i in range(N):
        if check_col_diag(board, row, i)==True:
            board[row][i]=1
            give = NQueens(board, row+1)
            if give:
                return True
            else:
                board[row][i] = 0
    return False
if NQueens(board, 0)==True:
    for row in board:
        print(row)
else:
    print("Not possible")
