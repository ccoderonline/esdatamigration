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
            MERGE INTO dailyrecords.expenses AS target
            USING (SELECT ? AS date, ? AS inventory, ? AS salaries) AS source
            ON target.date = source.date
            WHEN MATCHED THEN
                UPDATE SET inventory = source.inventory, salaries = source.salaries
            WHEN NOT MATCHED THEN
                INSERT (date, inventory, salaries)
                VALUES (source.date, source.inventory, source.salaries);
        """, (row['date'], row['inventory'], row['salaries']))

    def insert_collection(self, cursor, row):
        cursor.execute("""
            MERGE INTO dailyrecords.collection AS target
            USING (SELECT ? AS date, ? AS upi, ? AS cash, ? AS card, ? AS foodappsettlement, ? AS others) AS source
            ON target.date = source.date
            WHEN MATCHED THEN
                UPDATE SET upi = source.upi, cash = source.cash, card = source.card, foodappsettlement = source.foodappsettlement, others = source.others
            WHEN NOT MATCHED THEN
                INSERT (date, upi, cash, card, foodappsettlement, others)
                VALUES (source.date, source.upi, source.cash, source.card, source.foodappsettlement, source.others);
        """, (row['date'], row['upi'], row['cash'], row['card'], row['foodappsettlement'], row['others']))

    def insert_date(self, cursor, row):
        cursor.execute("""
            MERGE INTO dailyrecords.date AS target
            USING (SELECT ? AS date, ? AS day, ? AS status, ? AS importance) AS source
            ON target.date = source.date
            WHEN MATCHED THEN
                UPDATE SET day = source.day, status = source.status, importance = source.importance
            WHEN NOT MATCHED THEN
                INSERT (date, day, status, importance)
                VALUES (source.date, source.day, source.status, source.importance);
        """, (row['date'], row['day'], row['status'], row['importance']))