import csv
import time
from pymongo import MongoClient


# Fields to extract from the CSV file
fields_to_extract = [
    'cid',
    'name',
    'radio',
    'azimut',
    'zipCode',
    'address',
    'operator',
    'latitude',
    'longitude',
    'amplitude',
    'technology'
]

# Request MongoDB credentials from the user
mongodb_user = input("MongoDB username: ")
mongodb_password = input("MongoDB password: ")
mongodb_host = input("MongoDB host (e.g., 192.168.1.1): ")
mongodb_port = input("MongoDB port (default is 27017): ") or '27017'
mongodb_database = input("MongoDB database: ")

# Construct MongoDB connection URI
mongodb_uri = f"mongodb://{mongodb_user}:{mongodb_password}@{mongodb_host}:{mongodb_port}/{mongodb_database}"

try:
    client = MongoClient(mongodb_uri)

    server_info = client.server_info()
    print(f"Connected to MongoDB server version {server_info['version']} successfully!")

    db = client[mongodb_database]
    collection = db.BroadcastElement # Name of the collection

    start_time = time.time()

    # Open and read the CSV file
    with open('Data.csv', 'r', encoding='ISO-8859-1') as input_file:
        csv_reader = csv.DictReader(input_file, delimiter=',')

        # Iterate over CSV rows
        for row in csv_reader:
            # Extract specific values from each row according to defined fields
            extracted_values = {field: row[field] if field in row else '' for field in fields_to_extract}

            # Add additional fields and values
            extracted_values['accountId'] = '658c5efc67758415091bd0f0'
            extracted_values['status'] = 'true'
 
            # Insert into MongoDB collection
            collection.insert_one(extracted_values)

            print(f"Inserted record: {extracted_values}")
    
    end_time = time.time()
    execution_time_seconds = end_time - start_time
    execution_time_minutes = execution_time_seconds // 60
    execution_time_seconds %= 60

    print(f"Data inserted into MongoDB successfully!")
    print(f"Number of records inserted: {collection.count_documents({})}")
    print(f"Execution time: {int(execution_time_minutes)} minutes and {execution_time_seconds:.2f} seconds")

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")