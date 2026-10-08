class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        result = 0
        for char in s:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1
        has_odd = False
        for count in freq.values():
            if count % 2 == 0:
                result += count
            else:
                result +=count -1
                has_odd=True

        if has_odd:
            result +=1

        return result
                

        
            
        