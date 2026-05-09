class Solution(object):
    def reverseString(self, string):
        rev = ""
        for char in string:
            rev = char + rev

        return rev


    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string_list = [char for char in s if char.isalnum()]
        string = "".join(string_list)
        string = string.lower()

        ## Brute
        ## TC = O(n) SC = O(n)
        # reverse = self.reverseString(string)
        # return reverse == string

        ## Optimal
        ## TC = O(n) SC = O(1)
        left = 0
        right = len(string) - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True