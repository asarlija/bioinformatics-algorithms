"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement CycleToChromosome
Rosalind ID: BA6G
URL: http://rosalind.info/problems/ba6g/
"""
def CycleToChromosome(str_nodes):
    Nodes=[int(x) for x in str_nodes[1:-1].split(" ")]
    Chromosome=[]
    k=int(len(Nodes)/2)
    for j in range(0,k):
        if Nodes[2*j] < Nodes[2*j+1]:
            Chromosome.append(int(Nodes[2*j+1]/2))
        else:
            Chromosome.append(int(-Nodes[2*j]/2))
    return Chromosome

def f(x):
    if x<0:
        s=""
    else:
        s="+"
    return s

def printCycleToChromosome(L):
    s="(" + " ".join([f(x) + str(x) for x in L]) + ")"
    print(s)

str_nodes="(1 2 4 3 6 5 7 8)"
result=CycleToChromosome(str_nodes)
printCycleToChromosome(result)



