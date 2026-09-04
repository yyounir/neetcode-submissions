'''
Understand:
- 2 Functions
    - First function inputs a list of strings
    - First function outputs a string
    - Second function inputs a string
    - Second function outputs a string
- Core logic:
    - Convert a list and output a string, then use the second function to convert a string to a list
    - You can use a python string method to convert a string to a list
- Edge cases:
    - If the list length is 0:
        - Return an empty string in the first function
        - Return an empty list in the second function

Plan:
- Create a function to decode a list of strs 
- Create an empty string named count - This would handle the strings added
- 

Implement:
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return "zero"
        # print("Function 1 edge case didnt execute")
        # print(f"Length: {len(strs)}")
        count = ""
        for i in range(len(strs)):
            strs[i] = strs[i].replace(" ", "__")
            if(strs[i] == ""):
                count += "emptystring" + " "
            count += strs[i] + " "
        
        return count
        

    def decode(self, s: str) -> List[str]:
        if(len(s) == 0 or s.strip() == "emptystring"):
            return [""]
        elif(s == "zero"):
            return []
              
            
        # print("Function 2 edge case didnt execute")
        # print("The string s is /'" + s + "/'")
        # print(f"Length: {len(s)}")

        newLst = s.split()
        for i in range(len(newLst)):
            newLst[i] = newLst[i].replace("__", " ")
            if(newLst[i] == "emptystring"):
                print("This if statement executed")
                newLst[i] = newLst[i].replace("emptystring", "")
            # print("The word is " + word + ", it didnt execute if statement")
        return newLst
