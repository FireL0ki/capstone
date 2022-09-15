# program to print off a list of courses based on user input

list_of_classes = []

number_courses = int(input('How many courses are you taking this semester? '))

# while the number_courses is greater than 0, keep asking for the names of courses, and append those courses. 
while number_courses > 0:
    new_class = input('Enter the name of a course you are taking: ')
    list_of_classes.append(new_class)
    # update the count by subtracting 1 on each loop, so eventually we will get to zero and stop adding courses
    number_courses = number_courses - 1

for course in list_of_classes:
    print(course)

if number_courses == 0:
    print('You are not taking any courses this semester.')


