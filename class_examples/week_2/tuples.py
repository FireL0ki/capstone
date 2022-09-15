# tuples are like a list, but is immutable (cannot be changed once created)
# tuple outputs have parentheses around them
print('TUPLES')
city_state = [ ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA') ]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

city, state = first_city_state
print(city)
print(state)

print('ANIMAL TUPLES')

#unpack tuple values - match the correct number of values
animals = ('lion', 'puma', 'tiger')
lion, puma, tiger = animals

print(tiger)

def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km

distances = get_distance()
print(distances)

