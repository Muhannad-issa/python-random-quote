import random

def baby():
  add_quotes = ["Wish for others what you wish for yourself", "Love thy neighbor"]
  #quotes = f.readlines()
  f = open("quotes.txt")
  quotes = f.read().splitlines()
  quotes.extend(add_quotes)
  f.close
  
  last = 16
  rnd = random.randint(0, last)

  print(quotes[rnd])

if __name__== "__main__":
  baby()