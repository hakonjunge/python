import random

def my_function():
  print("********* ")
  # Bruker randrange(1,101) fordi da inkluderes 100
  print( f"***{random.randrange(1,101)}***")
  print("********* ")
  print()
# Kjører funksjonen 3 ganger for å se om det blir forskjellige tall hver gang
my_function()
my_function()
my_function()