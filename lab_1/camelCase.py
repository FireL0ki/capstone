""" camelCase converter program! """

def banner():
    """ Display program name using stars """ # triple quotes are doc strings
    message = 'Awesome camelCase Program!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars}\n')

def instructions():
    """ Display instructions for how to use the program """
    print('Enter a sentence and this program will convert it to camelCase.')

def main():
    banner()
    instructions()

main()

user_input = str(input('Enter a sentence to convert to camelCase '))

# defines a function that converts the sentence to title case, and gets rid of spaces
def camel_case(x):
    # .title() converts the phrase to title case (first letter capitalized of each word), then .replace() replaces all " " spaces with no space 
    x = x.title().replace(" ", "")
    # Then x[0] grabs the first (0th) letter and makes it lowercase, and then we need to grab the rest of the word [1:] (from the second spot onward) and concatonate it to the first letter
    x = x[0].lower() + x[1:]
    return x

print(camel_case(user_input))