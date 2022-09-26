numbers = ['one', 'two', 'three']

try:
    # with is a context manager, separate from try/except, but often used together
    with open('numbers.txt', 'w') as number_file: # w for write -- will overwrite when run again. Use 'a' for append, to add to file.
        for n in numbers:
            number_file.writelines(numbers)
except OSError:
    print('Error writing to file.')