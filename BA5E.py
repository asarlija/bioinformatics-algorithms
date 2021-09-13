"""
A solution to a Rosalind bioinformatics problem
Problem Title: Find a Highest-Scoring Alignment of Two Strings
Rosalind ID: BA5E
URL: http://rosalind.info/problems/ba5e/
"""

def getPenality():
    penality={
    "A":[4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
    "C":[0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
    "D":[-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
    "E":[-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
    "F":[-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
    "G":[0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
    "H":[-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
    "I":[-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
    "K":[-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
    "L":[-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
    "M":[-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
    "N":[-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
    "P":[-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
    "Q":[-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
    "R":[-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
    "S":[1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
    "T":[0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
    "V":[0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
    "W":[-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
    "Y":[-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
    }
    return penality


def getInedexOfLetter():
    index={
    "A":0,
    "C":1,
    "D":2,
    "E":3,
    "F":4,
    "G":5,
    "H":6,
    "I":7,
    "K":8,
    "L":9,
    "M":10,
    "N":11,
    "P":12,
    "Q":13,
    "R":14,
    "S":15,
    "T":16,
    "V":17,
    "W":18,
    "Y":19
    }
    return index

def globalAlignment(first,second):
    s=[]
    for i in range(0,len(first)+1):
        s.append([0]*(len(second)+1))

    #for first column (σ = 5)
    for i in range(1,len(first)+1):
        s[i][0]=s[i-1][0]-5

    #for first row (σ = 5)
    for i in range(1,len(second)+1):
        s[0][i]=s[0][i-1]-5

    backtrack=[]
    for i in range(0,len(first)+1):
        backtrack.append([""]*(len(second)+1))
    #for first column 
    for i in range(1,len(first)+1):
        backtrack[i][0]="D"
    #for first row 
    for i in range(1,len(second)+1):
        backtrack[0][i]="R"

    penality=getPenality()
    index=getInedexOfLetter()

    for i in range(1,len(first)+1):
        for j in range(1,len(second)+1):
            s[i][j]=max(s[i-1][j]-5,s[i][j-1]-5,s[i-1][j-1]+penality[first[i-1]][index[second[j-1]]])
            if s[i][j]==s[i-1][j]-5:
                backtrack[i][j]="D"
            elif s[i][j]==s[i][j-1]-5:
                backtrack[i][j]=="R"
            else:
                backtrack[i][j]="diag"
    newFirst=""
    newSecond=""
    newFirst,newSecond=moves_to_string(first,second,AlignmentRecontructionMoves(backtrack))
    return str(s[len(first)][len(second)])+"\n"+newFirst+"\n"+newSecond

def moves_to_string(first,second,moves):
    pointer_1=0
    pointer_2=0
    v1=[]
    v2=[]

    for move in moves:
        if move=="D": #insert "-" on second, first the same 
            v1.append(first[pointer_1])
            pointer_1+=1
            v2.append("-")
        elif move=="R":
            v1.append("-")
            v2.append(second[pointer_2])
            pointer_2+=1
        else:
            v1.append(first[pointer_1])
            pointer_1+=1
            v2.append(second[pointer_2])
            pointer_2+=1
    return "".join(v1),"".join(v2)

def AlignmentRecontructionMoves(backtrack):
    n=len(backtrack)-1
    m=len(backtrack[0])-1
    moves=[]

    while n>0 or m>0:
        moves.append(backtrack[n][m])
        if backtrack[n][m]=="D":
            n-=1
        elif backtrack[n][m]=="R":
            m-=1
        else:
            n-=1
            m-=1
    return moves[::-1]

x="""PLEASANTLY
MEANLY"""
inlines=x.split()
first=inlines[0]
second=inlines[1]
result=globalAlignment(first,second)
print(result)
        
    
    
                

    
