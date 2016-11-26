# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:55:53 2016

@author: Daniel

#Question/Answer game that can use a CSV ("Q","A") file to play the game
#1 to N teams
Keep score through 3 rounds - bonus round?
points per question change each round

"""

#read the csv to get the categories
def print_hline(char='-',width=42):
    print(char*width)
    
print("Welcome to the game.")
players = []
num_players = input("\nHow many players? ")
for i in range(1,int(num_players)+1):
    players.append(input("Player {} name? ".format(i)))
game_round = 1
categories = [['cat1','cat2','cat3','cat4','cat5','cat6'],['cat7','cat8','cat9','cat10','cat11','cat12']]
num_cats = len(categories[game_round-1])
questions = [
             {100:"Question1",200:"Question2",300:"Question3",400:"Question4"},
             {100:"Question5",200:"Question6"}
            ],[
             {200:"Question1b",400:"Question2b",800:"Question3b",1600:"Question4b"},
             {200:"Question5b",400:"Question6b"}
            ]
answers = [
             {100:"Answer1",200:"Answer2",300:"Answer3",400:"Answer4"},
             {100:"Answer5",200:"Answer6"}
            ],[
             {200:"Answer1b",400:"Answer2b",800:"Answer3b",1600:"Answer4b"},
             {200:"Answer5b",400:"Answer6b"}
            ]
print("Here are the categories:")
for i,cat in enumerate(categories[game_round-1]):
    if i+1==len(categories[game_round-1]):
        print(" {}".format(cat))
    else: print(" {} |".format(cat),end="")
print_hline('=')
for i in range(1,5+1):
    value = i*100*game_round
    if value > 999:
        for j in range(1,6+1):
            if j==num_cats:
                print(" {} ".format(i*100*game_round))
            else: print(" {} |".format(i*100*game_round),end="")
    else:
        for j in range(1,6+1):
            if j==num_cats:
                print("  {} ".format(i*100*game_round))
            else: print("  {} |".format(i*100*game_round),end="")
    if i<5: print_hline()
print_hline('=')
category = int(input("Select a category (1-{}) ".format(num_cats)))
point_value = int(input("Select a point value (in hundreds) "))*100
print("The question is:\n  {}".format(questions[game_round-1][category-1][point_value]))
print("The answer is:\n  {}".format(answers[game_round-1][category-1][point_value]))