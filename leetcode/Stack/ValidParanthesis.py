""" Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
* """
class ValidParanthesis(object):

    def valparan(self, s):
        if len(s) == 0:
            return True
        if len(s)%2 == 1:
            return False
        pdict = {}
        pdict[']'] = '['
        pdict['}'] = '{'
        pdict[')'] = '('
        stack = []
        for i in range(len(s)):
            if s[i] in pdict.keys():
                if len(stack) != 0:
                    top = stack.pop()
                else:
                    top = '#'
                if top != pdict[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0  # important return len(stack) == 0

paranthesis = ValidParanthesis()
print(paranthesis.valparan("{][()"))
print(paranthesis.valparan("{][()"))
print(paranthesis.valparan("()"))
print(paranthesis.valparan("{}"))
