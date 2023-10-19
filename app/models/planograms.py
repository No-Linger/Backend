from pymongo import collection

class Planograms:
    def __init__(self, name: str, store: str, date: str, img:str, collection: collection) -> None:
        self.name = name
        self.store = store
        self.date = date
        self.img = img 
        self.collection = collection
    
    def to_dic(self):
        return {
            'name': self.name,
            'store': self.store,
            'date': self.date,
            'img': self.img
        }

    def insert(self):
        try:
            self.collection.insert_one(self.to_dic())
            return True
        except Exception as e:
            print(e)
            return False