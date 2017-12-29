# Imports.
import sys
import time
from termcolor import colored, cprint


# Version tracking.
def version_tracking(v_number):
   cprint("Hi there! Your copy of ADMS is currently on %s"%(v_number), 'magenta')
version_tracking("v1.0")


# A short introduction to the script.
cprint("Welcome to Alex's Dictionary Management System!", 'blue')
cprint("-----------------------------------------------", 'blue')
cprint("FAQ:", 'blue')
cprint("----", 'blue')
cprint("What can this script do?", 'blue')
print("ADMS lets the user manipulate objects from the script's dictionary.")
cprint("What can't this script do?", 'blue')
print("As of v1.0, the script does not allow users to create their own dictionaries.")
cprint("What's the point of this script?!", 'blue')
print("Over the holidays, I wanted to prove to my colleague that Python was a viable language to teach. \n")


# Creating and printing the user's original dictionary.
usr_dict_name = input('Please name your new dictionary: ')

usr_dict = {
    'Alex' : 1,
    'Jose' : 2,
    'Eric' : 3
}

intro_msg = colored('currently looks like this: \n', 'yellow')
print(usr_dict_name, intro_msg)

for x in usr_dict:
    print (x)
print('\n') 


# Defining and asking for user input.
del_usr_input = input('Please delete a user from {name}: '.format(name = usr_dict_name))
add_usr_input = input('Please add a user to {name}: '.format(name = usr_dict_name))


# True or false messages that inform the user of changes they've made to their dictionary.
del_usr_pos_msg = colored("has been deleted from {name}".format(name = usr_dict_name), 'green', attrs=['bold'])
del_usr_neg_msg = colored("hasn't been deleted from {name}".format(name = usr_dict_name), 'red', attrs=['bold'])
add_usr_pos_msg = colored("has been added to {name}".format(name = usr_dict_name), 'green', attrs=['bold'])
add_usr_neg_msg = colored("hasn't been added to {name}".format(name = usr_dict_name), 'red', attrs=['bold'])


# Adding/removing objects from the user's dictionary.
# Deleting del_usr_input from the dictionary.
if del_usr_input in usr_dict.keys():
    usr_dict.pop(del_usr_input)
else:
    print(del_usr_input, del_usr_neg_msg)

# Adding 'add_usr_input' to the dictionary.
usr_dict[add_usr_input] = 4


# Checks to see if the objects have been added or deleted.
if del_usr_input not in usr_dict:
    print(del_usr_input, del_usr_pos_msg)
else:
    print(del_usr_input, del_usr_neg_msg)

if add_usr_input in usr_dict:
    print(add_usr_input, add_usr_pos_msg, '\n')
else:
    print(add_usr_input, add_usr_neg_msg, '\n')


# Prints the user's changed dictionary.
outro_msg = colored('was updated successfully: \n', 'yellow', attrs=['bold'])
print(usr_dict_name, outro_msg)
for x in usr_dict:
    print (x)
print('\n')

