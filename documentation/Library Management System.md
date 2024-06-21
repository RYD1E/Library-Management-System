# Library Management System

## Overview
This library management system is designed to facilitate the management of books, users, and book checkouts/check-ins in a library. The system is implemented in Python and uses JSON for data storage. Logging is used to keep track of operations for auditing and debugging purposes.

## System Components
The system consists of the following main components:
1. **Book Management**: Handles the addition, updating, deletion, listing, and searching of books.
2. **User Management**: Handles the addition, updating, deletion, listing, and searching of users.
3. **Checkout Management**: Manages the checkout and check-in processes for books.

## Key Classes and Their Responsibilities
1. `Storage`: Handles reading from and writing to a JSON file to persist data.
2. `BookManager`: Manages operations related to books.
3. `UserManager`: Manages operations related to users.
4. `CheckoutManager`: Manages the process of checking out and checking in books.

## Logging
Logging is set up to write to `data/library.log`, and logs include timestamps and messages for actions performed, such as adding books or users, updating records, and errors encountered.

## Input Validation
The system includes validation functions to ensure that user inputs for ISBN and user IDs conform to expected formats:
- **ISBN Validation**: Must be either 10 or 13 digits.
- **User ID Validation**: Must be alphanumeric and 5-10 characters long.

## Usage
1. **Run the Application**: Execute `main.py` to start the library management system.
2. **Interact with the Menu**: Follow the menu prompts to manage books, users, and checkouts.

## Directory Structure
- **data/**: Contains data files such as `library.json`.
- **documentation/**: Contains project documentation.
- **library_management_system/**: Main package for the library management system.
- `__init__.py`: Package initializer.
- `book.py`: Book-related functionalities.
- `checkout.py`: Checkout process functionalities.
- `main.py`: Entry point of the application.
- `models.py`: Data models.
- `storage.py`: Data storage management.
- `user.py`: User-related functionalities.
- **tests/**: Contains unit tests.
- `__init__.py`: Test package initializer.
- `test.py`: Unit tests for the system.

## Design Decisions
- **JSON Storage**: Chosen for simplicity and ease of use in a standalone application.
- **Logging**: Provides a record of operations and errors for debugging and audit purposes.
- **Validation**: Ensures that user inputs conform to expected formats, reducing the risk of data errors.

## Future Enhancements
- **User Authentication**: Add login functionality to restrict access to authorized users.
- **Advanced Search**: Implement more sophisticated search criteria for books and users.
- **Graphical User Interface (GUI)**: Develop a graphical user interface for a more user-friendly experience.
- **Genre and Additional Book Information**: Include genres and other book-related details such as publication date and summary.
- **Collaborative Filtering for Book Recommendations**: Implement collaborative filtering to recommend books based on user preferences and borrowing history.
- **Popularity Tracking**: Track and display the number of times a book is checked out to determine its popularity.
- **Notification System**: Implement a notification system to alert users about due dates, new arrivals, and other relevant information.
- **Reports and Analytics**: Generate reports and analytics on library usage and user activity.
- **Mobile Application**: Develop a mobile application for accessing the library management system on smartphones and tablets.
