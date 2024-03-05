# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:17:46 2024

@author: chibuike
"""

userName = input(" What is your name? ")

userInput = input(f"Hi {userName}, want to join me in a game?(Y/N) ")


if userInput == "Y" :
    print("okay let's begin ")
    
    question1 = input("knock knock: ")
    if question1 == "who's there":
            question2 = input("Lettuce: ")
            if question2 == "lettuce who":
                print ("lettuce in")
            else:
                print("you were meant to say 'lettuce in'")
    else:
        print("you were meant to say 'who's there' ")
            
else:
    print ("oh, i am sad")
    

    