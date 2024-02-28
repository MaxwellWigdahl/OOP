import CellPhoneClass as cpc

phone = cpc.CellPhone('Apple', 'iPhone 15', 1099)
phone.set_retail_price(999)

print("Manufactured by: ", phone.get_manufact())
print("The current model is: ", phone.get_model())
print("The retail price of the phone is: ", phone.get_retail_price())