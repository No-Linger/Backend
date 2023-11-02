from pymongo.collection import Collection
import logging

class Planograms:
    """
    A class representing a planogram, which is a visual representation of how products should be arranged on shelves in a store.

    Attributes:
        name (str): The name of the planogram.
        store (str): The store associated with the planogram.
        date (str): The date of the planogram.
        img_path (str): The path to the image file of the planogram.
        _collection (collection): A reference to a collection object from the `pymongo` library.
    """

    def __init__(self, name: str, store: str, date: str, img_path: str, collection: Collection) -> None:
        """
        Initializes a planogram object with the provided attributes.

        Args:
            name (str): The name of the planogram.
            store (str): The store associated with the planogram.
            date (str): The date of the planogram.
            img_path (str): The path to the image file of the planogram.
            collection (collection): A reference to a collection object from the `pymongo` library.
        """
        self.name = name
        self.store = store
        self.date = date
        self.img_path = img_path
        self._collection = collection
    
    def to_dic(self) -> dict:
        """
        Converts the planogram object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the planogram object.
        """
        return {
            'Nombre': self.name,
            'Tienda': self.store,
            'Fecha': self.date,
            'Ver': self.img_path
        }

    def insert(self) -> bool:
        """
        Inserts the planogram into a collection.

        Returns:
            bool: True if the planogram was successfully inserted, False otherwise.
        """
        try:
            self._collection.insert_one(self.to_dic())
            return True
        except Exception as e:
            logging.error(e)
            return False