#sets
# sets are not ordered
# sets prevent duplicates

cats = set() # creates empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)

birds = { 'owl', 'robin', 'swan'}
print(birds)
birds.add('robin')
print(birds)
birds.add('cardinal')
print(birds)

bird_lsit = ['robin', 'swan', 'swan', 'eagle', 'cardinal', 'swan', 'robin']
bird_list_no_duplicates = lsit(set(bird_list))
print(bird_list_no_duplicates)
