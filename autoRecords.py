from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker for generating realistic data
fake = Faker()


def generate_unique_id():
    """Generate a Unique ID in the format N-#####"""
    return f"N-{random.randint(10000, 99999)}"

def generate_random_records(num_records=10):
    """
    Generate random records with reasonable constraints
    :param num_records: Number of records to generate
    :return: List of records formatted for Airtable
    """
    records = []

    # Constants
    departments = ['Sales', 'Engineering', 'Marketing', 'HR', 'Finance', 'Operations']
    statuses = ['Active', 'On Leave', 'Contract', 'Remote']

    for _ in range(num_records):
        # Generate date in the correct format
        random_date = datetime.now() - timedelta(days=random.randint(0, 365))
        formatted_date = random_date.strftime('%Y-%m-%dT%H:%M:%S.000Z')

        record = {
            'fields': {
                'ID': generate_unique_id(),
                'Name': fake.name(),
                'Age': random.randint(18, 80),
                'Email': fake.email(),
                'Department': random.choice(departments),
                'Salary': round(random.uniform(30000, 150000), 2),
                'Phone': fake.phone_number(),
                'Address': fake.address().replace('\n', '\\n'),  # Escape newlines
                'Date Added': formatted_date,
                'Status': random.choice(statuses),
                'Years of Experience': random.randint(0, 45)
            }
        }
        records.append(record)

    return records

def prepare_records_for_airtable(records):
    """Convert records from nested format to flat format for Airtable"""
    return [record['fields'] for record in records]

if __name__ == "__main__":
    records = generate_random_records(2)
    print(records)
    prepared_records = prepare_records_for_airtable(records)
    print(prepared_records)