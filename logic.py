import random #this is the inbuild library to get the random value
def Start_Game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)

    return mat

def Random_2(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while mat[r][c] !=0:
        r= random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c]=2

def Status(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "WON"

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return "GAME NOT OVER"

    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] or mat[i][j]==mat[i+1][j]:
                return "GAME NOT OVER"

    for i in range(3):
        if mat[3][i]== mat[3][i+1]:
            return"GAME NOT OVER"

    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "GAME NOT OVER"
    
    return "LOST"

def compress(mat):
    changed = False
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos] = mat[i][j]
                if j!=pos:
                    changed = True
                pos+=1
    return new_mat,changed

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j] = 2*mat[i][j]
                mat[i][j+1]=0
                changed  = True
    return mat,changed

def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat

def move_up(board):
    transpose_matr = transpose(board)
    matr,changed1 = compress(transpose_matr)
    matr,changed2 = merge(matr)
    changed = changed1 or changed2
    matr,temp= compress(matr)
    final_out = transpose(matr)
    return final_out,changed

def move_down(board):
    matr = transpose(board)
    matr = reverse(matr)
    matr,changed1 = compress(matr)
    matr,changed2 = merge(matr)
    changed = changed1 or changed2
    matr,temp = compress(matr)
    matr= reverse(matr)
    final_out = transpose(matr)
    return final_out,changed

def move_right(board):
    matr = reverse(board)
    matr,changed1 = compress(matr)
    matr,changed2 = merge(matr)
    changed = changed1 or changed2
    matr,temp= compress(matr)
    final_out = reverse(matr)
    return final_out,changed

def move_left(board):
    matr,changed1 = compress(board)
    matr,changed2 = merge(matr)
    changed = changed1 or changed2
    matr,temp= compress(matr)
    return matr,changed


