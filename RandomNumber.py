import random


odd = [random.randrange(1, 100, 2) for _ in range(5)]
print(f"Stage 1: Initial list of odd integers -> {odd}")


even = [random.randrange(2, 100, 2) for _ in range(4)]
print(f"Stage 2: List of even integers to insert -> {even}")


odd[2] = even
print(f"Stage 3: After replacing the 3rd element -> {odd}")

#Flatten the list

flattened = []
for item in odd:
    if isinstance(item, list):
       
        flattened.extend(item)
    else:
       
        flattened.append(item)
print(f"Stage 4: Flattened list -> {flattened}")


flattened.sort()
print(f"Stage 5: Final sorted list -> {flattened}")
