# MongoDB Data Importer from CSV

This Python script is designed to import data from a CSV file into a MongoDB database. It extracts specific fields from the CSV file, adds additional fields, and inserts the data into a MongoDB collection.

## Usage

### Prerequisites

1. Python installed on your system ([Download Python](https://www.python.org/downloads/))
2. MongoDB installed on your system or accessible via a remote server ([Download MongoDB](https://www.mongodb.com/try/download/community))

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/JeffreyAndrew/mongo-csv-importer.git
    ```

2. Install the required Python packages:

    ```bash
    pip install pymongo
    ```

### Running the Script

1. Navigate to the directory where the script is located.

2. Execute the script:

    ```bash
    python mongo_import.py
    ```

3. Follow the prompts to enter your MongoDB credentials and database details.

4. The script will then read the `Data.csv` file (make sure it's in the same directory) and import the data into your MongoDB database.

## CSV File Format

Ensure that the CSV file (`Data.csv`) follows the specified format with columns matching the fields listed in the script.

## Notes

- This script assumes that the MongoDB server is running and accessible.
