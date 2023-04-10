import json
from difflib import get_close_matches

#Load Data File
data = json.load(open('data.json'))

def translate(key):
    #Make sure word is lowercase
    key =  key.lower()
    if key in data:
        return data[key]
    #Check if result is empty or not
    elif len(get_close_matches(key, data.keys())) > 0:
        choice = input('Did you mean %s instead? Enter Y if yes and N if no. : ' % get_close_matches(key, data.keys())[0])
        choice = choice.upper()
        if choice == "Y":
           return translate(get_close_matches(key, data.keys())[0])
        else:
            SystemExit()
    else:
        return 'The word doesn\'t exsist.Please check the word again!'

def start():
    print("\tWelcome to Cliff Dictionary\n")
    word = input('Enter the word: ')
    result = translate(word)
    #check if result is a list or not
    if type(result)==list:
        print('\t\t\tDefenitions')
        for item in result:
            print(f'\n{item}')
    else:
        print(result)


start()