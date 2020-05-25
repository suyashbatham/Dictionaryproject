                      # Algorithm
                     # 1.interface
                     # 2.i need to develop the word matching
                     # 3.modify the program
                     # 4. get close matches (fruit = fruti or fruits)

                # Condition to check data format
                # 1.small case letter
                # 2.title
                # 3.Capitalize
                # 4.Upper Case

import json
from difflib import get_close_matches

data = json.load(open("origional.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on wrong keys ")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("pugger your paw steps on wrong keys")



word = input("Enter the word you want to search")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)



# word = input("Enter the word you want to search")
# output = data[word]
# print(output) # print the value of the given key




