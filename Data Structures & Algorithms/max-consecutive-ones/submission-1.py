class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        temp = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                temp = max(temp, count)
                count = 0
        
        return max(temp, count)