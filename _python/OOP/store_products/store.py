#Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.

#Let's also give some methods to our Store class:

#add_product(self, new_product) - takes a product and adds it to the store
#sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
#inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
#set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)

class Store:
    def __init__(self, name):
        self.name = name
        self.product = []

    def add_product(self, new_product):
        self.product.append(new_product)
        return self

    def sell_product(self, id):
        print(f"Remove the product {self.product[id]} from products list")
        self.product.pop(id)
        return self
    def inflation(self, percent_increase):
        for i in self.product:
            i.update_price(percent_increase,True)
        return self

    def set_clearance(self, category, percent_discount):
    
        print(f"Clearance for {category}")
        for i in self.product:
            i.update_price(percent_discount,False)
        return self
        
        

#Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
#Let's give some methods to our Product class:
#update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
#print_info(self) - print the name of the product, its category, and its price.
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price*percent_change
        if is_increased == False:
            self.price -= self.price*percent_change
        return self

    def print_info(self):
        #print(f"Category {self.category} : The price of {self.name} is {self.price}")
        print(f"The price of {self.name} is {self.price}")


#Create a Store class with 2 attributes
#Create a Product class with 3 attributes
#Add the print_info method to the Product class
#Add the update_price method to the Product class
#Add the add_product method to the Store class
#Add the sell_product method to the Store class
#Test out your classes by creating an instance of the Store and a few instances of the Product class, add those instances to the store instance, and then test out the methods.


apple = Product(name="apple", price=5, category="fruit")
pear = Product("pear", 6, category="fruit")
banana = Product("banana", 10, category="fruit")
#print(apple.__dict__)

shop = Store("EasyBuy")


shop.add_product(apple).add_product(pear).add_product(banana)
for i in shop.product:
    i.print_info()
#print(shop.__dict__)
shop.set_clearance("fruit", 0.5)
for i in shop.product:
    i.print_info()
shop.inflation(0.02)


#set clearance







#apple.print_info()
#apple.update_price(0.15,is_increased=False)
#apple.print_info()















