h= float(input ('Digite a quantidade de cachorros quentes consumidos: '))
p=float(input ('Digite a quantidade de participantes: '))

if (1<=h and p<=1000):
    media=h/p
    media=round(media,2)
    print ('Média: '+str(media))
else:
    print('Seus dados nao batem com o solicitado, programa sera encerrado')
