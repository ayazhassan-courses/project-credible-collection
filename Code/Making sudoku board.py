import time
from matplotlib import pyplot as plt

#Naive Approach to solve a sudoku board:

#Function used to visualise a (9x9) sudoku board:
def sudoku_board(b):
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



# Function used to check whether the 
# filled sudoku board is valid or not.
def valid(bo):
    row_d = {0:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            1:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            2:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            3:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
            4:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
            5:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            6:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            7:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            8:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}}

    col_d = {0:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            1:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            2:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            3:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
            4:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
            5:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            6:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            7:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            8:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}}

    box_d = {0:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            1:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            2:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            3:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
            4:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0},
            5:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            6:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            7:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}, 
            8:{1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}}

    for row in range(9):
        for col in range(9):

            row_d[row][bo[row][col]]+=1
            col_d[col][bo[row][col]]+=1

            if col//3==0:
                if row<=8:
                    box=6
                if row<6:
                    box=3
                if row<3:
                    box=0
            elif col//3==1:
                if row<=8:
                    box=7
                if row<6:
                    box=4
                if row<3:
                    box=1
            elif col//3==2:
                if row<=8:
                    box=8
                if row<6:
                    box=5
                if row<3:
                    box=2    
            box_d[box][bo[row][col]]+=1

            if row_d[row][bo[row][col]]>1 or col_d[col][bo[row][col]]>1 or box_d[box][bo[row][col]]>1:
                return False
    return True
            


# Function uses recursion to fill out all 
# the empty spaces to fill the board.
def Solve(bo, i, j):
    if i==len(bo)-1 and j==len(bo):
        if valid(bo):
            return True
        return False

    if j==len(bo):
        i+=1
        j=0

    if bo[i][j]!=0:
        return Solve(bo, i, j+1)

    for guess in range(1,10):

        bo[i][j]=guess

        if Solve(bo, i, j+1):
            return True
        bo[i][j]=0

    return False

bo=[[1,5,0,8,7,3,2,0,6], 
    [3,8,6,5,9,2,7,1,4], 
    [7,2,9,6,4,0,8,3,5], 
    [8,6,3,7,0,5,1,4,9], 
    [9,7,5,3,1,4,6,2,8], 
    [4,1,2,9,6,8,3,5,7], 
    [6,3,0,4,5,7,9,8,2], 
    [5,9,8,0,3,6,4,7,1], 
    [2,4,7,0,8,9,5,6,3]]

sudoku_board(bo)
print('____Solved-Board_____')
st_2=time.time()
Solve(bo, 0, 0)
sudoku_board(bo)
ed_2=time.time()
rt_2=ed_2-st_2
print("--------------------------RUNTIME for naive approach---------------------------------")
print(rt_2)
t = rt_2 //16

print()
print('2nd Algo')
print()







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
