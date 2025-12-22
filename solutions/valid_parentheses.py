"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:
- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.
"""

PARENTHESES = "([{)]}"
OPEN_PARENTHESES = frozenset("([{")
CLOSED_PARENTHESES = frozenset(")]}")

MATCHING_PARENTHESES = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def is_valid_parentheses(s: str) -> bool:
    for char in s:
        if char not in PARENTHESES:
            raise ValueError("input contains invalid characters")

    open_stack = []
    for char in s:
        if char in OPEN_PARENTHESES:
            open_stack.append(char)
        elif len(open_stack) > 0:
            last_open = open_stack.pop()
            if MATCHING_PARENTHESES.get(last_open) != char:
                return False
        else:
            return False

    return len(open_stack) == 0


def main():
    print(is_valid_parentheses("()"))
    print(is_valid_parentheses("()[]{}"))
    print(is_valid_parentheses("(]"))
    print(is_valid_parentheses("([])"))
    print(is_valid_parentheses("([)]"))


if __name__ == "__main__":
    main()
