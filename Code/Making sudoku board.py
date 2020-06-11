board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

def solution(b):

    #Base case for recursion.
    position = empty(b)  
    if not position:
        return True
    else:
        row,col=position

    for a in range(1,10):
        if check(b, a, (row,col)):
            b[row][col]=a

            if solution(b):
                return True

            b[row][col]=0

    return False


def check(b, number, position):

    
    for i in range(len(b)):
        if b[i][position[1]]==number and i!=position[0]:
            return False 


    for j in range(len(b[0])):
        if b[position[0]][j]==number and j!=position[1]:
            return False





    #Checking entry in individual boxes.
    row_check=position[0]//3
    col_check=position[1]//3
    for i in range(row_check*3, row_check*3+3):
        for j in range(col_check*3, col_check*3+3):
            if b[i][j]==number and (i,j)!=position:
                return False

    return True


def sudoku_board(b):
    #Function used to make a (9x9) sudoku board:

    for x in range(len(b)):
        if x%3==0 and x!=0:
            print('- - - - - - - - - - -')

        for y in range(len(b[0])):
            if y%3==0 and y!=0:
              print('|', end=' ')
      
            if y==len(b[0])-1:
              print(b[x][y])
      
            else:
              print(b[x][y], end=' ')
sudoku_board(board)
#in the code above the nested list is being converted into a sudoku board using for loops.

def empty(b):
    #Function used to find position of empty boxes on the sudoku board.
    for row in range(len(b)):
        for col in range(len(b[0])):
            if b[row][col]==0:
                return (row , col)

    # If no empty boxes left:
    return None


solution(board)
sudoku_board(board)
#the above code will work at the backend and will make sue that the game is being solved correctly 
