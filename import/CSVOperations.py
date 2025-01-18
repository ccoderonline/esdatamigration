import json
from datetime import datetime
import pandas as pd

class CSVHandler:
    def read_csv(self, file_path):
        return pd.read_csv(file_path)

    def validate_data(self, df):
        errors = []
        for index, row in df.iterrows():
            try:
                datetime.strptime(row['date'], '%Y-%m-%d')
                json.loads(row['inventory'])
                json.loads(row['salaries'])
                required_columns = ['upi', 'cash', 'card', 'foodappsettlement', 'others']
                for col in required_columns:
                    if col not in row:
                        raise KeyError(f"Column '{col}' is missing in the data")
                assert float(row['upi']) >= 0 and float(row['cash']) >= 0 and float(row['card']) >= 0 and float(row['foodappsettlement']) >= 0 and float(row['others']) >= 0
            except Exception as e:
                errors.append((index, str(e)))
        return errors

    def split_data(self, df):
        date_data = df[['date', 'day', 'status', 'importance']]
        expenses_data = df[['date', 'day', 'inventory', 'salaries']]
        collection_data = df[['date', 'day', 'upi', 'cash', 'card', 'foodappsettlement', 'others']]
        return date_data, expenses_data, collection_data