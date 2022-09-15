print('hello, capstone!')

# variables
school = 'MCTC'
gpa = 4.0

# if-statements
if gpa == 4:
    print('Wow!')
elif gpa > 3:
    print('Awesome!')
else:
    print('Cool!')

# lists  # in operator
schools = ['MCTC', 'North Hennepin', 'DCTC']
if 'MCTC' in schools: 
    print('MCTC is one of the schools in the list')

schools.sort()
print(schools)
schools.append('Century College')
print(schools)

schools.reverse() # returns None
print(schools)

# strings
class_name = 'Software Development Capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split('o'))

if 'Capstone' in class_name:
    print('This must be the capstone')

#loops - for loops over range
for x in range(10): 
    print(x)

# loops - for loops over sequence
for s in schools: 
    print(s.upper())

for letter in school:
    print(letter * 10)

data = [0] * 10
print(data)

more_data = [None] * 10
print(more_data)

# while loops
# name = input('Enter your name')
# while len(name) == 0:
# # while not name:   // same thing as ! == name
#     print('Please enter at least one character ')
#     name = input('Enter your name: ')

# True and False and None
start_of_semester = True
winter = False

if winter: 
    print('brr!')
else:
    print('it is not winter')

# Dictionaries
class_codes = { 2905: 'Capstone', 2560: 'Web', 3545: 'Java'}

for code in class_codes:
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)
    print(f'The class code is {code} and the name is {name}')


# Slicing strings, lists
schools = ['MCTC', 'North Hennepin', 'DCTC']
first_two = schools[0:2]  # first number to the one before the final number
print(first_two)

last_school = schools[-1]
print(last_school)
last_two_schools = schools[-2:]
print(last_two_schools)

school_name = 'Minneapolis Community and Technical College'
city = school_name[:11]
print(city)

# File IO
# with open('data.txt') as f:
#     print(f.read())

# with oper('schools.txt', 'w') as f:
#     f.writelines(schools)

# Functions

def get_name():
    print('Hello, please enter your name!')
    name = input('Your name is ')
    return name

name = get_name()
