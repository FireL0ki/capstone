
class Author:
    def __init__(self, name):
        self.name = name
        self.book_list = []

    def __str__(self):
        if self.book_list:
            full_book_list = ', '.join(self.book_list)
        else:
            full_book_list = 'No published works.'
        return f'Author: {self.name} Books Published: {full_book_list}'

        # shorter way to write:
        # full_book_list = ', '.join(self.book_list) or 'No published books'
        # return f'{self.name}. Books: {full_book_list}'
        
    # method to add book titles to the book_list
    def publish(self, book_title):
        if book_title in self.book_list:
            print(f'The book {book_title} already exists in the book list.')
            return
        else:
            self.book_list.append(book_title)

def main():
    jordan = Author('Robert Jordan')
    jordan.publish('The Eye of the World')
    jordan.publish('The Great Hunt')
    jordan.publish('The Great Hunt')

    print(jordan)

    oberon = Author('Sifryn Oberon')
    print(oberon)

main()
