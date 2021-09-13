"""
A solution to a Rosalind bioinformatics problem
Problem Title: Implement ChromosomeToCycle
Rosalind ID: BA6F
URL: http://rosalind.info/problems/ba6f/
"""
def ChromosomeToCycle(str_chromosome):
    chromosome=[int(x) for x in str_chromosome[1:-1].split(" ")]
    n=len(chromosome)
    node=[]
    for j in range(0,n):
        i=chromosome[j]
        if i>0:
            node.append(2*i-1)
            node.append(2*i)
        else:
            node.append(-2*i)
            node.append(-2*i-1)
    return node
    
str_chromosome="(+1 -2 -3 +4)"
result=ChromosomeToCycle(str_chromosome)
print("("+" ".join([str(x) for x in result])+")")
