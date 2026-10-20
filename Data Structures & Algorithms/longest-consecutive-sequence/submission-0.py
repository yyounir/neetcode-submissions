'''
UNDERSTAND:
- Inputs an int array
- Outputs an int
- Core logic:
    - We need to see how long the numbers go consecutively
- Clarifications
    - len(nums) could be 0 or 1

PLAN:
- Create function and validate
- Convert nums to set
- Set longest = 1
- For each num in set
    - If num - 1 not in set
        - Start counting
    - Else
        - Continue
- Return longest

IMPLEMENT:
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        if(len(nums) == 1):
            return 1

        nums = set(nums)
        
        longest = 1
        count = 1

        for num in nums:
            if(num - 1 not in nums):
                while(num + 1 in nums):
                    count += 1
                    num += 1
                    if(count > longest):
                        longest = count
            count = 1
        
        return longest