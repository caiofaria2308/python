#importando o banco SQLite 3
import sqlite3
import time

#Armazenando o banco na Memória
conn=sqlite3.connect(':memory:')
#criando aquele que manipula o banco
cursor=conn.cursor()

#Cria tabela que armazena as notas da AC
cursor.execute("CREATE TABLE ac(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nota REAL not null);")
#Cria tabela que armazena a nota da prova
cursor.execute("CREATE TABLE prova(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nota REAL NOT NULL);")
#Criação da variavel para o loop
i=0
#loop para cadastrar as notas das 10 AC's
for i in range(10):
    #armazenando a nota em uma variável.
    nota=input('Digite a '+str(i+1)+'º nota AC: ')
    #Inserindoa a nota no banco
    cursor.execute("INSERT INTO ac(id,nota) VALUES(null,"+nota+")")
#Cadastrando e armazenando no banco a nota da prova
prova=input("Digite a nota da prova: ")
cursor.execute('INSERT INTO prova VALUES(null,'+prova+')')

#Seleciona as 7 maiores notas das AC
cursor.execute('SELECT nota FROM ac ORDER BY nota DESC LIMIT 7')
#cria um temp que armazenará a soma das 7 maiores notas
actemp=0
for linha in cursor.fetchall():
    #Colocando e somando as notas das AC na temporaria
    actemp=linha[0]+actemp
#Calculando os 60% da média final
ac=(actemp/7)*0.6

#Selecionando e atribuindo em uma variável a nota da prova
cursor.execute('select nota from prova')

prova=0
for li in cursor.fetchall():
    prova=li[0]+prova
#Calculando os 40% da nota final
notafinal=(prova*0.4)+ac
#Mostrando a nota final
print ('Sua nota final é: '+str(notafinal))

#Se a nota for menor que 6 ele rodará o IF, se nao ele irá direto para o ELSE
if (notafinal<6):
    #Atribuição da nota substitutiva e caso ela seja maior que a da prova, ela representará os 4o%
    substitutiva=input("Digite o valor da nota substitutiva: ")
    if (float(substitutiva)<notafinal):
        substitutiva=prova
    substitutiva=float(substitutiva)*0.4
    final=ac+float(substitutiva/2)
    
    print ('Sua média com a nota substitutiva: '+str(final))
    
    if (final<6):
        print('Você foi reprovado')
    else:
        print('Você foi aprovado ! Parabéns! ')
else:
    print('Você foi aprovado ! Parabéns! ')

conn.close()
time.sleep(10)    
