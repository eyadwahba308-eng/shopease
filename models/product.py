
from factories.factory_repo import RepositoryFactory


class Product:
    def __init__(self, id, name, price):
        self.id = int(id)
        self.name = name
        self.price = float(price)

    @staticmethod
    def get_all():
        repo = RepositoryFactory.get_repository("product")
        rows = repo.get_all()

        products = []

        for r in rows:
            products.append(
                Product(r["id"], r["name"], r["price"])
            )

        return products

    @staticmethod
    def get_by_id(id):
        repo = RepositoryFactory.get_repository("product")
        r = repo.get_by_id(id)

        if r:
            return Product(r["id"], r["name"], r["price"])

        return None
