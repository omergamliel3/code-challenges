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
