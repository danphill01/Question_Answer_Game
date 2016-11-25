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
    
print("Welcome to the game. Here are the categories")
game_round = 1
categories = [['cat1','cat2','cat3','cat4','cat5','cat6'],['cat7','cat8','cat9','cat10','cat11','cat12']]
num_cats = len(categories[game_round-1])
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
print_hline()
    
