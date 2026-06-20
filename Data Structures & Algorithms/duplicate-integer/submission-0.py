class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in range(0,len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
                return True
        return False

s1 = Solution()
print(s1.hasDuplicate([1,2,3,3]))  
