s1 = {'Math','Physics','Chemistry'}
s2 = {'Physics','Biology','Math'}

common_subjects = s1.intersection(s2)

only_s1 = s1.difference(s2)

only_s2 = s2.difference(s1)

total_unique_subjects = s1.union(s2)

print(f"1. Common subjects: {common_subjects}")
print(f"2. Subjects taken by only the first student: {only_s1}")
print(f"3. Subjects taken by only the second student: {only_s2}")
print(f"4. Total unique subjects : {total_unique_subjects}")
