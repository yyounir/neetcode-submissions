class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        count = 0

        for i in nums:
            if i == nums[count]:
                nums.pop(nums[count])
                count += 1
                if count == len(nums):
                    break
                continue
            else:
                count += 1
                if count == len(nums):
                    break
                continue