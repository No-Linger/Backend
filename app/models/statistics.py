from pymongo.collection import Collection

class Statistics:
    """
    Represents statistical data and provides methods to convert and insert the data.

    Args:
        date (str): The date of the statistics.
        time (str): The time of the statistics.
        model_percentage (str): The model percentage of the statistics.
        error_percentage (str): The error percentage of the statistics.
        collection (collection): The MongoDB collection where the statistics will be stored.
    """

    def __init__(self, date: str, time: str, model_percentage: str, error_percentage: str, collection: Collection) -> None:
        """
        Initializes a Statistics instance with the provided data and a MongoDB collection.

        Args:
            date (str): The date of the statistics.
            time (str): The time of the statistics.
            model_percentage (str): The model percentage of the statistics.
            error_percentage (str): The error percentage of the statistics.
            collection (collection): The MongoDB collection where the statistics will be stored.
        """
        self.date = date
        self.time = time
        self.model_percentage = model_percentage
        self.error_percentage = error_percentage
        self.statsCollection = collection
    

    def to_dic(self):
        """
        Converts the Statistics instance to a dictionary format.

        Returns:
            dict: A dictionary representation of the Statistics instance.
        """
        return {
            'date': self.date,
            'time': self.time,
            'model_percentage': self.model_percentage,
            'error_percentage': self.error_percentage,
        }
    
    def insert(self):
        """
        Inserts the Statistics instance into the MongoDB collection.

        Returns:
            bool: True if the insertion is successful, False otherwise.
        """
        try:
            self.statsCollection.insert_one(self.to_dic())
            return True
        except Exception as e:
            print(e)
            return False
        
    def insert_many(self, stats: list):
        """
        Inserts multiple Statistics instances into the MongoDB collection.

        Args:
            stats (list): A list of dictionaries representing multiple Statistics instances.

        Raises:
            ValueError: If an unexpected error occurs during insertion.

        Returns:
            None
        """
        try:
            self.statsCollection.insert_many(stats)
        except Exception as e:
            print(e)
            raise ValueError("Unexpected error", e)
            
