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
    sysout((lambda z : f"{z}" if z.l in "liverpool er bedre enn city" else "\n")(l))