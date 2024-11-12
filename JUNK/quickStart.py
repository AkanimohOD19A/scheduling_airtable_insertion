import os
from dotenv import load_dotenv
from pyairtable import Api

load_dotenv()
api = os.getenv('API_KEY')
print(api)