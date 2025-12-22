'''
Reverse A String
'''

string = "hello_aryan"

# Method 1

reversed_str = ""

for char in string: 
    reversed_str = char + reversed_str

print(reversed_str)

# Method 2:

reversed_str = ""

reversed_str = string[::-1]

print(reversed_str)

# Method 3:
 
s = list(string)  # Convert to list

left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

s = ''.join(s)

print(s)



'''
Remove all extra characters in string and only keep alphabets in string
'''
my_str = "A man, a plan, a canal: Panama"
string = "".join([ch for ch in my_str if ch.isalpha()]).lower()
print(string)