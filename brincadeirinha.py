def somar(x,y):
    print (int(x)+int(y))
def subtrair(x,y):
    print(int(x)-int(y))
def multiplicar (x,y):
    print(int(x)*int(y))
def dividir(x,y):
    print(int(x)/int(y))

print ('Bem vinda a calculadora \n')
i=0
while (i==0):
    x1=input('Digite o primeiro numero: ')
    x2=input('Digite o segundo número: ')
    tipo=input('Que tipo de você quer? 1=soma,2=sub,3=mult,4=div: ')
    if (tipo=='1'):
        somar(x1,x2)
    if (tipo=='2'):
        subtrair(x1,x2)
    if (tipo=='3'):
        multiplicar(x1,x2)
    if (tipo=='4'):
        dividir(x1,x2)
    i=int(input('Deseja continuar? 0=sim,1=não: '))
   
     
