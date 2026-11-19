class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        low = 0
        high = k-1
        total = 0
        n = len(nums)
        res = float("-inf")
        for i in range(low,high+1):
            total += nums[i]

        while high < n:
            final = total/k
            res = max(res,final)
            low +=1
            high +=1
            if high == n:
                break
            total = total -nums[low-1]
            total = total +nums[high]
        return res
                



        