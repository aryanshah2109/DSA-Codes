# Given 2 strings, Return True if they are isomorphic. Else return False
# Isomorphic strings are those who have same unique character mappings
# Eg: "egg" and "add" . O/P = True. Here e->a, g->d
# Eg: "egg" and "adh". O/P = False. Here e->a, g->d and g-> h but g cannot have 2 mappings


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