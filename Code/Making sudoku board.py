a = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def make_board(a):
    x=len(a)
    for i in range(len(a)):
        if i%3==0 and i!=0:
            print("---"*x)
        for j in range(len(a[i])):
            if j%3==0 and j!=0:
                print("|",end="")
            if j==len(a[i])-1:
                print(a[i][j])
            else:
                print(a[i][j],end=" ")
        
def find_empty_box(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==0:
                return (i,j)
            

print(make_board(a))