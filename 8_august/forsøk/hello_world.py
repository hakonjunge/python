print("hello world jeg er håkon")
#Dette er en kommentar
#Bruk slike for å notere og hjelpe å holde styr på enkle linjer
"""
bruk dette 
for å ha 
kommentarer over 
flere linjer 
"""
x = 5
y = 99
z = "hællæh"
print(x)
print(y)
print(z)

x, y, z = "Programmering 1", "Webutvikling", "Innføring i design av digitale produkter"

print(x, y, z)
print(x + " " + y + "" + z) #samme resultat som den over
print(x)
print(y)
print(z)


kodesprak = ["python", "javascript", "html", "css"]
print(kodesprak)


#(lambda HELLOWORLD: [(print(l,end="") if l in "Hello World!" else print()) for l in [l for l in "Hello World"]])("HeLlOwOrLd")


import random
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","!","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Æ","Ø","Å",",","."]
text = "Hello, World!"
while text != "":
    word = abc[random.randrange(len(abc))]
    if not word == txt[0]:
        continue
    txt = txt[1:]
    print(word, end="")

'''
import random

class Letter:
    def __init__(self,l):
        self.l = l
    def __str__(self):
        return self.l

def sysout(word):
    print(f"{word}",end="")
    return


abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","!"]
txt = "liverpool er bedre enn city"
while txt != "":
    l = Letter(abc[random.randrange(len(abc))])
    if not l.l == txt[0]:
        continue
    txt = txt[1:]
    sysout((lambda z : f"{z}" if z.l in "liverpool er bedre enn city" else "\n")(l))'''