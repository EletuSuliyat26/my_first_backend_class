# Define the data
phones = [
    {"brand": "Apple", "price": 200000},
    {"brand": "Samsung", "price": 198000},
    {"brand": "Google", "price": 150000}
]

laptops = [
    {"brand": "Dell", "price": 380000},
    {"brand": "HP", "price": 400000},
    {"brand": "Apple", "price": 500000}
]

products = {
    "phone": phones,
    "laptop": laptops
}

# Define functions
def get_product_details(product):
    return f"Brand: {product['brand']}, Price: ${product['price']}"

def inquire_product(category, brand, products):
    if category in products:
        for product in products[category]:
            if product["brand"].lower() == brand.lower():
                return product
    return None

def handle_purchase(product):
    print(get_product_details(product))
    purchase = input("Do you want to purchase this product? (yes/no): ")
    if purchase.lower() == "yes":
        return f"Thank you for your purchase. Your checkout price is ${product['price']}."
    else:
        return "Thank you for your inquiry."

def start_service():
    print("Welcome to Carlcare Services!")
    category = input("What would you like to inquire about? (phone/laptop): ").lower()
    
    if category in products:
        brand = input(f"Which brand of {category} are you interested in?: ")
        product = inquire_product(category, brand, products)
        
        if product:
            result = handle_purchase(product)
            print(result)
        else:
            print(f"Sorry, we do not have any {brand} {category}s available.")
    else:
        print(f"Sorry, we do not have any {category}s available.")

# Execute the service
start_service()
