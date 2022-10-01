class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in ('+', '-','*','/'):
                stack.append(str(i))
            elif i in ('+','-','*'):
                r, l = stack.pop(), stack.pop()
                stack.append(str(int(eval(l+i+r))))
            else:
                r, l = int(stack.pop()), int(stack.pop())
                stack.append(str(int(float(l)/r)))
        return int(stack.pop())