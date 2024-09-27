import psycopg2
import psycopg2 as dbconnector

DB_CONN_STRING = dict(dbname="productdb",
                      host="ed-v-mntperf-124.be.core.pw",
                      user="productdbuser",
                      password="temppass",
                      port="5432")

class DBManager:
    def __init__(self, db):
        self.db = db
        self.connection = None
        self.__cursor = None

    def connect(self, db=None):
        if db is None:
            db = self.db
        self.connection = dbconnector.connect(
            dbname = db.name,
            host = db.host,
            user = db.user.name,
            password = db.user.password,
            port = db.port
        )
        self.connection.autocommit = True
        return self.connection

    @property
    def cursor(self):
        if self.__cursor is None:
            self.__cursor = self.connection.cursor()
        return self.__cursor

class DB:
    def __init__(self, dbname, user):
        self.name = dbname
        self.user = user

class PostgresDB(DB):
    def __init__(self, host, port, dbname, user):
        super().__init__(dbname, user=user)
        self.host = host
        self.port = port

class DBUser:
    def __init__(self, user, password):
        self.name = user
        self.password = password


def test():
    user = DBUser(DB_CONN_STRING["user"], DB_CONN_STRING["password"])
    db = PostgresDB(host=DB_CONN_STRING["host"], dbname=DB_CONN_STRING["dbname"], user=user, port=DB_CONN_STRING["port"])
    pm = DBManager(db)
    pm.connect()

    print(pm.connection)
    # pm.cursor.execute(
    #     """CREATE TABLE products
    #                     (id serial,
    #                     name varchar(255),
    #                     protein decimal,
    #                     fat decimal,
    #                     carb decimal
    #                     );""")

    pm.cursor.execute("""select * from products""")
    print(pm.cursor.fetchall())


if __name__ == "__main__":
    test()