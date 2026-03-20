from uuid import uuid4

def binary_search(product_list, target_id):
    start = 0;
    end = len(product_list) - 1

    while start <= end:
        print("Searching for {} in {}".format(target_id, product_list))
        mid = (start + end) // 2

        if product_list[mid].id == target_id:
            print(product_list[mid])
            return mid
        elif product_list[mid].id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


class Product():
    """
    Product class
    """

    def __init__(self, product_name, category):
        self.id = str(uuid4())
        self.name = product_name
        self.category = category
        self.price = 0
        self.stock = 0

def main():
    all_products = {
        "furniture": ["Sofa Couch", "Office Workstation", "Shelf Unit", "Bed Frame", "Dinning Table"],
        "home textile": ["Bed Sheets & Set", "Bath Towel", "Cushion Cover", "Area Rug", "Kitchen Linen"],
        "kitchenware": ["Chef's Knife", "Cutting Board", "Grater", "Mixing Bowl", "Spatula"],
        "decor": ["Cactus Plant", "Throw Pillow", "Decorative Bedroom Mirrow", "Ceramic Vase", "Glass Vase"]
    }

    product_list = [Product(product, category) for category, products in all_products.items() for product in products]
    for product in product_list:
        print(product.id, product.name)

if __name__ == "__main__":
    main()
