# Check if a strings is a palindrome or not
# a string is palindrome if they are same from left to right and right to left
# eg: abcba is a valid palindrome as reverse of abcba is same as input string abcba
# The string contain non-alphanumerical characters like _, space, special symbols, etc.
# So remove those non-alphanumerical characters and then handle palindrome nature

def checkPalindrome(input_string):

    alpha_string = "".join([char for char in input_string if char.isalnum()]).lower()

    reversed_string = ""

    for char in alpha_string:
        reversed_string = char + reversed_string

    return reversed_string == alpha_string
        
    
input_string = input("Enter string: ")

if checkPalindrome(input_string):
    print(f"Given string is a Valid Palindrome")

else:
    print(f"Given string is not a Valid Palindrome")