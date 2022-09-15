#useful for returning multiple values from a function
def get_random_cat_and_pattern():
    return 'tiger', 'stripes' # return a tuple

# Unpack your tuple to conveniently get both values in separate variable
cat, pattern = get_random_cat_and_pattern() # cat = 'tiger', pattern = 'stripe'

# if you prefer you can do this but it's usually more work
data = get_random_cat_and_pattern()

try: 
    print(data[10]) # tiger
except:
    print('oops, that does not exist.')
