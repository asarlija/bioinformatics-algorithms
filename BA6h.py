"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement ColoredEdges
Rosalind ID: BA6H
URL: http://rosalind.info/problems/ba6h/
"""

def ChromosomeToCycle(Chromosome):
    Nodes=[]
    for j in range(0,len(Chromosome)):
        i=Chromosome[j]
        if i > 0:
            Nodes.append(2*i-1)
            Nodes.append(2*i)
        else:
            Nodes.append(-2*i) 
            Nodes.append(-2*i-1)
    return Nodes

def ColoredEdges(int_chromosome):
    Edges=[]
    for chromosome in int_chromosome:
        Nodes=ChromosomeToCycle(chromosome)
        for j in range(0,len(chromosome)):
            Edges.append([Nodes[2*j+1],Nodes[(2*j+2)%len(Nodes)]])
    return Edges

def printColoredEdges(L):
    s=""
    for el in L:
        s=s+ "("+ str(el[0])+","+str(el[1])+"), "
    print(s[:-1][:-1])
    
str_chromosome='(+1 -2 -3)(+4 +5 -6)'
str_chromosome=str_chromosome[1:-1].split(")(")
n=len(str_chromosome)
int_chromosome=[]
for i in range(0,n):
    int_chromosome.append([int(x) for x in str_chromosome[i].split()])
result=ColoredEdges(int_chromosome)
printColoredEdges(result)
