class Book:
    def __init__(self, title, author, isbn, available=True):
        """ 
        Initialize a Book object.
        
        Args:
            title: The title of the book.
            author: The author of the book.
            isbn: The ISBN of the book.
            available: (Optional) Availability status of the book (default is True).
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        """ 
        Convert Book object attributes to a dictionary.
        
        Returns:
            dict: A dictionary representation of the Book object.
        """
        return self.__dict__


class User:
    def __init__(self, name, user_id):
        """ 
        Initialize a User object.
        
        Args:
            name: The name of the user.
            user_id: The ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        """ 
        Convert User object attributes to a dictionary.
        
        Returns:
            dict: A dictionary representation of the User object.
        """
        return self.__dict__


class Checkout:
    def __init__(self, user_id, isbn):
        """ 
        Initialize a Checkout object.
        
        Args:
            user_id: The ID of the user performing the checkout.
            isbn: The ISBN of the book being checked out.
        """
        self.user_id = user_id
        self.isbn = isbn

    def to_dict(self):
        """ 
        Convert Checkout object attributes to a dictionary.
        
        Returns:
            dict: A dictionary representation of the Checkout object.
        """
        return self.__dict__
