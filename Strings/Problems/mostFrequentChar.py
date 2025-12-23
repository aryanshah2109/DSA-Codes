# Find out the character with highest frequency

# TC = O(n2) SC = O(1)
def approach1(s):
    n = len(s)
    maxCount = 0
    count = 0
    maxCountChar = ""

    for i in range(n):
        count = 1

        for j in range(i+1,n):
            if s[i] == s[j]:
                count += 1

        if count > maxCount:
            maxCount = count
            maxCountChar = s[i]

    return maxCountChar


# TC = O(n + k), SC = O(k) for k unique characters in string
def approach2(s):
    n = len(s)

    hashmap = {}

    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
        
    maxCount = 1
    maxCountChar = ""
    for key in hashmap.keys():
        if maxCount < hashmap[key]:
            maxCount = hashmap[key]
            maxCountChar = key
    return maxCountChar


s = input("Enter string: ")


print(approach1(s))
print(approach2(s))