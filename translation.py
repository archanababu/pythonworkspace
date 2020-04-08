#----------------------------------
# VOWEL translation function example
#----------------------------------

'''
You can type multi line comments here
For example1
example2
example3
'''

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    
    return translation

newPhrase = input("Enter a new phrase : ")

print(translate(newPhrase))