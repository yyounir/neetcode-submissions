'''
Understand:
- Inputs an array of nums and an integer k
- Outputs an array
- Core logic:
    - The function would find the given k most frequent elements
    - In Example 1, k is 2, so we need to find 2 most frequent elements
    - 1 and 2 from the array example are the most frequent because there are more 1's and 2's than any other element
- Possible edge cases:
    - Based on the constraints, it states that there garunteed to be a frequent number, so there shouldnt be an empty array or a mismatch in the amount of elements
    - If there is only 1 element, return that element since its the only frequent one
    - If all the array values are distinct, such as each element being found only once, return that array only if the size is equal to k

Match:
- I would need to store elements in a dictionary to keep track of the frequency of the elements being read
- Using the values() would help me handle the edge case when the numbers are distinct and to see the max of the elements
- May not be the most efficient because it may require me to use multiple for loops

Plan:
- Create a function named Solution
- Handle edge cases where there is only one element in the array
    - Return that one element
- Create an empty dictionary where you would keep track of the frequency of the elements
- Create a for loop to iterate through the array
    - If the element is in the array
        - Update({key, element : value, increment})
        - Else Update({key, element : value, 1})
- Sort the dictionary using dict(sorted(dict.items(), key = lambda item: item[1]))
- Iterate the array k times, so the that the first k elements are appended to the array you want to return
- Return the array

Implement:
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 
        if(len(nums) == 1):
            return [nums[0]]
        
        new_dict = {}
        lst = []

        for num in nums:
            if(num in new_dict):
                new_dict.update({num : new_dict.get(num) + 1})
            else:
                new_dict.update({num : 1})

        new_dict = dict(sorted(new_dict.items(), key = lambda item: item[1], reverse=True))
        newList = list(new_dict.keys())

        for i in range(k):
            lst.append(newList[i])
        
        return lst
        