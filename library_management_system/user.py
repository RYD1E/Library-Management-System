from .models import User

class UserManager:
    def __init__(self, storage):
        """ 
        Initialize the UserManager with a storage instance.
        
        Args:
            storage: An instance of the storage to interact with.
        """
        self.storage = storage

    def add_user(self, name, user_id):
        """ 
        Add a new user to the storage.
        
        Args:
            name: The name of the user.
            user_id: The ID of the user.
        """
        user = User(name, user_id)
        self.storage.add('users', user.to_dict())

    def update_user(self, user_id, name=None):
        """ 
        Update the details of a user in the storage.
        
        Args:
            user_id: The ID of the user to update.
            name: (Optional) The new name of the user.
        
        Returns:
            bool: True if the user was found and updated, False otherwise.
        """
        users = self.storage.list('users')
        for index, user in enumerate(users):
            if user['user_id'] == user_id:
                if name is not None:
                    user['name'] = name
                self.storage.update('users', index, user)
                return True
        return False

    def delete_user(self, user_id):
        """ 
        Delete a user from the storage.
        
        Args:
            user_id: The ID of the user to delete.
        
        Returns:
            bool: True if the user was found and deleted, False otherwise.
        """
        users = self.storage.list('users')
        for index, user in enumerate(users):
            if user['user_id'] == user_id:
                self.storage.delete('users', index)
                return True
        return False

    def list_users(self):
        """ 
        List all users currently stored.
        
        Returns:
            list: A list of dictionaries representing all users.
        """
        return self.storage.list('users')

    def find_users(self, criteria):
        """ 
        Find users based on given criteria.
        
        Args:
            criteria: A dictionary specifying the criteria to search for.
        
        Returns:
            list: A list of dictionaries representing users matching the criteria.
        """
        return self.storage.find('users', criteria)
