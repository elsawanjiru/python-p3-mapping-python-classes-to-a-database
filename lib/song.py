import sqlite3

class Song:
    CONN = None
    CURSOR = None

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        cls.CONN = sqlite3.connect('db/music.db')  
        cls.CURSOR = cls.CONN.cursor()

        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        cls.CURSOR.execute(sql)
        cls.CONN.commit()

    @classmethod
    def close_connection(cls):
        if cls.CONN:
            cls.CONN.close()

    def save(self):
        if not self.CONN or not self.CURSOR:
            raise ValueError("Database connection is not established. Call create_table() first.")

        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        self.CURSOR.execute(sql, (self.name, self.album))
        self.id = self.CURSOR.lastrowid
        self.CONN.commit()
