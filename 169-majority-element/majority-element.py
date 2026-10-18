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
        best = None
        best_count = 0
        for num in freq:
            if freq[num] > best_count:
                best_count = freq[num]
                best = num
        return best