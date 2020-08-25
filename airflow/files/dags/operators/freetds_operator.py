import pyodbc
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class FreeTDSOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 sql: str,
                 conn: dict,
                 autocommit: bool = False,
                 *args,
                 **kwargs
                 ):
        super(FreeTDSOperator, self).__init__(*args, **kwargs)
        self.autocommit = autocommit
        self.sql = sql
        self.conn = conn

    def execute(self, context):
        with self._setup_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(self.sql)

    def _setup_connection(self):
        conn_str: str = f"DRIVER=FreeTDS;SERVER={self.conn['server']};PORT={self.conn['port']};UID={self.conn['user']};PWD={self.conn['pwd']};TDS_VERSION=8.0"
        conn = pyodbc.connect(conn_str, autocommit=self.autocommit)
        return conn
