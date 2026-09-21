day1_visitors = {"V1", "V2", "V3", "V4"}
day2_visitors = {"V3", "V4", "V5", "V6"}

unique_visitors = day1_visitors.union(day2_visitors)
returning_visitors = day1_visitors.intersection(day2_visitors)
only_day1 = day1_visitors.difference(day2_visitors)
only_day2 = day2_visitors.difference(day1_visitors)

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Only day 1:", only_day1)
print("Only day 2:", only_day2)