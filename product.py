from uuid import uuid4

class Product():
    """
    Product class
    """

    def __init__(self, id="", product_name="", category=""):
        """
        Initializes a new product
        """
        if not id:
            self.id = f"{str(uuid4())}-{category}"
        else:
            self.id = id
        self.name = product_name
        self.category = category
        self.price = 0
        self.stock = 0
    
    def __lt__(self, other):
        """
        Method to specify the order for sorting a product type
        """
        return self.id < other.id
    
    def __str__(self):
        return f"{self.id} {self.name}"