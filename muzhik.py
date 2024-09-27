from random import randint

REAL_ESTATE_TYPES = ["house", "flat", "dacha"]
VEHICLE_TYPES = ["car", "motorbike", "bicycle", "scooter"]

class Person:
    user_id = 1
    def __init__(self):
        self.prop = []
        self.user_id = Person.user_id
        Person.user_id += 1
        self.bank_account = BankAccount(self.user_id)
    
    def work(self):
        salary = randint(5, 10)
        self.bank_account.put_money(salary)

    def buy_prop(self, prop_obj):
        # проверить счет
        if self.bank_account.get_balance() < prop_obj.buy_price:
            print('Not enough money')
            return
        
        if isinstance(prop_obj, House) and (not any(list(map(lambda obj: isinstance(obj, Car), self.prop)))):
            print("You have to have a car befor buying a house")
            return

        # списать деньги
        self.bank_account.take_money(prop_obj.buy_price)
        # положить объект в имещуство
        self.prop.append(prop_obj)
    
    def sell_prop(self, idx):
        self.bank_account.put_money(self.prop[idx].sell_price)
        self.prop.pop(idx)


class BankAccount:
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0

    def get_balance(self):
        return self.balance
    
    def put_money(self, amount):
        self.balance += amount

    def take_money(self, amount):
        self.balance -= amount


# property
class RealEstate:
    def __init__(self, type, name, buy_price=100, sell_price=90):
        if not (type in REAL_ESTATE_TYPES):
            raise ValueError(f"Real Estate type must be in {REAL_ESTATE_TYPES}")
        self.type = type
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price

        RealEstateRegistry.set_real_estate_item(self.name)
    
    def __str__(self):
        return f"{self.type}: {self.name}"

class Vehicle:
    def __init__(self, type, name, buy_price=30, sell_price=15):
            if not (type in VEHICLE_TYPES):
                raise ValueError(f"Vehicle type must be in {VEHICLE_TYPES}")
    ...


class RealEstateRegistry:
    __real_estate_list = set()
    
    @classmethod
    def set_real_estate_item(cls, item_name):
        if item_name in cls.__real_estate_list:
            raise ValueError(f"{item_name} is already registered")
        cls.__real_estate_list.add(item_name)        
    
    
class Car:
    buy_price = 50
    sell_price = 30

class House:
    buy_price = 100
    sell_price = 90
    

def test():
    flat = RealEstate("flat", "Lenina-53-28")
    print(flat)
    
if __name__ == "__main__":
    test()