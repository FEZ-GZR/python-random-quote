#!/usr/local/bin/python3
import random
def primary():
    #print("Keep it logically awesome.") (temporarily removed)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last) #The last signifies that the last variable hlds the highest indes for the array. Then our random numer is stored in rnd using the random.randint function, which takes the lowest-possible number (zero) and highest possible number (stored in last within the array from the quote.text file).
  last = len(quotes) - 1 #This here is stating that the last will have a number either remove or add a quote from the text file. The last variable can be changed to update automatically.
  
  print(quotes[rnd]) #The [0] means that it will print out from the array text quote file the first item.

if __name__== "__main__":
    primary()



