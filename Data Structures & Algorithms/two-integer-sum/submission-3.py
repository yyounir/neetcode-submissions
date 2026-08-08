'''
1. Understand
- Inputs a list of ints, and an int target
- Outputs a list of ints
- This function finds two suitable numbers that adds towards the target value and captures the index of those values
- Use two pointers to make sure every different combination of numbers is scanned
- Possible edge cases:
    - 1 value in list

2. Plan (Approach 1)
- Create a variable named pointer1, pointing to the first element of the list = 0
- Create a variable named pointer2, pointing to the second element of the list = 0
- Use a while loop until nums[pointer1] == nums[-2]
    - When starting with pointer1 at the first element, check to see if pointer1 + pointer2 == target:
        - Return [ pointer1 , pointer2 ]
        - Else: pointer2++
    - If nums[pointer2] == nums[-1]:
        - pointer1++
        - pointer2 = pointer1 + 1
- Return "[-1 , -1] (wrong output)"

3. Implement
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = 1

        while not pointer1 == len(nums):
            if(nums[pointer1] + nums[pointer2] == target):
                return [pointer1 , pointer2]
            else:
                pointer2 += 1
            if(pointer2 == len(nums)):
                pointer1 += 1
                pointer2 = pointer1 + 1
        return [-1]


        