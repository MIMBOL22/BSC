import random
import hashlib



table = {
    #   
    '0':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '1':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '2':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '3':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '4':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '5':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '6':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '7':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '8':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    '9':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    'a':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    'b':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    'c':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    'd':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    'e':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''},
    'f':{'0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'','a':'','b':'','c':'','d':'','e':'','f':''}
}

seed = "mule zone tired worth peace census drastic squeeze setup trend man city "
seedArr = seed
password = b"123456789"


 
def randomSlov(slova):
	i = random.randint(0,len(slova)-1)
	return str.capitalize(slova[i])

def abort(text):
	return text.replace('.', '').split()

def get_key(arrOne, value):
    for k, v in arrOne.items():
        if v == value:
            return k

def set_table(x,y,v,a):
    a[y][x] = v
    return a

def get_table(x,y,a):
    return a[y][x]
 
seedArr = abort(seedArr)
 


with open("words.txt") as file:		         # StackOverFlow - если 2 дебила это сила, то миллион дебилов, это ...
    wordsArr = [row.strip() for row in file] # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

if len(password) < 8:
   while True:
       input("Пароль меньше чем 8 символов, для выхода нажмите  Ctr + C") 

passHash = hashlib.md5(password).hexdigest()
passHashArr = [passHash[i:i+2] for i in range(0, len(passHash), 2)]
for y in range(0,12):
    table = set_table(passHashArr[y][0],passHashArr[y][1],seedArr[y].capitalize(),table)
fut = 1
houh = {}
for y in wordsArr:
    houh[fut] = y
    fut +=1
for h in table:
    for g in table[h]:
        if table[h][g] == '':
            table[h][g] = randomSlov(wordsArr)
disign = "|"
arrOne = {'   ':0,'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
for a in table:
    for b in table:
        if(len(table[b][a])+1 > arrOne[b]):
            arrOne[b] = len(table[b][a])+1
for t in arrOne:
    disign += t.capitalize()+" "*arrOne[t]+"| "
disign += "\n"
for a in table:
    disign += "+---+"
    for b in table[a]:
        disign += "-"*(arrOne[b]+2)+"+"
    disign += "\n| "+a+" | "
    for b in table[a]:
        disign += table[a][b]+" "*(arrOne[b]-len(table[a][b])+1)+"| "
    disign += "\n"
print(disign,"\n |--------------------------------------------------------------------------------------------|\n |    Pin:",str(password),"\n |--------------------------------------------------------------------------------------------|\n |    Seed:",seed,"\n |--------------------------------------------------------------------------------------------|\n |    Hash:",passHash ,"\n |--------------------------------------------------------------------------------------------|")
