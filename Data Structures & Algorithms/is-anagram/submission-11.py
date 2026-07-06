'''
1. Understand
- Inputs a string s, and string t
- Outputs a boolean
- The function detects if a word is an anagram if the same set of characters appear in the other string
- Possible edge cases: 
    - 1 letter word

2. Plan
- Create function
- Create a variable named "countS" and "countT" to keep track of the letters mentioned, this is so that we can see how often the letters are being used
- Use a for loop to iterate through the letters via range(len(t) OR len(s))
    - If the letter is in dictionary for t:
        - Update the dictionary, value++
        - Else: Update the "countT", value = 1
    - If the letter is in dictionary for s:
        - Update the dictionary, value++
        - Else: Update the "countS", value = 1
- Return "countS" == "countT"

3. Implement
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if(not len(s) == len(t)): return False

        for i in range(len(s)):
            if(s[i] in countS):
                countS.update({s[i] : countS.get(s[i]) + 1})
            else:
                countS.update({s[i] : 1})
            if(t[i] in countT):
                countT.update({t[i] : countT.get(t[i]) + 1})
            else:
                countT.update({t[i] : 1})

        print(countS.keys())
        print(countT.keys())

        for key in countS:
            if(key in countT):
                if(countS.get(key) == countT.get(key)):
                    continue
                else:
                    return False
            return False
        return True
        