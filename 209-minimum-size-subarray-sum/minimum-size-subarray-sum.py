class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = 0
        window_sum = 0 
        res = float('inf')

        while high < n:
            window_sum += nums[high]
            while window_sum >= target:
                length = high - low + 1
                res = min(res,length)
                window_sum -= nums[low]
                low +=1
            high +=1
        return 0 if res == float('inf') else res
                