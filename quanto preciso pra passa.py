import sqlite3
def frange(start, stop=None, step=None):
    #Use float number in range() function
    # if stop and step argument is null set start=0.0 and step = 1.0
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ("%g" % start) # return float number
        start = start + step

conn=sqlite3.connect(":memory:")
cursor=conn.cursor()

cursor.execute("CREATE TABLE ac (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nota REAL NOT NULL);")
for i in range (0,10):
    nota=input("Digite a "+str(i+1)+'º nota AC: ')
    cursor.execute("INSERT INTO ac(id,nota) VALUES(null,"+nota+")")

cursor.execute('SELECT nota FROM ac ORDER BY nota DESC LIMIT 7')
actemp=0
for linha in cursor.fetchall():
    actemp=linha[0]+actemp
ac=(actemp/7)*0.6

if (ac>=6):
    print('Você já passou ! Pode zerar a prova que ta suave kkkkk')
elif(ac<2):
    print('Mesmo que você gabarite sua nota a chance de passar é nula :( Sua nota ficaria= '+str(ac+4))
else :
    
    for x in frange(0.0,10.0,0.1):
        if((float(x)*0.4)+float(ac) >=6):
            print ("Você precisa tirar: "+x+" na prova para passar com a nota mínima.")
            break
            
