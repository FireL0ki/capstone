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