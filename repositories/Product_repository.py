
from config.database_config import STORAGE
from core.db_connection import DatabaseConnection
from core.file_manager import FileManager


class ProductRepository:

    @staticmethod
    def get_all():
        if STORAGE == "mysql":
            db = DatabaseConnection().get_connection()
            cursor = db.cursor(dictionary=True)

            cursor.execute("SELECT id, name, price FROM products")
            rows = cursor.fetchall()

            return rows

        return FileManager().read_csv("data/products.csv")

    @staticmethod
    def get_by_id(id):
        if STORAGE == "mysql":
            db = DatabaseConnection().get_connection()
            cursor = db.cursor(dictionary=True)

            cursor.execute(
                "SELECT id, name, price FROM products WHERE id=%s",
                (id,)
            )

            return cursor.fetchone()

        rows = FileManager().read_csv("data/products.csv")

        for r in rows:
            if int(r["id"]) == id:
                return r

        return None
