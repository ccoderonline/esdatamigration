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
            INSERT INTO expenses (date, day, inventory, salaries)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            day = VALUES(day),
            inventory = VALUES(inventory),
            salaries = VALUES(salaries)
        """, (row['date'], row['day'], row['inventory'], row['salaries']))

    def insert_collection(self, cursor, row):
        cursor.execute("""
            INSERT INTO collection (date, day, upi, cash, card, foodappsettlement, others)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            day = VALUES(day),
            upi = VALUES(upi),
            cash = VALUES(cash),
            card = VALUES(card),
            foodappsettlement = VALUES(foodappsettlement),
            others = VALUES(others)
        """, (row['date'], row['day'], row['upi'], row['cash'], row['card'], row['foodappsettlement'], row['others']))