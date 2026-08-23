'''
1. Understand:
- Inputs a list of strings
- Outputs an array, mainly 2D arrays
- Core logic:
    - Group all anagrams together, with each sublist having anagrams
    - Each of the arrays have their own letters
- Possible edge cases:
    - Empty array should return empty string as 2D array
    - Array with 1 element should return that element in the 2D array

2. Plan
- Create a function 
- Create an empty array called count
- Handle edge cases
- Create an empty dictionary (dict)
- Use a for loop to iterate through the array of strs
    - To sort a string, you use "".join(sorted( <word> )), check to see if <word> sorted like that is in the dictionary
        - Update dictionary (key: "".join(sorted( <word> )) : values: "".join(sorted( <word> )) + [word])
        - Make it so that the key, which is the already sorted word, has their value added to the list 
        - Else: Update the dictionary with the value of [word]
- Return list(dict.values())

3. Implement
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if(not strs):
        #     # If there are no words in the list
        #     return [[""]]
        # if(len(strs) == 1):
        #     # If there is only one word in the list
        #     return [strs[0]]

        dict = {}
        # "".join(sorted(word))

        for word in strs:
            if("".join(sorted(word)) in dict):
                dict.update({"".join(sorted(word)) : dict.get("".join(sorted(word))) + [word]})
            else:
                dict.update({"".join(sorted(word)) : [word]})
        
        return list(dict.values())

        
         