class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        p1 = 0
        unique = 1
        p2 = 0
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                p2 +=1
                continue
            else:
                nums[p1+1] = nums[p2]
                p1 +=1
                unique += 1
                p2 +=1
        return unique



            
        