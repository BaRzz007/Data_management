import os
from product import Product
from db import Db

def binary_search(arr, target_id):
    """
    This function implements the binary search algorithm and 
    returns the index of the target id or -1 if the id is not in the list
    """
    print("Searching for {} using binary search algorithm".format(target_id))

    start = 0;
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        print("Comparing {} with {}".format(target_id, arr[mid].id))

        if arr[mid].id == target_id:
            #print(f"Found {target_id} at index: {mid}")
            return mid
        elif arr[mid].id < target_id:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

def sequential_search(arr, target_id):
    """
    Simulating a sequential search for a target id
    """
    print("Searching for {} using sequential search".format(target_id))
    idx = 0
    for item in arr:
        print(f"Comparing {item.id} with {target_id}")
        if item.id == target_id:
            #print(f"Found {target_id} at index: {idx}")
            return idx;
        idx += 1
    return -1




def main():
    """
    entry point to the program
    """
    d_base = Db()

    d_base.connect()
    product_query = d_base.execute("SELECT * FROM products") # returns a list of tuples
    products = [Product(product[0], product[1], product[4]) for product in product_query]

    sequential_search(products, "da4986e1-3181-4091-ae5f-69b7a0bc5247-kitchenware")

    print() # newline to space the outputs

    products.sort()
    binary_search(products, "da4986e1-3181-4091-ae5f-69b7a0bc5247-kitchenware")

    d_base.close()


if __name__ == "__main__":
    main()
