import pymssql
import os

print("Testando mssql")

server = ""
user = ""
password = ""
database = ""

procedure = ""

with pymssql.connect(server, user, password, database) as conn:
  with conn.cursor(as_dict=True) as cursor:
    cursor.callproc(f"{procedure}")
    cursor.execute(f"exec {procedure}")