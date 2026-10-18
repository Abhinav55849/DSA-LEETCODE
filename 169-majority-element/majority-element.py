class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for char in nums:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1
        return max(freq,key =freq.get)