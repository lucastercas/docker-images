import pyodbc
import os

print("Testando pyodbc")

conn_str = """
DRIVER={ODBC Driver 17 for SQL Server};
SERVER=192.168.6.6;
DATABASE=mydb;
PORT=1443;
UID=user;
PWD=password;
"""
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()