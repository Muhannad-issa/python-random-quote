import random

def baby():
  
  f = open("quotes.txt")
  #quotes = f.readlines()
  quotes = f.read().splitlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)

  print(quotes[rnd])

if __name__== "__main__":
  baby()