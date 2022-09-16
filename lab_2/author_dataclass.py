from dataclasses import dataclass

@dataclass
class Author:
    name: str
    books: list

def main():

    jordan = Author('Robert Jordan', 'The Eye of the World')
    print(jordan)

main()
