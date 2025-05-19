class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 200
        self.past_orders = []

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_balance(self, amount):
        self.balance += amount
        print(f"{amount} added. Current balance: {self.balance}")

    def view_balance(self):
        print(f"Your balance is {self.balance}")

    def place_order(self, restaurant, item_name, quantity):
        for menu_item in restaurant.menu.items:
            if item_name.lower() == menu_item.lower():
                price = restaurant.menu.get_price(menu_item)
                total = price * quantity
                if self.balance < total:
                    print("Insufficient balance.")
                    return
                
                order = Order(menu_item, quantity, total)
                self.past_orders.append(order)
                print(f"Order placed: {order}")
                self.balance -= total
                print(f"Remaining balance: {self.balance}")
                return
        print("Item not found.")


    def view_past_orders(self):
        if not self.past_orders:
            print("No past orders.")
        else:
            print("--- Past Orders ---")
            for order in self.past_orders:
                print(order)


class Admin:
    def __init__(self, name):
        self.name = name

    def create_customer_account(self, restaurant, name, email, address):
        customer = Customer(name, email, address)
        restaurant.customers.append(customer)
        print("Customer account created.")

    def remove_customer_account(self, restaurant, name):
        for c in restaurant.customers:
            if c.name == name:
                restaurant.customers.remove(c)
                print("Customer removed.")
                return
        print("Customer not found.")

    def view_customers(self, restaurant):
        if not restaurant.customers:
            print("No customers found.")
        else:
            print("--- Customers ---")
            for c in restaurant.customers:
                print(f"{c.name} - {c.email} - {c.address}")

    def add_item(self, restaurant, name, price):
        restaurant.menu.add_item(name, price)
        print(f"{name} added to menu.")

    def remove_item(self, restaurant, name):
        restaurant.menu.remove_item(name)
        print(f"{name} removed from menu.")


class Menu:
    def __init__(self):
        self.items = {}
        self.add_item('Pizza', 250)
        self.add_item('Burger', 150)
        self.add_item('Dessert', 100)
        self.add_item('Choco', 50)

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def get_price(self, name):
        return self.items.get(name)

    def show_menu(self):
        print('Name\tPrice')
        for name, price in self.items.items():
            print(f'{name}\t{price} tk')


class Order:
    def __init__(self, item, quantity, total_price):
        self.item = item
        self.quantity = quantity
        self.total_price = total_price

    def __repr__(self):
        return f"{self.item} x {self.quantity} = {self.total_price}"


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.customers = []


res = Restaurant("Yummy")


def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    customer = Customer(name, email, address)
    res.customers.append(customer)

    while True:
        print("--- Customer Menu ---")
        print("1. View Menu")
        print("2. Add Balance")
        print("3. View Balance")
        print("4. Place Order")
        print("5. View Past Orders")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            customer.view_menu(res)
        elif choice == '2':
            amt = int(input("Enter amount: "))
            customer.add_balance(amt)
        elif choice == '3':
            customer.view_balance()
        elif choice == '4':
            item = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            customer.place_order(res, item, qty)
        elif choice == '5':
            customer.view_past_orders()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")


def admin_menu():
    name = input("Enter admin name: ")
    admin = Admin(name)

    while True:
        print("--- Admin Menu ---")
        print("1. Create Customer")
        print("2. Remove Customer")
        print("3. View Customers")
        print("4. Add Menu Item")
        print("5. Remove Menu Item")
        print("6. View Menu")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            cname = input("Customer name: ")
            email = input("Email: ")
            address = input("Address: ")
            admin.create_customer_account(res, cname, email, address)
        elif choice == '2':
            cname = input("Enter customer name to remove: ")
            admin.remove_customer_account(res, cname)
        elif choice == '3':
            admin.view_customers(res)
        elif choice == '4':
            iname = input("Item name: ")
            price = int(input("Item price: "))
            admin.add_item(res, iname, price)
        elif choice == '5':
            iname = input("Item to remove: ")
            admin.remove_item(res, iname)
        elif choice == '6':
            res.menu.show_menu()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")


while True:
    print(f"~~~ Welcome to {res.name} Restaurant ~~~")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    option = input("Enter choice: ")

    if option == '1':
        customer_menu()
    elif option == '2':
        admin_menu()
    elif option == '3':
        print("Thank you!!!")
        break
    else:
        print("Invalid input.")
