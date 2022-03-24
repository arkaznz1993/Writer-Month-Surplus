import os
import mysql.connector
from mysql.connector.constants import ClientFlag

# Instance name - flash-hour-338103:asia-south1:test-sql-server

config = {
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': '35.200.140.194',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': os.environ.get('SSL_CA'),
    'ssl_cert': os.environ.get('SSL_CERT'),
    'ssl_key': os.environ.get('SSL_KEY'),
    'database': os.environ.get('DB_NAME'),
}

INSERT_CARD = 'INSERT INTO CardDetails (' \
              'CardId, CardTitle, WordCount, Client, Writer, SubmittedDate, Status)' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s) ' \
              'ON DUPLICATE KEY UPDATE ' \
              'CardTitle = VALUES(CardTitle),' \
              'WordCount = VALUES(WordCount),' \
              'Client = VALUES(Client),' \
              'Writer = VALUES(Writer),' \
              'SubmittedDate = VALUES(SubmittedDate),' \
              'Status = VALUES(Status);'


class DatabaseConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def insert_card_details(self, values):
        self.cursor.executemany(INSERT_CARD, values)
        self.connection.commit()


database_connection = DatabaseConnector()
