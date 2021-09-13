"""
A solution to a ROSALIND bioinformatics problem.
Problem Title: Generate the Convolution of a Spectrum
Rosalind ID: BA4H
URL: http://rosalind.info/problems/ba4h/
"""
def SpectralConvolution(arr):
    l=[]
    for a in arr:
        for b in arr:
            if a-b>0:
                l.append(a-b)
    D=dict()
    for element in l:
        try:
            D[element]+=1
        except KeyError:
            D[element]=1
    result=[]
    while D!={}:
        maxv=max(D.values())
        for key in D.keys():
            if D[key]==maxv:
                for i in range(0,maxv):
                    result.append(key)
                D.pop(key)
                break
    return result
        
x="0 137 186 323"
inlines=x.split()
x_list=list()
for i in range(len(inlines)):
    x_list.append(int(inlines[i]))
result = SpectralConvolution(x_list)
print(result)

y="""465 473 998 257 0 385 664 707 147 929 87 450 748 938 998 768 234 722 851 113 700 957 265 284 250 137 317 801 128 820 321 612 956 434 534 621 651 129 421 337 216 699 347 101 464 601 87 563 738 635 386 972 620 851 948 200 156 571 551 522 828 984 514 378 363 484 855 869 835 234 1085 764 230 885"""
inlines_y=y.split()
y_list=list()
for i in range(len(inlines_y)):
    y_list.append(int(inlines_y[i]))
result_y = SpectralConvolution(y_list)
print(result_y)
