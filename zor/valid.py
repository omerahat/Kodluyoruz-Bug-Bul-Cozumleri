def isValid(s):
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in bracket_pairs:
            stack.append(char)
        else:
            if not stack or bracket_pairs[stack.pop()] != char:
                return False

    return not stack

print(isValid("()"))         # Output: True
print(isValid("()[]{}"))     # Output: True
print(isValid("(]"))         # Output: False
