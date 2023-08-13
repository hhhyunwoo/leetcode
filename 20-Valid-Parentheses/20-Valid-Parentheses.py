class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False 
                popVal = stack.pop(-1)
                if c == ')' and popVal != '(':
                    return False
                elif c == '}'and popVal != '{':
                    return False
                elif c == ']'and popVal != '[':
                    return False

        if len(stack) > 0: return False
        else: return True