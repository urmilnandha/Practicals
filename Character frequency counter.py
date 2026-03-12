# Step 1: Get input from the user
user_input = input("Enter a string to analyze: ")

# Step 2: Initialize an empty dictionary
frequency_dict = {}

# Step 3: Loop through each character in the string
for char in user_input:
    # If the character is already in the dictionary, increment its count
    if char in frequency_dict:
        frequency_dict[char] += 1
    # If the character is new, add it to the dictionary with a count of 1
    else:
        frequency_dict[char] = 1

# Step 4: Display the results
print("\nCharacter Frequencies:")
for char, count in frequency_dict.items():
    print(f"'{char}': {count}")
