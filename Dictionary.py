# Imports.
import sys
import time
from termcolor import colored, cprint


# Version tracking.
def version_tracking(v_number):
   cprint("Hi there! Your copy of ADMS is currently on %s"%(v_number), 'magenta')
version_tracking("v1.4")


# A short introduction to the script.
cprint("Welcome to Alex's Dictionary Management System!", 'blue')
cprint("-----------------------------------------------", 'blue')
cprint("FAQ:", 'blue')
cprint("----", 'blue')
cprint("What can this script do?", 'blue')
print("ADMS lets the user create and manipulate their very own dictionary.")
cprint("What can't this script do?", 'blue')
print("As of v1.2, user's can not save and load their custom dictionaries.")
print("I don't know, play around with it. Since it's free, you can view it's source code and edit it to your liking.")
cprint("What's the point of this script?!", 'blue')
print("Over the holidays, I wanted to prove to my colleague that Python was a viable language to teach. \n")


# Creating and printing the user's dictionary.
# Asking the user to name their dictionary.
usr_dict_name = input('Please name your new dictionary: ')

# A blank dictionary.
usr_dict = {
}

# Introduces the user to their new dictionary.
intro_msg = colored('currently looks like this: \n', 'yellow')
print(usr_dict_name, intro_msg)

# Prints the blank dictionary.
for x in usr_dict:
    print (x)
print('\n') 


# True or false messages that inform the user of changes they've made to their dictionary.
del_usr_pos_msg = colored("has been deleted from {name}".format(name = usr_dict_name), 'green', attrs=['bold'])
del_usr_neg_msg = colored("hasn't been deleted from {name}".format(name = usr_dict_name), 'red', attrs=['bold'])
add_usr_pos_msg = colored("has been added to {name}".format(name = usr_dict_name), 'green', attrs=['bold'])
add_usr_neg_msg = colored("hasn't been added to {name}".format(name = usr_dict_name), 'red', attrs=['bold'])


# Generating user ID.
count = 0


# User choice.
# This is new and I have no idea how well it'll work later on down the track...
# Asking the user for either input 1 or 2 (1 deletes a user, 2 adds a new user).
while True:
    usr_choice = input('Enter an operation (m for help): ')


# Man page.
    if usr_choice == "m":
        cprint("Man page", 'blue') 
        cprint("--------", 'blue')
        cprint("1    deletes a user from the dictionary.", 'blue')
        cprint("2    adds a user to the dictionary.", 'blue')
        cprint("3    writes changes and prints the updated dictionary.", 'blue')
        cprint("4    stops and exists the script.", 'blue')
        cprint("m    prints this man page.", 'blue')
        print("\n")


# Deleting a user.
    elif usr_choice == "1":
        del_usr_input = input('Please delete a user from {name}: '.format(name = usr_dict_name)) 
        if del_usr_input in usr_dict.keys():
            usr_dict.pop(del_usr_input)
        else:
            print(del_usr_input, del_usr_neg_msg)
    
        if del_usr_input not in usr_dict:
            print(del_usr_input, del_usr_pos_msg, '\n')
        else:
            print(del_usr_input, del_usr_neg_msg, '\n')


# Adding a user.
    elif usr_choice == "2":    
        add_usr_input = input('Please add a user to {name}: '.format(name = usr_dict_name))

        usr_dict[add_usr_input] = count + 1

        if add_usr_input in usr_dict:
            print(add_usr_input, add_usr_pos_msg, '\n')
        else:
            print(add_usr_input, add_usr_neg_msg, '\n')


# Prints the user's changed dictionary.
    elif usr_choice == "3":
        outro_msg = colored('was updated successfully: \n', 'yellow', attrs=['bold'])
        print(usr_dict_name, outro_msg)

        for x in usr_dict:
            print (x)
        print('\n')


# Existing the script.
    elif usr_choice == "4":
        cprint("Exiting...", 'blue')
        cprint("Thank you for using ADMS. If you enjoyed the script, support free software like it. Everyone will benefit from it! =)", 'blue')
        cprint("- Alex Smith", 'blue')
        time.sleep(1)
        quit()


# Invalid input for user error.
    else:
        usr_error = colored("Invalid input! '{choice}' is not a valid operation. See man page for help.".format(choice = usr_choice), 'red', attrs=['bold'])
        print(usr_error)

