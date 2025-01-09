#Reverse String


def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):  # Start from the last character
        reversed_str += s[i]
    return reversed_str

def reverse_string_slicing(s):
    return s[::-1]

# Example usage
s = input("Please enter a string: ")
print("方法一Reversed string:", reverse_string(s))
print("方法二Reversed string:", reverse_string_slicing(s))


