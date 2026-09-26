def is_balanced(expression):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    opening = set(pairs.values())

    for char in expression:
        if char in opening:
            stack.append(char)

        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


expression = input("Enter an expression: ")

if is_balanced(expression):
    print("Parentheses are balanced.")
else:
    print("Parentheses are not balanced.")
