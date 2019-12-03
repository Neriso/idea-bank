import sys
import os
menu = ["1. show list", "2. add to", "3. delete", "q. quit"]

options = True
while options == True:
    print()
    for line in menu:
        print(line)
    print()
    user_option = input("what would you do? ")
    print()

    if user_option == "2":
        with open("ideatxt.txt","a") as ideabank:
            idea = input("what is your new idea?")
            ideabank.write(idea + "\n") 
            ideabank.close()

    elif user_option == "1":
        with open("ideatxt.txt","r") as ideabank:
            for i, line in enumerate(ideabank):
                print('{}.{}'.format(i+1, line.strip()))
                #print (ideabank.read())

    elif user_option == "q":
        pass
    
    elif user_option == "3":
        (remove_idea) = input("with idea would you like to delate? ")
        with open("ideatxt.txt") as ideabank:
            for line in enumerate(ideabank):
               line.remove(remove_idea)
                
                

        ideabank.close()
