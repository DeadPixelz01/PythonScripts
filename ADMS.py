#!/usr/bin/env python3
# Imports.
import time
from termcolor import colored, cprint
import json


# Version tracking.
def version_tracking(v_number):
    cprint("Hi there! Your copy of ADMS is currently on %s" % v_number, 'magenta')


version_tracking("v2.0")

# A short introduction to the script.
cprint("Welcome to Alex's Dictionary Management System!", 'blue')
cprint("-----------------------------------------------", 'blue')
cprint('Description:', 'blue')
cprint('------------', 'blue')
cprint('Allows users to create, save, load and manage Python based dictionaries. \n', 'magenta')

# True or false messages that inform the user of changes they've made to their dictionary.
msgs = {
    'del_usr_pos_msg': 'has been deleted from {name}',
    'del_usr_neg_msg': 'has not been deleted from {name}',
    'add_usr_pos_msg': 'has been added to {name}',
    'add_usr_neg_msg': 'has not been added to {name}'
}

# User keys.
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
        cprint("s    saves the dictionary that's currently open.", 'blue')
        cprint("l    loads an old dictionary", 'blue')
        cprint("n    creates a new dictionary.", 'blue')
        cprint("m    prints this man page.", 'blue')
        print("\n")

    # Creating a new dictionary.
    elif usr_choice == 'n':
        # Asking the user to name the dictionary.
        usr_dict_name = input('Please name your new dictionary: ')

        # A blank dictionary.
        usr_dict = {
        }

        # Informs the user that a new dictionary was created.
        intro_msg = colored('currently looks like this: \n', 'yellow')
        print(usr_dict_name, intro_msg)

        # Prints the new dictionary.
        for x in usr_dict:
            print(x)
        print('\n')

# Deleting a user.
    elif usr_choice == "1":
        del_usr_input = input('Please delete a user from {name}: '.format(name=usr_dict_name))
        if del_usr_input in usr_dict.keys():
            usr_dict.pop(del_usr_input)
        else:
            print(msgs['del_usr_neg_msg'].format(name=usr_dict_name))
    
        if del_usr_input not in usr_dict:
            print(del_usr_input, msgs['del_usr_pos_msg'].format('green', name=usr_dict_name), '\n')
        else:
            print(del_usr_input, msgs['del_usr_neg_msg'].format('red', name=usr_dict_name), '\n')

# Adding a user.
    elif usr_choice == "2":    
        add_usr_input = input('Please add a user to {name}: '.format(name=usr_dict_name))
        usr_dict[add_usr_input] = count + 1
        if add_usr_input in usr_dict:
            print(add_usr_input, msgs['add_usr_pos_msg'].format('green', name=usr_dict_name), '\n')
        else:
            print(add_usr_input, msgs['add_usr_neg_msg'].format('red', name=usr_dict_name), '\n')

# Prints the user's changed dictionary.
    elif usr_choice == "3":
        update_msg = colored('was updated successfully: \n', 'yellow')
        print(usr_dict_name, update_msg)

        for x in usr_dict:
            print(x)
        print('\n')

# Saving dictionaries.
    elif usr_choice == 's':
        save_file = input('Please name the file: ')
        with open('{filename_save}.json'.format(filename_save=save_file), 'w') as fp:
            json.dump(usr_dict, fp)
        saved_msg = colored('was saved successfully! \n', 'magenta')
        print(usr_dict_name, saved_msg)

# Loading dictionaries.
    elif usr_choice == 'l':
        usr_dict_name = 'Your dictionary'
        load_file = input('Please enter the name of the file you wish to load: ')
        with open('{filename_load}.json'.format(filename_load=load_file), 'r') as fp:
            usr_dict = json.load(fp)
        loaded_msg = colored('was loaded successfully! \n', 'magenta')
        print(usr_dict_name, loaded_msg)

# Existing the script.
    elif usr_choice == "4":
        cprint("Exiting...", 'blue')
        cprint("Thank you for using ADMS. If you enjoyed the script, support software like it =)", 'blue')
        cprint(" -Alex Smith", 'blue')
        time.sleep(1)
        quit()

# Invalid input for user error.
    else:
        usr_error = colored("Invalid input! '{choice}' is not a valid operation. See man page for help."
                            .format(choice=usr_choice), 'red', attrs=['bold'])
        print(usr_error)
