class Solution(object):
    def twoSum(self, nums, target):
        dict={}

        for i,val in enumerate(nums):
            diff=target-val
            if diff in dict:
                return [dict[diff],i]
            dict[val]=i
            
s1 = Solution()
s1.twoSum([2,7,11,15],9)