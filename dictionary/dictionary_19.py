data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
result = {}
seen_values = []

for key, value in data.items():
    if value not in seen_values:
        result[key] = value
        seen_values.append(value)

print(result)