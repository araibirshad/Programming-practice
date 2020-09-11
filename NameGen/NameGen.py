# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:37:47 2020

@author: araibirshad
"""
#Name-Generator
#v1.0
#Only American Names. Can add nationality selection in the future.
#Option to select male/female.
#Option to select number of names to be displayed.

import time
import random

f
#>>>>>>>>>>>>>>Function Definitions<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
def load_fem():
    l_file = open('C:/Users/pc/Documents/Python Scripts/Name Gen/fem_name.txt','r')
    ln = l_file.read()
    
    l_file.close()
    return ln.split()
    
    
    
def load_male():
        l2_file = open('C:/Users/pc/Documents/Python Scripts/Name Gen/male_name.txt','r')
        ln2 = l2_file.read()
        
        #l2_file.close()
        return ln2.split()
def load_surname():
    l3_file = open('C:/Users/pc/Documents/Python Scripts/Name Gen/surnames.txt','r')
    ln3 = l3_file.read() 
    
    l3_file.close()
    return ln3.split()
    
def run_prog():
    a = load_male()
    b = load_fem()
    c = load_surname()
    print('Welcome to Name Generator v1.0.')
    
    while True:
       sex = str(input('Please enter the gender of the name you require. M/F')) 
       if sex.upper() not in ('M','F'):
           print('Invalid input. Please try again')
       else:
           break
    
    while True:
      try:
          num = int(input('Please enter the number of names you want generated.'))
          print('Fetching names.....')
          break
      except ValueError:
          print('Please enter a valid number')
    
    ls_names = []
    for i in range(num):
        if sex == 'M':
        
          ls_names.append(str(a[random.randrange(0,len(a))]+' '+
                               c[random.randint(0,len(c))]))
            
                              
        else:
            
          ls_names.append(str(b[random.randrange(0,len(b))]+' '+
                              c[random.randrange(0,len(c))]))
    for i in ls_names:
          print(i)
 
run_prog()

            
    


