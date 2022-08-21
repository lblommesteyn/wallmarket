class Product:
    def __init__(self, name=None, id=None, skuIds=None, description=None,
                 image=None, price=None):
        self.name = name
        self.id = id
        self.skuIds = skuIds
        self.description = description
        self.image = image
        self.price = price

    def __repr__(self):
        return str(self.__dict__)
