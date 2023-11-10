class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}

        for i in range(len(nums)):
            lookup = target-nums[i]
            if lookup in hm:
                return [hm[lookup], i]
            hm[nums[i]] = i
        
        