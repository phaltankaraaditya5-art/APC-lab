dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "c": 6, "d": 7}

common_keys = []
for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Common keys:", common_keys)