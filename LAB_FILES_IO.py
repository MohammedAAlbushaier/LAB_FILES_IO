'''
Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"

'''

file = open("to_do.txt", "a+", encoding="UTF-8")
while True:
    userInput = input("do you want to add a new To-Do item?(\"y\" for yes and \"n\" for no) \nNOTE: write \"exit\" to close the program ")
    if userInput=='y' or userInput=="Y":
        userInput2=input("Please write what would you like to add into the To-Do list")

        file.write(userInput2+"\n" )
    elif userInput=='n' or userInput=="N":
        userInput2 = input("do you want to list your To-Do items ?(\"y\" for yes and \"n\" for no)")
        if userInput2=='y' or userInput2=='Y':
            file.seek(0)
            print (file.read())
        elif userInput2=='n' or userInput2=='N':
            break
    elif userInput=="exit":
        break

file.close()