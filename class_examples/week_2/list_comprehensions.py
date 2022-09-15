# The classes a student is registered for 
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only the ITEC classes
only_itec = [ c for c in classes_registered if c.startswith('ITEC') ] # c.lower()
print(only_itec)

# Record temperature every day. Record -1 if not possible to take measurement.
high_temps = [-1, 78, 72, 67, -1, 51, 87, -1, 54, 67, 78, -1, 70]

# Make a list of only numbers that represent a valid temperature measurement
only_real_measurements = [ temp for temp in high_temps if temp != -1 ]
print(only_real_measurements)

temp_celsius = [ (temp_f - 32) * 5 / 9 for temp_f in only_real_measurements]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)
print(f'The average i9s {average:.2f}')  # .2f -- decimal place formatting

# numbers -- start with list [2, 4, 6], write a comprehension to make a new list with each number increased by one
even_numbers = [2, 4, 6]
print(even_numbers)

increased_numbers = [ number + 1 for number in even_numbers]
print(increased_numbers)

# create new list with non-zero numbers
number_list = [0, 3, 4, 0, 22, 1]
print(number_list)

non_zero_numbers = [ number for number in number_list if number != 0]
print(non_zero_numbers)

# create new list with non-itec classes
classes_list = [ 'ITEC 2560', 'BTEC 1010', 'ITEC 2905']
print(classes_list)

non_itec_classes = [ c for c in classes_list if not c.startswith('ITEC') ]
print(non_itec_classes)

# create new list where numbers are doubled, only if not zero
all_numbers_list = [0, 10, 4, 0, 32]
print(all_numbers_list)

doubled_numbers = [ number * 2 for number in all_numbers_list if number != 0]
print(doubled_numbers)