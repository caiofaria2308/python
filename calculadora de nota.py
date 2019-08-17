import sqlite3

conn=sqlite3.connect(':memory:')
cursor=conn.cursor()

cursor.execute("CREATE TABLE ac(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nota REAL not null);")
cursor.execute("CREATE TABLE prova(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nota REAL NOT NULL);")
i=0
for i in range(10):
    nota=input('Digite a '+str(i+1)+'º nota AC: ')
    cursor.execute("INSERT INTO ac(id,nota) VALUES(null,"+nota+")")

prova=input("Digite a nota da prova: ")
cursor.execute('INSERT INTO prova VALUES(null,'+prova+')')

cursor.execute('SELECT nota FROM ac ORDER BY nota DESC LIMIT 7')
actemp=0
for linha in cursor.fetchall():
    actemp=linha[0]+actemp
ac=(actemp/7)*0.6


cursor.execute('select nota from prova')
prova=0
for li in cursor.fetchall():
    prova=li[0]+prova

notafinal=(prova*0.4)+ac
print ('Sua nota final é: '+str(notafinal))

if (notafinal<6):
    substitutiva=input("Digite o valor da nota substitutiva: ")
    if (float(substitutiva)<notafinal):
        substitutiva=notafinal
    substitutiva=float(substitutiva)*0.4
    final=notafinal+float(substitutiva)
    print ('Sua média com a nota substitutiva: '+str(final))
    if (final<6):
        print('Você foi reprovado')
    else:
        print('Você foi aprovado ! Parabéns! ')
else:
    print('Você foi aprovado ! Parabéns! ')

conn.close()
