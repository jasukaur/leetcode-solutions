class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arr = []

        i = 0

        while i<len(nums):
            start = nums[i]
            while i+1 <len(nums) and nums[i]+1 == nums[i+1]:
                i+=1
            
            if start != nums[i]:
                arr.append(str(start) + "->" + str(nums[i]))
            else:
                arr.append(str(nums[i]))
            
            i+=1

            
        return arr