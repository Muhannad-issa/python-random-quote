import random

def baby():
  
  with open("quotes.txt", 'a') as f:
    #f.write("\nWork smarter not harder")
  #quotes = f.readlines()
    f = open("quotes.txt")
  quotes = f.read().splitlines()
  last = 14
  rnd = random.randint(0, last)

  print(quotes[rnd])

if __name__== "__main__":
  baby()