class user:
    def __init__(self):
        self.users={}
        self.logged_in_user=None
    def register(self,name,password):
        if name in self.users:
            print("User already exists")
        else:
            self.users[name]=password
            print("Registration succesful")
    def login(self,name,password):
        if name in self.users and self.users[name]==password:
            self.logged_in_user=name
            print("login successful")
        else:
            print("Invalid Credentials")
    def logout(self):
        if self.logged_in_user:
            print("Bye")
            self.logged_in_user=None
        else:
            print("No user logged in")

class productManager:
    def __init__(self):
        self.products = {
            "laptop": 50000,
            "earpods": 2000,
            "Watch": 1500,
            "Accessories": 1000
        }
        self.cart = []

    def show_products(self):
        print("\nAvailable Products:")
        idx = 1
        for product, price in self.products.items():
            print(f"{idx} .{product} -₹ {price}")
            idx += 1

    def add_to_cart(self, index):
        try:
            product_list = list(self.products.items())
            product, price = product_list[index - 1]
            self.cart.append((product, price))
            print(f"{product} added to the cart for ₹ {price}")
        except IndexError:
            print("Invalid Product Selection")

    def view_cart(self):
        print("Your Cart")
        if not self.cart:
            print("Cart is empty")
        else:
            total = 0
            idx = 1
            for product, price in self.cart:
                print(f"{idx}.{product} = ₹{price} ")
                total += price
                idx += 1
            print(f"Total Amount: {total}")

    def checkout(self):
        print("Checkout")
        if self.cart:
            total = 0
            print("You are purchasing the following items:")
            for product, price in self.cart:
                print(f"{product} - ₹{price} ")
                total += price
            print(f"Total Amount: {total}")
            self.cart.clear()
            print("Checkout Complete. Thank you!")
        else:
            print("Your Cart is Empty")

    def delete_products(self, index):
        try:
            product_name = list(self.products.keys())[index - 1]
            self.products.pop(product_name)
            print(f"{product_name} has been deleted from the product list")
        except IndexError:
            print("Invalid Product Index")

class StoreApp:
    def __init__(self):#fixed constructor
        self.user_system=user()
        self.product_manager=productManager()

    def user_menu(self):
        while self.user_system.logged_in_user:
            print("\n 1) View Products \n 2) View Cart \n 3) Checkout \n 4) Delete product \n 5)exit ")
            choice = input("Select an option")

            if choice=='1':
                self.product_manager.show_products()
                try:
                    index=int(input("Enter Product Number to add"))
                    self.product_manager.add_to_cart(index)
                except:
                    print("Invalid selection")

            elif choice=='2':
                self.product_manager.view_cart()

            elif choice=='3':
                self.product_manager.checkout()
            elif choice=='4':
                self.product_manager.show_products()
                index=int(input("enter Product number to delete"))
                self.product_manager.delete_products(index)
            elif choice=='5':
                self.user_system.logout()
            else:
                print("Invalid code")

    def menu(self):
        while True:
            print("\n Enter Your choice: \n 1)Register 2) Login 3) Logout")
            choice=input("choice")

            if choice=='1':
                name=input("Enter Your name")
                password=input("Enter your Password")
                self.user_system.register(name, password)
            elif choice=='2':
                name=input("Enter your name")
                password=input("Enter your password")
                self.user_system.login(name, password)

                if self.user_system.logged_in_user:
                    self.user_menu()
            elif choice=='3':
                self.user_system.logout()
            else:
                print("Invalid code")

store=StoreApp()
store.menu()
