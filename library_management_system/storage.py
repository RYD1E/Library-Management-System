import json

class Storage:
    def __init__(self, filename):
        """ 
        Initialize a Storage instance.
        
        Args:
            filename: The name of the file to load/save data from/to.
        """
        self.filename = filename
        self.load()

    def load(self):
        """ 
        Load data from the JSON file into memory.
        """
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save(self):
        """ 
        Save data from memory back to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add(self, collection, item):
        """ 
        Add an item to a collection in the storage.
        
        Args:
            collection: The name of the collection to add the item to.
            item: The item (dictionary) to add to the collection.
        """
        if collection not in self.data:
            self.data[collection] = []
        self.data[collection].append(item)
        self.save()

    def update(self, collection, index, item):
        """ 
        Update an item in a collection.
        
        Args:
            collection: The name of the collection containing the item.
            index: The index of the item in the collection.
            item: The updated item (dictionary) to replace the existing item.
        """
        self.data[collection][index] = item
        self.save()

    def delete(self, collection, index):
        """ 
        Delete an item from a collection.
        
        Args:
            collection: The name of the collection containing the item.
            index: The index of the item to delete from the collection.
        """
        del self.data[collection][index]
        self.save()

    def list(self, collection):
        """ 
        Retrieve all items from a collection.
        
        Args:
            collection: The name of the collection to retrieve items from.
        
        Returns:
            list: A list of all items in the collection.
        """
        return self.data.get(collection, [])

    def find(self, collection, criteria):
        """ 
        Find items in a collection based on given criteria.
        
        Args:
            collection: The name of the collection to search within.
            criteria: A dictionary specifying the criteria to match items against.
        
        Returns:
            list: A list of items (dictionaries) matching the criteria.
        """
        return [item for item in self.data.get(collection, []) if all(item[k] == v for k, v in criteria.items())]
