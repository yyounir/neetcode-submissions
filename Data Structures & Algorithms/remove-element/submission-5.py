class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [1, 1, 2, 3, 4]
        temp = []

        for num in nums:
            if num == val: continue
            temp.append(num)
        
        for i in range(len(temp)):
            nums[i] = temp[i]

        

        return len(temp)