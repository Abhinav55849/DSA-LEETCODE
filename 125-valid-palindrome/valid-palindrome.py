class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_s = ""
        for char in s:
            if ("a"<= char <="z") or ("A"<= char <="Z") or ("0"<= char <="9"):
                clean_s += char.lower()
        
        return clean_s == clean_s[::-1]
            


