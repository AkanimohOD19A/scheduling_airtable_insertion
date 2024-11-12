from pyairtable import Api
from autoRecords import generate_random_records

def setup_airtable_connection(api_key):
    """
    Set up connection
    :param api_key:
    :return:
    """

    return Api(api_key)


def fetch_table_and_insert_data(api, base_id, table_name, records):
    """
    Connect to a table (Table creation is not allowed via API), then,
    Insert data
    :param num_records: Number of records to generate
    :param api:
    :param base_id:
    :param table_name:
    :return:
    """
    table = api.table(base_id, table_name)
    # auto_records = generate_random_records(num_records)
    # Batch Insert records
    insert_records = table.batch_create(records)
    return insert_records


def retrieve_data(api, base_id, table_name, filter_formula=None):
    """
    Retrieve data from table with optional filtering
    :param api:
    :param base_id:
    :param table_name:
    :param filter_formula:
    :return:
    """

    table = api.table(base_id, table_name)
    if filter_formula:
        records = table.all(formula=filter_formula)
    else:
        records = table.all()

    return records