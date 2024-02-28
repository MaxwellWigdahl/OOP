import InsectClass as ic

mosquito = ic.Insect(2,4, 'Mosquito')
housefly = ic.Insect(2,4, 'Housefly')

mosquito.calc_flight()
housefly.calc_flight()


print(f"The {mosquito.get_name()} flies {mosquito.get_miles()} miles.")
print(f"The {housefly.get_name()} flies {housefly.get_miles()} miles.")
