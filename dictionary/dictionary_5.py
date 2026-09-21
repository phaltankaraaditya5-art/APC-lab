cities = {"Mumbai": 20000000, "Delhi": 19000000, "Pune": 6000000}
city = input("Enter city to remove: ")

if city in cities:
    del cities[city]

print(cities)