import os
from dotenv import load_dotenv
from pyairtable import Api
import logging
from autoRecords import *

# Set Up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment vars
load_dotenv()

# Credentials
API_KEY = os.getenv("API_KEY")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")


def prep_for_insertion(generated_records):
    """Convert records from nested to a flat format"""
    return [record['fields'] for record in generated_records]


def main():
    # Initiate Connection
    api = Api(API_KEY)
    table = api.table(BASE_ID, TABLE_NAME)

    num_records = 50

    try:
        # Generate and prep. data
        auto_records = generate_random_records(num_records)
        prepd_records = prep_for_insertion(auto_records)

        # Insert Data
        print("inserting records... ")
        # created_records = fetch_table_and_insert_data(api, BASE_ID, TABLE_NAME, auto_records)
        created_records = table.batch_create(prepd_records)
        print(f"Successfully inserted {len(created_records)} records")

        # if

        # # Retrieve Data
        # print("\nRetrieving all records... ")
        # all_records = retrieve_data(api, BASE_ID, TABLE_NAME)
        # print(f"Found {len(all_records)} records")
        #
        # for record in all_records:
        #     print(f"Record ID: {record['id']}")
        #     print(f"Fields: {record['fields']}\n")
        #
        # # Filtered Data: Optional
        # print("Retrieving filtered records... ")
        # filter_formula = match({"Age": 30})
        # filtered_records = retrieve_data(api, BASE_ID, TABLE_NAME, filter_formula)
        # print(f"Found {len(all_records)} filtered records matching filter")

    except Exception as e:
        # print(f"An error occurred: {str(e)}")
        logger.error(f"An error occurred: {str(e)}")
        raise


if __name__ == "__main__":
    main()
