user_key = input("Enter a key (or press Enter to keep it empty): ")
user_value = input("Enter a value: ")

my_dict = {}

if user_key:
    my_dict[user_key] = user_value

if not my_dict:
    print("\nThe dictionary is empty!")
else:
    print(f"\nThe dictionary is NOT empty! Current content: {my_dict}")

