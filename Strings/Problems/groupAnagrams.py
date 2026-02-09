class Solution(object):
    def calculate_char(self, s):
        char_set = {}
        for i in range(len(s)):
            if s[i] in char_set:
                char_set[s[i]] += 1
            else:
                char_set[s[i]] = 1

        char_set_str = ""

        for key in sorted(char_set.keys()):
            char_set_str += "{}-{}".format(key, char_set[key])

        return char_set_str


    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    
        ## BRUTE:
        ## TC = O(n*nlogn) SC = O(n)
        # hashmap = {}
        # for s in strs:
        #     sorted_element = "".join(sorted(s))
        #     if sorted_element in hashmap:
        #         hashmap[sorted_element].append(s)
        #     else:
        #         hashmap[sorted_element] = [s]
        # ans = []
        # for value in hashmap.values():
        #     ans.append(value)       
        # return ans

        ## OPTIMAL
        ## TC = O(n*n) SC = O(n)
        hashmap = {}
        for s in strs:
            char_set = self.calculate_char(s)
            if char_set in hashmap:
                hashmap[char_set].append(s)
            else:
                hashmap[char_set] = [s]
        ans = []
        for value in hashmap.values():
            ans.append(value)
        return ans
