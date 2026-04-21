from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username # aacuser
        PASS = password # pass123
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        try:
            if data is not None: 
                self.collection.insert_one(data)  
                return True
            return False 
        except Exception as e:
            print(f"Create error: {e}")
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        try:
            if query is not None:
                cursor = self.collection.find(query)
                return list(cursor)
            return []
        except Exception as e:
            print(f"Read error: {e}")
            return []
        
    def update(self, query, data):
        try:
            if query is not None and data is not None:
                result = self.collection.update_many(query, {"$set": data})
                return result.modified_count
            else:
                return 0
        except Exception:
            return 0
    
    def delete(self, query):
        try:
            if query is not None:
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                return 0
        except Exception:
            return 0