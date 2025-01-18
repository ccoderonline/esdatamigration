import mysql.connector

class MySQLDatabase:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = self.connect_to_mysql_server()

    def connect_to_mysql_server(self):
        return mysql.connector.connect(
            host=self.server,
            database=self.database,
            user=self.username,
            password=self.password
        )

    def insert_expenses(self, cursor, row):
        cursor.execute("""
            INSERT INTO expenses (date, inventory, salaries)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            inventory = VALUES(inventory),
            salaries = VALUES(salaries)
        """, (row['date'], row['inventory'], row['salaries']))

    def insert_collection(self, cursor, row):
        cursor.execute("""
            INSERT INTO collection (date, upi, cash, card, foodappsettlement, others)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            upi = VALUES(upi),
            cash = VALUES(cash),
            card = VALUES(card),
            foodappsettlement = VALUES(foodappsettlement),
            others = VALUES(others)
        """, (row['date'], row['upi'], row['cash'], row['card'], row['foodappsettlement'], row['others']))

    def insert_date(self, cursor, row):
        cursor.execute("""
            INSERT INTO date (date, day, status, importance)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            day = VALUES(day),
            status = VALUES(status),
            importance = VALUES(importance)
        """, (row['date'], row['day'], row['status'], row['importance']))