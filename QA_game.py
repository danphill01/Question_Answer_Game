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

def populate_questions_and_answers(game_round):
    for i,category in enumerate(categories[game_round]):
        for point_value in range(100*(game_round+1),500*(game_round+1)+1,100*(game_round+1)):
            questions[game_round][i][point_value]=category+" "+str(point_value)+" question"
            answers[game_round][i][point_value]=category+" "+str(point_value)+" answer"

def show_board(game_round):
    for i,cat in enumerate(categories[game_round]):
        if i+1==len(categories[game_round]):
            print(" {}".format(cat))
        else: print(" {} |".format(cat),end="")
    print_hline('=')
    #for each row on the board
    for i in range(1,5+1):
        #value of row
        value = i*100*(game_round+1)
        #set the indent spacing based on the size of the point value string
        if value > 999:
            spacing = " " 
        else: spacing = "  "
        #print only the active questions in each row 
        for j in range(num_cats):
            #check if the question has already been asked
#            print(value,questions[game_round][j][value])
            if value in questions[game_round][j]:
                #question exists, check if last column
                if j==num_cats-1:
                    print(spacing+"{} ".format(i*100*(game_round+1)))
                #not last row
                else: print(spacing+"{} ".format(i*100*(game_round+1)),end="|")
            #question has been seen, print space
            else: 
                #check if last column
                if j==num_cats-1:
                    print(" "*6)
                #not last row
                else: print(" "*6,end="|")
        if i<5: print_hline()
    print_hline('=')

def board_not_empty(game_round):
    return True
    
print("Welcome to the game.")
players = []
num_players = input("\nHow many players? ")
for i in range(1,int(num_players)+1):
    players.append(input("Player {} name? ".format(i)))
categories = [['cat1','cat2','cat3','cat4','cat5','cat6'],['cat7','cat8','cat9','cat10','cat11','cat12']]
questions = [
             {},{},{},{},{},{}
            ],[
             {},{},{},{},{},{}
            ]
answers = [
             {},{},{},{},{},{}
            ],[
             {},{},{},{},{},{}
            ]
for game_round in range(2):
    num_cats = len(categories[game_round])

    populate_questions_and_answers(game_round)
    print("Here are the categories for round {}:".format(game_round+1))
    while board_not_empty(game_round):
        show_board(game_round)
        category = int(input("Select a category (1-{}) ".format(num_cats)))
        point_value = int(input("Select a point value (in hundreds) "))*100
        print("The question is:\n  {}".format(questions[game_round][category-1][point_value]))
        input("Press enter to see the answer")
        print("The answer is:\n  {}".format(answers[game_round][category-1][point_value]))
        input("Press enter to continue")
        print("deleting {}".format(questions[game_round][category-1][point_value]))
        del questions[game_round][category-1][point_value]
#        print("deleted {}".format(questions[game_round][category-1][point_value]))
        del answers[game_round][category-1][point_value]
#        break

