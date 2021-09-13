"""
A solution to a Rosalind bioinformatics problem
Problem Title: Find the Length of a Longest Path in a Manhattan-like Grid
Rosalind ID: BA5B
URL: http://rosalind.info/problems/ba5b/
"""
def ManhattanTourist(n,m,Down,Right):
    s=[]
    for i in range(0,n+1):
        s.append([0]*(m+1))
    #for first row
    for i in range(1,m+1):
        s[0][i]=s[0][i-1]+Right[0][i-1]
    #for first column
    for j in range(1,n+1):
        s[j][0]=s[j-1][0]+Down[j-1][0]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j]=max(s[i][j-1]+Right[i][j-1],
                        s[i-1][j]+Down[i-1][j])
    return s[n][m]

x="""4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2"""
inlines=x.split("\n")
nm=inlines[0].split()
n=int(nm[0])
m=int(nm[1])
Down=[]
for i in range(1,n+1):
    Down.append([int(x) for x in inlines[i].split()])
Right=[]
for i in range(n+2,n+m+3):
    Right.append([int(x) for x in inlines[i].split()])
result=ManhattanTourist(n,m,Down,Right)
print(result)
