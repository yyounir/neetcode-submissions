class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newNums = [] # Create a new empty string
        count = 1 # Create a variable count to help compare elements

        for i in nums:
            if i == nums[count]:
                count += 1
                if count == len(nums):
                    break
                continue
            else:
                newNums.append(i) # Add i to the new list
            if count == len(nums):
                newNums.append(nums[-1])
                break
        
        return nums


