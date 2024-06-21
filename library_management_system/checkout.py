from .models import Checkout
class CheckoutManager:
    def __init__(self, storage):
        """ 
        Initialize the manager with a storage instance.
        
        Args:
            storage: An instance of the storage to interact with.
        """
        self.storage = storage

    def checkout_book(self, user_id, isbn):
        """ 
        Checkout a book for a user if it is available.
        
        Args:
            user_id: The ID of the user checking out the book.
            isbn: The ISBN of the book to be checked out.
        
        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        books = self.storage.list('books')
        for book in books:
            if book['isbn'] == isbn and book['available']:
                book['available'] = False
                self.storage.update('books', books.index(book), book)
                checkout = Checkout(user_id, isbn)
                self.storage.add('checkouts', checkout.to_dict())
                return True
        return False  # Return False if book not found or not available

    def checkin_book(self, isbn):
        """ 
        Checkin a book if it is currently checked out.
        
        Args:
            isbn: The ISBN of the book to be checked in.
        
        Returns:
            bool: True if the book was successfully checked in, False otherwise.
        """
        books = self.storage.list('books')
        for book in books:
            if book['isbn'] == isbn and not book['available']:
                book['available'] = True
                self.storage.update('books', books.index(book), book)
                checkouts = self.storage.list('checkouts')
                for index, checkout in enumerate(checkouts):
                    if checkout['isbn'] == isbn:
                        self.storage.delete('checkouts', index)
                        return True
        return False  # Return False if book not found or already available

    def list_checkouts(self):
        return self.storage.list('checkouts')
