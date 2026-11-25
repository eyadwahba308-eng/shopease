
from core.db_connection import DatabaseConnection
from core.file_manager import FileManager


class MySQLProductRepository:
    def __init__(self):
        self.db = DatabaseConnection().get_connection()

    def get_all(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT id, name, price FROM products")

        return cursor.fetchall()

    def get_by_id(self, id):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, name, price FROM products WHERE id=%s",
            (id,)
        )

        return cursor.fetchone()


class CSVProductRepository:
    def __init__(self):
        self.file = FileManager()

    def get_all(self):
        rows = self.file.read_csv("data/products.csv")
        products = []

        for r in rows:
            product = {
                "id": int(r["id"]),
                "name": r["name"],
                "price": float(r["price"])
            }

            products.append(product)

        return products

    def get_by_id(self, id):
        products = self.get_all()

        for row in products:
            if row["id"] == id:
                return row

        return None
