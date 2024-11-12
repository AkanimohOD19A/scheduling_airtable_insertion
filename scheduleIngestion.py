import os
from dotenv import load_dotenv
from pyairtable import Api
from pyairtable.formulas import match
from datetime import datetime
import schedule
import time
import logging
from autoRecords import *

# Set Up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('airtable_ingestion.log'),
        logging.StreamHandler
    ]
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


def ingest_data():
    """Handling the data ingestion process"""

    try:
        # Initiate Connection
        api = Api(API_KEY)
        table = api.table(BASE_ID, TABLE_NAME)

        # Generate and prep. data
        num_records = 50
        auto_records = generate_random_records(num_records)
        prepd_records = prep_for_insertion(auto_records)

        # Insert Data
        logger.info("Starting record insertion... ")
        created_records = table.batch_create(prepd_records)
        logger.info(f"Successfully inserted {len(created_records)} records at {datetime.now()}")

        # Verify Insertion
        first_record = table.first()
        logger.info(f"Verification - Last inserted record: {first_record['fields']['ID']}")

    except Exception as e:
        # print(f"An error occurred: {str(e)}")
        logger.error(f"Error during data ingestion: {str(e)}")


def main():
    logger.info("Starting scheduled data ingestion service...")

    # Schedule the job to run every 30 minutes
    schedule.every(30).minutes.do(ingest_data)

    # Run immediately on start
    logger.info("Performing initial data ingestion")
    ingest_data()

    # Keep script running
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # check every minute for pending job
        except KeyboardInterrupt:
            logger.info("Scheduled service stopped by user")
            break
        except Exception as e:
            logger.error(f"Error in main loop: {str(e)}")
            time.sleep(300)  # Wait before retrying | 5 minutes
            continue


if __name__ == "__main__":
    main()
