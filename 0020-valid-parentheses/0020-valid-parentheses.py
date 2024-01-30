class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    closeKeys = {')': '(', ']': '[', '}': '{'}

    for c in s:
      if c in closeKeys.keys():
        if not stack or stack.pop() != closeKeys[c]:
          return False
      else:
        stack.append(c)
  
    return True if not stack else False