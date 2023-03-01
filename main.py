# This file is a interface to the automata.py file, which is the main file of the project. The automata.py file is responsible for reading the file and creating the automata, and the main.py file is responsible for reading the input and calling the automata to check if the word is accepted or not.

import os
import automata as auto

# function to represent the menu
def menu():
    print('Choose an option below:')
    print('-----------------')
    print(' 1 - Read automata from file')
    print(' 2 - Exit')
    print('-----------------')

# function to read the automata from a file
def readFromFile():
    # read the file name
    print('\nEnter the file name (with extension):')
    print('The file need to be in the inputs folder(/inputs/file_name.txt)')
    # list files in the inputs folder
    print('Files in the inputs folder:\n')
    for file in os.listdir('inputs'):
        print('\t'+file)

    file_name = input('\nFile name: ')
    file = 'inputs/'+file_name
    # check if the file exists
    if os.path.exists(file):
        # create the automata
        automata = auto.Automata(file)
        # read the file of strings
        print('\nChoose the file of strings to validate (with extension):')
        print('The file need to be in the strings folder(/strings/file_name.txt)')
        # list files in the strings folder
        print('Files in the strings folder:\n')
        for file in os.listdir('strings'):
            print('\t'+file)
        # list files in the strings folder
        string = input('\nFile name: ')
        strings_file = 'strings/'+string
        # check if the file exists
        if os.path.exists(strings_file):
        # open the file
            with open(strings_file, 'r') as f:
                # read the strings
                strings = f.read().splitlines()
                #  by element execute the automata
                print('Validating strings...')
                for string in strings:
                    # check if the word is accepted
                    if automata.run(string):
                        print('* Accepted: ' + string)
                        # write the word and result in the output file
                        with open('outputs/output_'+file_name, 'a') as f:
                            f.write(string + ' -> Accepted by automata ' + file_name + ' \n')
                            f.close()
                    else:
                        print('~ Not accepted: ' + string)
                        with open('outputs/output_'+file_name, 'a') as f:
                            f.write(string + ' -> Not accepted by automata ' + file_name + ' \n')
                            f.close()
                f.close()
        else:
            print('File not found')
    else:
        print('File not found')
    print('\n-----------------')

def main():
    print('Welcome to the automata validator')
    # variable to control the menu
    option = 0
    while option != 2:
        menu()
        option = int(input('Option: '))
        match option:
            case 1:
                readFromFile()
            case 2:
                print('-----------------')
                print('\nBye, see you soon!')
            case _:
                return menu()

if __name__ == '__main__':
    main()