def to_upper(text):
    result = ""
    for char in text:
        # Check if character is lowercase (between 'a' and 'z')
        if 'a' <= char <= 'z':
            # Subtract 32 from ASCII value to get uppercase
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def to_lower(text):
    result = ""
    for char in text:
        # Check if character is uppercase (between 'A' and 'Z')
        if 'A' <= char <= 'Z':
            # Add 32 to ASCII value to get lowercase
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_toggle(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

# --- Main Program ---
user_input = input("Enter a string: ")

print(f"Original: {user_input}")
print(f"Uppercase: {to_upper(user_input)}")
print(f"Lowercase: {to_lower(user_input)}")
print(f"Toggle Case: {to_toggle(user_input)}")
