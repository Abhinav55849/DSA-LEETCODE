class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        low = 0
        high = k-1
        total = 0
        n = len(nums)
        res = float("-inf")
        for i in range(low,high+1):
            total += nums[i]

        while high < n:
            res = max(res,total/float(k))
            low +=1
            high +=1
            if high == n:
                break
            total = total -nums[low-1]
            total = total +nums[high]
        return res
                



        