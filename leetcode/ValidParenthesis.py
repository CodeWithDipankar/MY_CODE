'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
#Answer:

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mappingDict = {')':'(','}':'{',']':'['}

        stack = []
        for index, eachItem in enumerate(s):
            if eachItem in mappingDict:
                if len(stack)>0 and stack.pop() == mappingDict[eachItem]:
                    if index == len(s)-1:
                        if len(stack) == 0:
                            return True
                        else:
                            return False
                    else:
                        continue
                else:
                    return False
            else:
                stack.append(eachItem)

            

s = '([()]{[{}{}])'
A = Solution()
print(A.isValid(s))
