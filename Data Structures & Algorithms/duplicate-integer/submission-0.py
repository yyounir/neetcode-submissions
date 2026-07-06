class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in range(len(nums)):
            if(nums[i] in count):
                count.update({nums[i] : count.get(nums[i]) + 1 })
            else:
                count.update({nums[i] : 1 })
        
        for num in count:
            if(num > 1):
                return True
            else:
                return False