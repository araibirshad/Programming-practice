import sys
import os

#a pretty ingenious solution to a perplexing problem statement
#makes use of the properties of the list data structure in python
#check the output in PYthon Tutor to get a sense of the working of the program


if __name__ == '__main__':
    n = int(input())


if n == 0:
   print('0')
else:
   
   b = (bin(n).replace('0b','')).split('0')
   h =[]

   for s in b:
      if s=='':
          continue
      else:
          h.append(int(s))
   m = str(max(h))
   print(len(m))

