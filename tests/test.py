import unittest
import os
import sys
from library_management_system import BookManager, UserManager, CheckoutManager, Storage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

file_path = 'data/test_library.json'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")

class TestBookManager(unittest.TestCase):
    """
    Unit tests for BookManager class.
    """
    
    def setUp(self):
        """
        Set up the test environment.
        """
        self.storage = Storage('data/test_library.json')
        self.book_manager = BookManager(self.storage)
        
        # Add initial test data
        self.book_manager.add_book("Test Book", "Test Author", "1234567890")

    def test_add_book(self):
        """
        Test case for adding a book.
        """
        self.assertTrue(self.book_manager.add_book("New Book", "New Author", "0987654321"))
        self.assertFalse(self.book_manager.add_book("Duplicate Book", "Duplicate Author", "1234567890"))

    def test_delete_book(self):
        """
        Test case for deleting a book.
        """
        self.assertTrue(self.book_manager.delete_book("1234567890"))
        self.assertTrue(self.book_manager.delete_book("0987654321"))
        self.assertFalse(self.book_manager.delete_book("0987655321"))

    def test_search_books(self):
        """
        Test case for searching books.
        """
        books = self.book_manager.find_books({'title': 'Test Book'})
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['isbn'], '1234567890')

        books = self.book_manager.find_books({'author': 'Test Author'})
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['isbn'], '1234567890')

        books = self.book_manager.find_books({'isbn': '1234567890'})
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], 'Test Book')

        books = self.book_manager.find_books({'isbn': '0987654321'})
        self.assertEqual(len(books), 0)

class TestUserManager(unittest.TestCase):
    """
    Unit tests for UserManager class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.storage = Storage('data/test_library.json')
        self.user_manager = UserManager(self.storage)
        
        # Add initial test data
        self.user_manager.add_user("Test User", "testuser123")

    def test_update_user(self):
        """
        Test case for updating a user.
        """
        self.assertTrue(self.user_manager.update_user("testuser123", "Updated Test User"))
        self.assertFalse(self.user_manager.update_user("nonexistentuser", "Updated Test User"))

class TestCheckoutManager(unittest.TestCase):
    """
    Unit tests for CheckoutManager class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.storage = Storage('data/test_library.json')
        self.checkout_manager = CheckoutManager(self.storage)
        
        # Add initial test data
        self.checkout_manager.checkout_book("testuser123", "1234567890")

    def test_checkout_book(self):
        """
        Test case for checking out a book.
        """
        self.assertFalse(self.checkout_manager.checkout_book("testuser123", "1234567890"))
        self.assertFalse(self.checkout_manager.checkout_book("testuser123", "0987654321"))
        self.assertFalse(self.checkout_manager.checkout_book("nonexistentuser", "1234567890"))

    def test_list_checkouts(self):
        """
        Test case for listing checkouts.
        """
        checkouts = self.checkout_manager.list_checkouts()
        self.assertEqual(len(checkouts), 1)
        self.assertEqual(checkouts[0]['isbn'], '1234567890')

if __name__ == '__main__':
    unittest.main()
