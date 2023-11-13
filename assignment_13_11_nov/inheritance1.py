# Inheritance :Inheriting properties from one class to
#another class
# 1 Inheritance
class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
    def display_product_details(self):
        print("Product : {}".format(self.name))
        print("pice : {}".format(self.price))
        print("Deal price : {}".format(self.deal_price))
        print("Ratings : {}".format(self.ratings))
class ElectronicItem(Product):
    def set_warrenty(self,warrenty_in_months):
        self.warrenty_in_months=warrenty_in_months
        print("warrenty_in_months : {}".format(self.warrenty_in_months))
className=ElectronicItem("Laptop",10000,8000,5)
className. display_product_details()
className.set_warrenty(24)

