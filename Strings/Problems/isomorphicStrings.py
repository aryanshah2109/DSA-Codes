# Given 2 strings, Return True if they are isomorphic. Else return False
# Isomorphic strings are those who have same unique character mappings
# Eg: "egg" and "add" . O/P = True. Here e->a, g->d
# Eg: "egg" and "adh". O/P = False. Here e->a, g->d and g-> h but g cannot have 2 mappings

import numpy as np

# TC = O(n2) SC = O(2n)
def approach1(s:str, t:str):
    mappings = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        current_values = [value for key, value in mappings.items()]

        if s[i] not in mappings:
            if t[i] in current_values:
                return False
            mappings.update({s[i]:t[i]})

        elif mappings[s[i]] != t[i] :
            return False          

    return True

# TC = O(n) SC = O(2*128) -> O(1)
def approach2(s:str, t:str):

    map_s = np.zeros(128)
    map_t = np.zeros(128)

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        ascii_s = ord(s[i])
        ascii_t = ord(t[i])

        if map_s[ascii_s] != map_t[ascii_t]:
            return False

        map_s[ascii_s] = i+1
        map_t[ascii_t] = i+1

    return True

print(approach1("egg","add"))
print(approach2("egg","add"))

print(approach1("egg","adh"))
print(approach2("egg","adh"))