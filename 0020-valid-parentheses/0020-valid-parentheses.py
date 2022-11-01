class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in p:
                stack.append(i)
            else:
                if not stack: return False
                curr = stack.pop()
                if p[curr] != i:
                    return False
        return not stack
            