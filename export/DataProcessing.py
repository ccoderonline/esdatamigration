import pandas as pd
import json
import re
from datetime import datetime

def read_csv(file_path):
    return pd.read_csv(file_path)

def parse_details(row):
    inventory = []
    salaries = []
    collections = {'upi': 0, 'cash': 0, 'foodappsettelment': 0, 'card': 0, 'others': 0}

    if 'chef_salary' in row and row['chef_salary'] == 'H':
        inventory.append('H')
        salaries.append('H')
        return inventory, salaries, collections

    inventory_columns = ['Tomato_Sauce', 'Chilly_Sauce', 'Tasting_Salt', 'Salt', 'Chilli_powder', 'Garam_Masala', 'Chicken_Masala', 'White_Pepper', 'Paper_Plates', 'Forks&Spoons', 'Handel_Covers', 'Parcel_Covers', 'Venigar', 'Ginger_Paste', 'Tooth_Picks', 'Food_Colour', 'Dry_Gobi', 'Rice_Bag', 'Oil', 'Eggs', 'Noodles', 'Vegetables', 'Chicken', 'Water', 'Gas', 'grocories', 'soya_Sauce', 'other_expenses']
    salary_columns = ['chef_salary']
    collection_columns = ['upi', 'cash', 'foodappsettelment']

    for col in inventory_columns:
        if col in row and not pd.isna(row[col]) and float(row[col]) > 0:
            inventory.append({'item': col, 'qty': 1, 'cost': float(row[col])})

    for col in salary_columns:
        if col in row and not pd.isna(row[col]):
            salaries.append({'name': 'naresh', 'salary': float(row[col])})

    for col in collection_columns:
        if col in row and not pd.isna(row[col]):
            collections[col] = float(row[col])
    
    return inventory, salaries, collections

def transform_data(df):
    structured_data = []
    
    for _, row in df.iterrows():
        date = datetime.strptime(row['Date'], '%m/%d/%Y')
        day = date.strftime('%A')
        inventory, salaries, collections = parse_details(row)
        
        structured_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'day': day,
            'inventory': json.dumps(inventory),
            'salaries': json.dumps(salaries),
            'upi': collections['upi'],
            'cash': collections['cash'],
            'card': collections['card'],
            'foodappsettelment': collections['foodappsettelment'],
            'others': collections['others']
        })
    
    return pd.DataFrame(structured_data)

def validate_data(df):
    errors = []
    for index, row in df.iterrows():
        try:
            datetime.strptime(row['date'], '%Y-%m-%d')
            json.loads(row['inventory'])
            json.loads(row['salaries'])
            assert row['upi'] >= 0 and row['cash'] >= 0 and row['card'] >= 0 and row['foodappsettelment'] >= 0 and row['others'] >= 0
            if row['inventory'] == 'H' and row['salaries'] == 'H':
                assert row['upi'] == 0 and row['cash'] == 0 and row['card'] == 0 and row['foodappsettelment'] == 0 and row['others'] == 0
        except Exception as e:
            errors.append((index, str(e)))
    
    return errors

def save_csv(df, file_path):
    df.to_csv(file_path, index=False)

def main(input_file, output_file):
    df = read_csv(input_file)
    transformed_df = transform_data(df)
    errors = validate_data(transformed_df)
    
    if errors:
        for error in errors:
            print(f"Error in row {error[0]}: {error[1]}")
    else:
        save_csv(transformed_df, output_file)
        print(f"Data successfully processed and saved to {output_file}")

if __name__ == "__main__":
    input_file = r"D:\\KiranT\\CCODESGIT\\unstructured_data.csv"
    output_file = r"D:\\KiranT\\CCODESGIT\\structured_data.csv"
    main(input_file, output_file)
