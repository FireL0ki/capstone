# program to convert a sentence into camel case

user_input = str(input('Enter a sentence to convert to camelCase '))

# defines a function that converts the sentence to title case, and gets rid of spaces
def camel_case(x):
    # .title() converts the phrase to title case (first letter capitalized of each word), then .replace() replaces all " " spaces with no space 
    x = x.title().replace(" ", "")
    # Then x[0] grabs the first (0th) letter and makes it lowercase, and then we need to grab the rest of the word [1:] (from the second spot onward) and concatonate it to the first letter
    x = x[0].lower() + x[1:]
    return x

print(camel_case(user_input))