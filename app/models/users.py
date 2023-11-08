from pymongo.collection import Collection
import logging

class Users:

    def __init__(self,id, name, email, phone,store_id,role, collection: Collection) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.store_id = store_id
        self.role = role
        self.collection = collection

    def to_dic(self) -> dict:
        return{
            '_id':self.id,
            'Nombre':self.name,
            'Email':self.email,
            'Telefono':self.phone,
            'Tienda_id':self.store_id,
            'Rol':self.role
        }
    def insert_user(self) -> bool:
        try:
            self.collection.insert_one(self.to_dic())
            return True
        except Exception as e:
            logging.error(e)
            return False
        
    

    