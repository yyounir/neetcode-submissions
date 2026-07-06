class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [1, 2, 3, 4, 2, 1, 1]

        for element in nums:
            if element == val: nums.remove(element)
            else: continue
        return nums