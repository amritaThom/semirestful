
from system.core.model import Model

class WelcomeModel(Model):
    def __init__(self):
        super(WelcomeModel, self).__init__()

    def get_product(self):
        query = "SELECT * FROM product"
        return self.db.query_db(query)

    def add_product(self, name, description, price):
        query = "INSERT INTO product (name, description, price, created_at, updated_at) VALUES (:name, :description, :price, NOW(), NOW())"
        data = {'name': name,'description': description, 'price': price}
        return self.db.query_db(query,data)

    def get_id(self,id):
        query = "SELECT * FROM product where id = :id"
        data = {'id': id}
        return self.db.query_db(query,data)

    def update_info(self, id, name, description, price):
        query = "UPDATE product SET name = :name, description = :description, price = :price WHERE id = :id"
        data = {
             'name': name, 
             'description':  description,
             'price': price,
             'id':id
            }
        return self.db.query_db(query,data)
    def delete(self,id):
        query = "DELETE FROM product WHERE id = '{}'".format(id)
        return self.db.query_db(query)
