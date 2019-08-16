def getFatorial(x):
    n1=[]
    n2=[]
    for i in range (int(x)):
        n1.append(int(input()))
        n2.append(int(input()))
    for u in range (int(x)):
        print (n1[int(u)]*n2[int(u)] )
fatorial=input()
getFatorial(fatorial)
