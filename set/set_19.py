morning = {"Varad", "Shiva", "Pravin", "Sartaj"}
afternoon = {"Shiva", "Pravin", "Sartaj", "Karan"}

both = morning.intersection(afternoon)
only_morning = morning.difference(afternoon)
only_afternoon = afternoon.difference(morning)
at_least_one = morning.union(afternoon)

print("Both sessions:", both)
print("Only morning:", only_morning)
print("Only afternoon:", only_afternoon)
print("At least one session:", at_least_one)