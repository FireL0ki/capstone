name = input('What is your name? ')
print('Hello, ' + name + '.')

name_length = len(name)
print(name + ' has ' + str(name_length) + ' letters in it.')

birth_month = input('What is your birth month? ')

if birth_month.upper() == 'SEPTEMBER':
    print(f'Happy birthday, {name}!')