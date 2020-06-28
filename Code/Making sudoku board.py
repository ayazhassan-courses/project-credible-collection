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
# filled sudoku board is valid or not
# by cheking the frequency of each number 
# in each row, coloumn and box.
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

bo_2=[[1,5,0,8,7,3,2,0,6], 
    [3,8,6,5,9,2,7,1,4], 
    [7,2,9,6,4,0,8,3,5], 
    [8,6,3,7,0,5,1,4,9], 
    [9,7,5,3,1,4,6,2,8], 
    [4,1,2,9,6,8,3,5,7], 
    [6,3,0,4,5,7,9,8,2], 
    [5,9,8,0,3,6,4,7,1], 
    [2,4,7,0,8,9,5,6,3]]

bo_3=[ [ 3, 1, 6, 5, 7, 8, 4, 9, 2 ],
         [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
         [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
         [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ],
         [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ],
         [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
         [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ],
         [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
         [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ]

print('____Solved-Board_____')
st_2=time.time()
Solve(bo, 0, 0)
sudoku_board(bo)
ed_2=time.time()
rt_2=ed_2-st_2
print()
#########################
sudoku_board(bo_3)
st=time.time()
Solve(bo_3,0,0)
print('____Solved-Board_____')
sudoku_board(bo_3)
end=time.time()
x=end-st
print()
print("--------------------------RUNTIME for naive approach with first board---------------------------------")
print(rt_2)
t = rt_2 //16

print()

print("--------------------------RUNTIME for naive approach with second board---------------------------------")
print(x)
y = x//16

print()



# Backtracking Algorithm to solve a sudoku board:

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


sudoku_board2(board)
print('____Solved-Board_____')
st_11=time.time()
solution(board)
sudoku_board2(board)
print()
ed_11=time.time()
rt_11=ed_11-st_11
print("------------------------RUNTIME for backtracking approach with first board----------------------")
print(rt_11)
print()
print()
sudoku_board2(bo_3)
print('____Solved-Board_____')
st_12=time.time()
solution(bo_3)
sudoku_board2(bo_3)
print()
ed_12=time.time()
rt_12=ed_12-st_12
print("------------------------RUNTIME for backtracking approach with second board----------------------")
print(rt_12)

#the above code will work at the backend and will make sue that the game is being solved correctly

#------------------------------------------------------------------------------------------------------------------------------------------------------

#---------plotting graph for the results----------------------------------:

#Note:------------------------------------------------------------------------------------------------------
#The naive approach is very inefficient and time consuming as compared to the backtracking approach/algorithm.
#The difference between the runtime of both algorithms is so significant that the bar plot of backtracking 
#is not visible on the graph. Hence, for plotting purposes, a fraction i.e. 1/16th the value of the runtime of 
#the naive approach is taken and plotted with runtime of backtracking. At the time of code, runtime of naive 
#aplgorithm was nearly 98 seconds while runtime for bactracking was around 0.02 seconds for the same sudoku board.
#-----------------------------------------------------------------------------------------------------------

#n.a = naive approach
#b.t = bactracking

graph_x=["n.a (1/16th time)(bo1)","b.t(bo1)","n.a (1/16th time)(bo2)","b.t(bo2)"]
graph_y=(t,rt_11,y,rt_12)
plt.title("Runtime for algorithms used to solve sudoku")
plt.bar(graph_x,graph_y,color="red")
plt.show()



