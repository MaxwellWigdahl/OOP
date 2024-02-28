class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.__descriptiption = description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def get_description(self):
        return self.__descriptiption
    
    def get_units_in_inventory(self):
        return self.__units_in_inventory
    
    def get_price(self):
        return self.__price
