class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        ### Brute: TC = O(n2) SC = O(1)
        
        # for i in range(n):
        #     isUnique = True
        #     for j in range(i+1, n):
        #         if s[i] == s[j]:
        #             isUnique = False
        #     if isUnique:
        #         return i
        
        ### Better : TC = O(n) SC = O(n + n)
        hashmap = {}
        duplicates = set()
        for i in range(n):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
            else:
                duplicates.add(s[i])

        for char in s:
            if char not in duplicates:
                return hashmap[char]
        
        return -1
        
        ### Optimal: TC = O(n) SC = O(n)
        n = len(s)
        hashmap = {}
        for i in range(n):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
            else:
                hashmap[s[i]] = -1

        print(hashmap)
        
        for char in s:
            if hashmap[char] != -1:
                return hashmap[char]
        
        return -1