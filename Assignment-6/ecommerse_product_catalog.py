# Base class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")
        print(f"Available: {'Yes' if self.is_available() else 'No'}")


# Electronics subclass inheriting form Product(baseclass)
class Electronics(Product):
    def __init__(self, name, price, stock, brand, warranty, specifications):
        super().__init__(name, price, stock) # Calling the parent class constructor
        self.brand = brand
        self.warranty = warranty  # e.g., "2 years"
        self.specifications = specifications  # dict or string

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Warranty: {self.warranty}")
        print("Specifications:")
        for spec, value in self.specifications.items():
            print(f"  - {spec}: {value}")


# Clothing subclass inheriting form Product(baseclass)
class Clothing(Product):
    def __init__(self, name, price, stock, brand, material, size):
        super().__init__(name, price, stock)
        self.brand = brand
        self.material = material
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Material: {self.material}")
        print(f"Size: {self.size}")




#####Driver ode

laptop = Electronics(
    name="Gaming Laptop",
    price=1500.00,
    stock=5,
    brand="Asus",
    warranty="2 years",
    specifications={
        "Processor": "Intel i7",
        "RAM": "16GB",
        "Storage": "1TB SSD",
        "GPU": "NVIDIA RTX 3060"
    }
)

tshirt = Clothing(
    name="Graphic T-Shirt",
    price=25,
    stock=20,
    brand="Puma",
    material="Cotton",
    size="L"
)


print("\n--- Electronics Item ---")
laptop.display_info()

print("\n--- Clothing Item ---")
tshirt.display_info()
