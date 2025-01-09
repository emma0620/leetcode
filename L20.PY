#檢查一個字串 s 是否包含有效的括號配對。

def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# 測試
print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False

