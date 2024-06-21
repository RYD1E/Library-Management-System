from .models import Book

class BookManager:
    def __init__(self, storage):
        """ 
        Initialize the manager with a storage instance.
        
        Args:
            storage: An instance of the storage to interact with.
        """
        self.storage = storage

    def add_book(self, title, author, isbn):
        """ 
        Add a new book to the storage if it doesn't already exist.
        
        Args:
            title: The title of the book.
            author: The author of the book.
            isbn: The ISBN of the book.
        
        Returns:
            bool: True if the book was successfully added, False if it already exists.
        """
        existing_books = self.storage.find('books', {'isbn': isbn})
        if existing_books:
            print(f"Book with ISBN {isbn} already exists.")
            return False
        
        book = Book(title, author, isbn)
        self.storage.add('books', book.to_dict())
        return True

    def update_book(self, isbn, title=None, author=None, available=None):
        """ 
        Update the details of a book in the storage.
        
        Args:
            isbn: The ISBN of the book to update.
            title: (Optional) The new title of the book.
            author: (Optional) The new author of the book.
            available: (Optional) The new availability status of the book.
        
        Returns:
            bool: True if the book was found and updated, False otherwise.
        """
        books = self.storage.list('books')
        for index, book in enumerate(books):
            if book['isbn'] == isbn:
                if title is not None:
                    book['title'] = title
                if author is not None:
                    book['author'] = author
                if available is not None:
                    book['available'] = available
                self.storage.update('books', index, book)
                return True
        return False

    def delete_book(self, isbn):
        """ 
        Delete a book from the storage.
        
        Args:
            isbn: The ISBN of the book to delete.
        
        Returns:
            bool: True if the book was found and deleted, False otherwise.
        """
        books = self.storage.list('books')
        for index, book in enumerate(books):
            if book['isbn'] == isbn:
                self.storage.delete('books', index)
                return True
        return False

    def list_books(self):
        """ 
        List all books currently stored.
        
        Returns:
            list: A list of dictionaries representing all books.
        """
        return self.storage.list('books')

    def find_books(self, criteria):
        """ 
        Find books based on given criteria.
        
        Args:
            criteria: A dictionary specifying the criteria to search for.
        
        Returns:
            list: A list of dictionaries representing books matching the criteria.
        """
        return self.storage.find('books', criteria)
