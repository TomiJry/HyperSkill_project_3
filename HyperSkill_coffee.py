class CoffeeMachine:
    def __init__(self):
        # Kezdeti állapotok és erőforrások
        self.state = "main_menu"
        self.resources = {
            "water": 400,
            "milk": 540,
            "coffee_beans": 120,
            "cups": 9,
            "money": 550
        }
        self.coffee_types = {
            "1": {"name": "espresso", "water": 250, "milk": 0, "coffee_beans": 16, "cost": 4},
            "2": {"name": "latte", "water": 350, "milk": 75, "coffee_beans": 20, "cost": 7},
            "3": {"name": "cappuccino", "water": 200, "milk": 100, "coffee_beans": 12, "cost": 6}
        }
        self.fill_steps = ["water", "milk", "coffee_beans", "cups"]
        self.fill_index = 0

    def handle_input(self, user_input):
        if self.state == "main_menu":
            self.main_menu(user_input)
        elif self.state == "buy":
            self.buy_menu(user_input)
        elif self.state == "fill":
            self.fill_menu(user_input)

    def main_menu(self, user_input):
        if user_input == "buy":
            self.state = "buy"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif user_input == "fill":
            self.state = "fill"
            self.fill_index = 0
            print(f"Write how many ml of {self.fill_steps[self.fill_index]} you want to add:")
        elif user_input == "take":
            print(f"I gave you ${self.resources['money']}")
            self.resources["money"] = 0
        elif user_input == "remaining":
            self.print_state()
        elif user_input == "exit":
            exit()

    def buy_menu(self, user_input):
        if user_input == "back":
            self.state = "main_menu"
        elif user_input in self.coffee_types:
            coffee = self.coffee_types[user_input]
            if self.check_resources(coffee):
                self.make_coffee(coffee)
            self.state = "main_menu"

    def fill_menu(self, user_input):
        try:
            amount = int(user_input)
            resource = self.fill_steps[self.fill_index]
            self.resources[resource] += amount
            self.fill_index += 1
            if self.fill_index < len(self.fill_steps):
                print(f"Write how many ml of {self.fill_steps[self.fill_index]} you want to add:")
            else:
                self.state = "main_menu"
        except ValueError:
            print("Please enter a valid number.")

    def check_resources(self, coffee):
        for resource, amount in coffee.items():
            if resource in self.resources and self.resources[resource] < amount:
                print(f"Sorry, not enough {resource}!")
                return False
        return True

    def make_coffee(self, coffee):
        self.resources["water"] -= coffee["water"]
        self.resources["milk"] -= coffee["milk"]
        self.resources["coffee_beans"] -= coffee["coffee_beans"]
        self.resources["cups"] -= 1
        self.resources["money"] += coffee["cost"]
        print("I have enough resources, making you a coffee!")

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.resources['water']} ml of water")
        print(f"{self.resources['milk']} ml of milk")
        print(f"{self.resources['coffee_beans']} g of coffee beans")
        print(f"{self.resources['cups']} disposable cups")
        print(f"${self.resources['money']} of money")

# Program futtatása
machine = CoffeeMachine()

while True:
    if machine.state == "main_menu":
        print("Write action (buy, fill, take, remaining, exit):")
    user_input = input().strip()
    machine.handle_input(user_input)
