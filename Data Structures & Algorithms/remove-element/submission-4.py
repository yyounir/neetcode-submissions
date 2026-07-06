class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [1, 2, 3, 4, 2, 1, 1]
        numsLength = len(nums)
        count = 0

        # for element in nums:
        #     if element == val: 
        #         nums.remove(element)
        #         count += 1
        #         continue
        #     else: continue

        for i in range(numsLength - 1):
            if nums[i] == val:
                del nums[i]
                count += 1
                continue
            else:
                continue

        return numsLength - count