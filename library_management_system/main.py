
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
import re
from library_management_system import BookManager, UserManager, CheckoutManager, Storage


# Setup logging
logging.basicConfig(filename='data/library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main_menu():
    """ 
    Display the main menu options and prompt for user input.
    
    Returns:
        str: The user's choice as a string.
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. List Books")
    print("5. Search Books")
    print("6. Add User")
    print("7. Update User")
    print("8. Delete User")
    print("9. List Users")
    print("10. Search Users")
    print("11. Checkout Book")
    print("12. Checkin Book")
    print("13. List Checkouts")
    print("14. Exit")
    return input("Enter choice: ").strip()

def validate_isbn(isbn):
    # Validate ISBN format: 10 or 13 digits
    return re.match(r'^\d{10}(\d{3})?$', isbn) is not None

def validate_user_id(user_id):
    # Validate user ID format: alphanumeric, 5-10 characters
    return re.match(r'^[a-zA-Z0-9]{5,10}$', user_id) is not None

def main():
    storage = Storage('data/library.json')
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    checkout_manager = CheckoutManager(storage)

    while True:
        try:
            choice = main_menu()

            if choice == '1':
                title = input("Enter title: ").strip()
                author = input("Enter author: ").strip()
                isbn = input("Enter ISBN: ").strip()
                if not validate_isbn(isbn):
                    raise ValueError("Invalid ISBN format. Please enter a valid ISBN.")
                book_manager.add_book(title, author, isbn)
                logging.info(f"Added book: {title}, {author}, {isbn}")
                print("Book added.")

            elif choice == '2':
                isbn = input("Enter ISBN of the book to update: ").strip()
                title = input("Enter new title (leave blank to keep current): ").strip()
                author = input("Enter new author (leave blank to keep current): ").strip()
                available = input("Is the book available? (yes/no/leave blank to keep current): ").strip().lower()
                if available not in {'yes', 'no', ''}:
                    raise ValueError("Invalid input for availability. Please enter 'yes', 'no', or leave blank.")
                if title == "" and author == "" and available == "":
                    print("Nothing to update.")
                else:
                    if not validate_isbn(isbn):
                        raise ValueError("Invalid ISBN format. Please enter a valid ISBN.")
                    if book_manager.update_book(isbn, title if title else None, author if author else None, available if available else None):
                        logging.info(f"Updated book: {isbn}")
                        print("Book updated.")
                    else:
                        print("Book not found.")

            elif choice == '3':
                isbn = input("Enter ISBN of the book to delete: ").strip()
                if book_manager.delete_book(isbn):
                    logging.info(f"Deleted book: {isbn}")
                    print("Book deleted.")
                else:
                    print("Book not found.")

            elif choice == '4':
                books = book_manager.list_books()
                if books:
                    for book in books:
                        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available: {book['available']}")
                else:
                    print("No books available.")

            elif choice == '5':
                criteria = {}
                title = input("Enter title to search (leave blank to ignore): ").strip()
                author = input("Enter author to search (leave blank to ignore): ").strip()
                isbn = input("Enter ISBN to search (leave blank to ignore): ").strip()
                if title:
                    criteria['title'] = title
                if author:
                    criteria['author'] = author
                if isbn:
                    if not validate_isbn(isbn):
                        raise ValueError("Invalid ISBN format. Please enter a valid ISBN.")
                    criteria['isbn'] = isbn
                books = book_manager.find_books(criteria)
                if books:
                    for book in books:
                        print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available: {book['available']}")
                else:
                    print("No books found.")

            elif choice == '6':
                name = input("Enter user name: ").strip()
                user_id = input("Enter user ID: ").strip()
                if not validate_user_id(user_id):
                    raise ValueError("Invalid user ID format. Please enter a valid user ID.")
                user_manager.add_user(name, user_id)
                logging.info(f"Added user: {name}, {user_id}")
                print("User added.")

            elif choice == '7':
                user_id = input("Enter user ID to update: ").strip()
                name = input("Enter new name (leave blank to keep current): ").strip()
                if user_manager.update_user(user_id, name if name else None):
                    logging.info(f"Updated user: {user_id}")
                    print("User updated.")
                else:
                    print("User not found.")

            elif choice == '8':
                user_id = input("Enter user ID to delete: ").strip()
                if user_manager.delete_user(user_id):
                    logging.info(f"Deleted user: {user_id}")
                    print("User deleted.")
                else:
                    print("User not found.")

            elif choice == '9':
                users = user_manager.list_users()
                if users:
                    for user in users:
                        print(f"Name: {user['name']}, User ID: {user['user_id']}")
                else:
                    print("No users available.")

            elif choice == '10':
                criteria = {}
                name = input("Enter name to search (leave blank to ignore): ").strip()
                user_id = input("Enter user ID to search (leave blank to ignore): ").strip()
                if name:
                    criteria['name'] = name
                if user_id:
                    if not validate_user_id(user_id):
                        raise ValueError("Invalid user ID format. Please enter a valid user ID.")
                    criteria['user_id'] = user_id
                users = user_manager.find_users(criteria)
                if users:
                    for user in users:
                        print(f"Name: {user['name']}, User ID: {user['user_id']}")
                else:
                    print("No users found.")

            elif choice == '11':
                user_id = input("Enter user ID: ").strip()
                isbn = input("Enter ISBN of the book to checkout: ").strip()
                if not validate_isbn(isbn):
                    raise ValueError("Invalid ISBN format. Please enter a valid ISBN.")
                if checkout_manager.checkout_book(user_id, isbn):
                    logging.info(f"Book checked out: {isbn} by {user_id}")
                    print("Book checked out.")
                else:
                    print("Book not available or not found.")

            elif choice == '12':
                isbn = input("Enter ISBN of the book to checkin: ").strip()
                if not validate_isbn(isbn):
                    raise ValueError("Invalid ISBN format. Please enter a valid ISBN.")
                if checkout_manager.checkin_book(isbn):
                    logging.info(f"Book checked in: {isbn}")
                    print("Book checked in.")
                else:
                    print("Book not found or already available.")

            elif choice == '13':
                checkouts = checkout_manager.list_checkouts()
                if checkouts:
                    for checkout in checkouts:
                        print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}")
                else:
                    print("No checkouts available.")

            elif choice == '14':
                print("Exiting.")
                break

            else:
                print("Invalid choice, please try again.")

        except ValueError as ve:
            print(f"ValueError: {ve}")
            logging.error(f"ValueError in main menu processing: {ve}")
        except KeyError as ke:
            print(f"KeyError: {ke}")
            logging.error(f"KeyError in main menu processing: {ke}")
        except Exception as e:
            print(f"Error: {e}")
            logging.error(f"Error in main menu processing: {e}")

if __name__ == "__main__":
    main()
