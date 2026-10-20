'''
UNDERSTAND:
- Inputs a list int
- Outputs a list int
- Core logic:
    - Multiply by everything except the current element and add it to the array
    - You get 48 by multiplying all elements except the first element
    - Using brute force, such as manually multiplying all elements would exceed time limit

PLAN:
- Create function
- Set prefix = 1
- Set result = [1] * len(nums)
    - That way we can easily map out the elements defined by its length
- Use a for loop to iterate thorugh nums
    - Set result[i] = prefix // by default the first number when for loop starts is always 1
    - Set prefix *= nums[i]

- Set postfix = 1
- Use a for loop to iterate through nums, backwards! (len(nums) - 1, -1, -1):
    - result[i] *= postfix
    - postfix *= nums[i]
- Return result

IMPLEMENT:
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
          result[i] = prefix
          prefix *= nums[i]
        
        # print(result)
        
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
          result[i] *= postfix
          postfix *= nums[i]

        return result