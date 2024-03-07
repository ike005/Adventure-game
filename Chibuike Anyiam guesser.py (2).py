# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:40:20 2024

@author: chibuike
"""

import random 
random.randint(1,100)
i=0
keepgoing = True
while (keepgoing):
    i += 1
    if i >= 7:
        Print=("Too many guesses")
        keepgoing = False
        
    UserGuess = input("Guess a number within (1-100): ")
    
    if UserGuess.isdigit():
        UserGuess = int(UserGuess)
        j = random.randint(1,100)
        
        if UserGuess < j :
            print("Too low")
                
        if UserGuess > j:
            print("Too high")
                    
        if UserGuess == j :
            print("correct")
            
    else:
        print("not a number")
            
            
    
                        

Keepgoing = False
                        
                    
                