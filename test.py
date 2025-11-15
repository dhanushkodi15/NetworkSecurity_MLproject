import pymongo
import certifi
from dotenv import load_dotenv
import os

def test_connection():
    load_dotenv()
    MONGO_DB_URL = os.getenv('MONGO_DB_URL')
    
    try:
        client = pymongo.MongoClient(
            MONGO_DB_URL,
            tls=True,
            tlsCAFile=certifi.where()
        )
        
        client.admin.command('ping')
        print("MongoDB connection successful!")
        return True
    except Exception as e:
        print(f"Connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_connection()
    