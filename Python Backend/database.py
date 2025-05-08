import cx_Oracle
from config import DB_USERNAME, DB_PASSWORD, DB_DSN

# Implement connection pooling for scalability
pool = cx_Oracle.SessionPool(
    DB_USERNAME,
    DB_PASSWORD,
    DB_DSN,
    min=2,
    max=10,
    increment=1,
    threaded=True
)

# Acquire a connection from the pool
connection = pool.acquire()
cursor = connection.cursor()