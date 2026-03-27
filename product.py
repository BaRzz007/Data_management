from uuid import uuid4

class Product():
    """
    Product class
    """

    def __init__(self, id="", product_name="", category=""):
        """
        Initializes a new product
        """
        # if id is not provided, generates a new id for the item
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
        """
        defines the string representation of the class
        """
        return f"{self.id} {self.name}"