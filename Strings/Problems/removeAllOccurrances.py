# Given 2 strings s and pattern. Remove all occurances of pattern from the string s
# Eg: s = daabcbcabcbc , pattern = abc
# Iteration 1: daabcbcabcbc --> pattern found at index 2
#               |-> after removal, dabcabcbc 
# Iteration 2: dabcabcbc --> pattern found at index 1
#               |-> after removal, dabcbc
# Iteration 3: dabcbc --> pattern found at index 1
#               |-> after removal dbc
# return dbc

# TC = O(n*m) SC = O(1)
def removeAllOccurances(s:str, pattern:str) -> str:

    while len(s) > 0 and s.find(pattern) != -1:

        starting_position = s.find(pattern)
        len_pattern = len(pattern)

        s = s[:starting_position] + s[starting_position+len_pattern:]

    return s

print(removeAllOccurances("daabcbcabcbc","abc"))
