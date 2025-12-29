rev = ""

def reverseStr(str, idx):
    global rev
    rev = rev + str[idx]
    if idx == 0:
        return
    reverseStr(str, idx-1)


def palindrome(str):
    global rev

    temp = str
    reverseStr(str, len(str)-1)
    
    return temp == rev

print(palindrome("abba"))
print(palindrome("abbc"))