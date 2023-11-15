from pymongo.collection import Collection
import logging

class Stores:
    """
    Represents a store and provides methods to insert store information into a MongoDB collection.

    Example Usage:
    ```python
    # Create a MongoDB collection
    collection = db['stores']

    # Create a new store object
    store = Stores('Store A', '123 Main St', 'John Doe', collection)

    # Insert the store information into the collection
    store.insert()
    ```

    Methods:
    - __init__(self, name, address, manager, collection: Collection) -> None: Initializes a new `Stores` object with the provided name, address, manager, and MongoDB collection.
    - to_dic(self): Converts the store information to a dictionary format.
    - insert(self): Inserts the store information into the MongoDB collection.

    Fields:
    - name: The name of the store.
    - address: The address of the store.
    - manager: The manager of the store.
    - store_collection: The MongoDB collection used to store the store information.
    """

    def __init__(self, name, address, manager, collection: Collection) -> None:
        self.name = name
        self.address = address
        self.manager = manager
        self.store_collection = collection
    
    def to_dic(self):
        """
        Converts the store information to a dictionary format.

        Returns:
        dict: The store information in dictionary format.
        """
        return {
            'Nombre': self.name,
            'Dirección': self.address,
            'Encargado': self.manager
        }
    
    def insert(self):
        """
        Inserts the store information into the MongoDB collection.

        Returns:
        bool: True if the insertion is successful, False otherwise.
        """
        try:
            self.store_collection.insert_one(self.to_dic())
            return True
        except Exception as e:
            logging.error(e)
            raise ValueError(e)
    
    def get_next_id(self):
        try:
            id = self.store_collection.count_documents({})

            return id + 1
        except Exception as e:
            logging.error(e)
            raise ValueError(e)