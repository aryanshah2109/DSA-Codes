# "the sky is blue" -> "blue is the sky"

# TC = O(nlogn) SC = O(n)
def approach1(s: str):
    s = s.strip()

    words = s.split(" ")
    words.reverse()
    rev = " ".join(words)    
    return rev


def reverse_str(s):
    rev = ""
    for char in s:
        rev = char + rev

    return rev

def approach2(s: str):
    
    s = s.strip()

    n = len(s)

    answer = ""

    # Reverse string
    s = reverse_str(s)

    # Reverse each word
    i = 0
    while i < n:

        word = ""

        while i<n and s[i] != " ":
            word += s[i]
            i += 1
        
        # reverse word
        
        word = reverse_str(word)

        if len(word) > 0:
            answer += " " + word
        
        i += 1


    return answer[1:]
    

print(approach1("the sky is blue"))
print(approach1("   hello world   "))

print(approach2("the sky is blue"))
print(approach2("   hello world   "))