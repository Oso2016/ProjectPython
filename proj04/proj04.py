# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

random_string = raw_input("Please enter a random word: ")
paliList = []
paliCheck = []
original = []
first_letter = random_string[0]
rest = random_string[1:]
rest = rest.lower()
first2 = first_letter.upper()
random_string2 = first2 + rest
random_string = random_string.replace(" ","")
random_string = random_string.lower()
for symbol in random_string:
    original.append(symbol)
for letter in random_string:
    paliList.append(letter)
for item in paliList:
    paliCheck.append(paliList[-1])
    paliList = paliList[0:-1]
print paliCheck
if original == paliCheck:
    print random_string2 + " is a palindrome."
else:
    print random_string2 + " is not a palindrome."
