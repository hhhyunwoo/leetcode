import itertools
from typing import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numDict = {2: ["a","b","c"],
        3:["d","e","f"],
        4:["g","h","i"],
        5:["j","k","l"],
        6:["m","n","o"],
        7:["p","q","r","s"],
        8:["t","u","v"],
        9:["w","x","y","z"]
        }
        
        if digits == "": return []
        ans = []

        def recur(letter, nextDigit):
            if len(letter) == len(digits):
                ans.append(letter)
            else:
                for c in numDict[int(nextDigit[0])]:
                    recur(letter+c, nextDigit[1:])
        
        recur("", digits)
        return ans 