dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"x": 2, "y": 3, "z": 4}

common_values = []
for value in dict1.values():
    if value in dict2.values():
        common_values.append(value)

print("Common values:", common_values)