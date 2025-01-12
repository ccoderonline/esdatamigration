import pyodbc

class AzureSQLDatabase:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = self.connect_to_microsoft_sql_server()

    def connect_to_microsoft_sql_server(self):
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password}"
        )
        return pyodbc.connect(conn_str)

    def insert_expenses(self, cursor, row):
        cursor.execute("""
            INSERT INTO expenses (date, day, inventory, salaries)
            VALUES (?, ?, ?, ?)
            ON DUPLICATE KEY UPDATE
            day = VALUES(day),
            inventory = VALUES(inventory),
            salaries = VALUES(salaries)
        """, (row['date'], row['day'], row['inventory'], row['salaries']))

    def insert_collection(self, cursor, row):
        cursor.execute("""
            INSERT INTO collection (date, day, upi, cash, card, foodappsettlement, others)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON DUPLICATE KEY UPDATE
            day = VALUES(day),
            upi = VALUES(upi),
            cash = VALUES(cash),
            card = VALUES(card),
            foodappsettlement = VALUES(foodappsettlement),
            others = VALUES(others)
        """, (row['date'], row['day'], row['upi'], row['cash'], row['card'], row['foodappsettlement'], row['others']))