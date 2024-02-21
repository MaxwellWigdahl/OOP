import InsectClass as ic

mosquito = ic.Insect()
housefly = ic.Insect()

mosquito.calc_flight()
housefly.calc_flight()


print('This is the number of miles that the mosquito can fly:', mosquito.get_miles())
print('This is the number of miles that the housefly can fly:', housefly.get_miles())
