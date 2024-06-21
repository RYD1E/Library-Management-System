# Library Management System

This project is a Library Management System, designed to help manage books, users, and checkout processes in a library.

## Project Structure

The project contains the following key modules and files:

- **book.py**: Manages book-related functionalities.
- **checkout.py**: Handles the checkout process for users.
- **main.py**: Entry point for running the application.
- **models.py**: Contains data models for books and users.
- **storage.py**: Manages data storage and retrieval.
- **user.py**: Manages user-related functionalities.
- **test.py**: Contains unit tests for the various modules.

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or later installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/RYD1E/Library-Management-System.git
    cd Library-Management-System
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

To run the application, execute the following command:

```sh
python library_management_system/main.py
```

### Running the Tests

To run the tests, execute the following command:

```sh
python -m unittest discover -s tests
```
