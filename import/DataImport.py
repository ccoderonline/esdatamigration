import argparse
from CSVOperations import CSVHandler
from MysqlOperations import MySQLDatabase
from AzuresqlOperations import AzureSQLDatabase

class DataImporter:
    def __init__(self, db_type, server, database, username, password):
        self.db_type = db_type
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = self.connect_to_database()
        self.csv_handler = CSVHandler()

    def connect_to_database(self):
        if self.db_type == 'mysql':
            return MySQLDatabase(self.server, self.database, self.username, self.password)
        else:
            return AzureSQLDatabase(self.server, self.database, self.username, self.password)

    def import_data(self, input_file):
        df = self.csv_handler.read_csv(input_file)
        errors = self.csv_handler.validate_data(df)
        
        if errors:
            for error in errors:
                print(f"Error in row {error[0]}: {error[1]}")
            return
        
        expenses_data, collection_data = self.csv_handler.split_data(df)
        
        cursor = self.conn.conn.cursor()
        
        for _, row in expenses_data.iterrows():
            self.conn.insert_expenses(cursor, row)
        
        for _, row in collection_data.iterrows():
            self.conn.insert_collection(cursor, row)
        
        self.conn.conn.commit()
        cursor.close()
        print("Data successfully imported into the database")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Import data into MySQL or Azure SQL database")
    parser.add_argument('--db_type', choices=['mysql', 'azure'], default='mysql', help="Type of database (mysql or azure)")
    parser.add_argument('input_file', help="Path to the input CSV file")
    parser.add_argument('server', help="Database server address")
    parser.add_argument('database', help="Database name")
    parser.add_argument('username', help="Database username")
    parser.add_argument('password', help="Database password")
    return parser.parse_args()

def main():
    args = parse_arguments()
    importer = DataImporter(args.db_type, args.server, args.database, args.username, args.password)
    importer.import_data(args.input_file)

if __name__ == "__main__":
    main()
    # To run this script from the command line, use the following command:
    # python /d:/KiranT/CCODESGIT/esdatamigration/import/DataImport.py <--db_type> <mysql|azure> <input_file> <server> <database> <username> <password>