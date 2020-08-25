import pyodbc


def create_procedure(cursor):
    print("--> Creating test_proc procedure")
    cursor.execute("""
  CREATE PROCEDURE test_proc_2
  AS BEGIN
    PRINT 'foo'
    WAITFOR DELAY '00:00:20'
    PRINT 'bar'
    WAITFOR DELAY '00:00:20'
  END
  """)


server = "mssql-server"
port = "1433"
user = "SA"
pwd = "t3st_Password"

conn_str = f"DRIVER=FreeTDS;SERVER={server};PORT={port};UID={user};PWD={pwd};TDS_VERSION=8.0;"

with pyodbc.connect(conn_str) as conn:
    with conn.cursor() as cursor:
        create_procedure(cursor)
