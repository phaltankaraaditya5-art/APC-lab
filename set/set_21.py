employee1_skills = {"Python", "SQL", "Java"}
employee2_skills = {"Python", "C++", "AWS"}

common_skills = employee1_skills.intersection(employee2_skills)
unique_emp1 = employee1_skills.difference(employee2_skills)
unique_emp2 = employee2_skills.difference(employee1_skills)
all_skills = employee1_skills.union(employee2_skills)

print("Common skills:", common_skills)
print("Unique to Employee 1:", unique_emp1)
print("Unique to Employee 2:", unique_emp2)
print("All skills:", all_skills)