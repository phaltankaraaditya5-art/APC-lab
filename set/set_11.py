set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

only_first = set1.difference(set2)
only_second = set2.difference(set1)

print("In first but not second:", only_first)
print("In second but not first:", only_second)