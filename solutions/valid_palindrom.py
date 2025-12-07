"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        candidate = "".join([char.lower() for char in s if char.isalnum()])
        length = len(candidate)

        for i in range(length):
            if candidate[i] != candidate[length - 1 - i]:
                return False

        return True


def main():
    palindrome = ValidPalindrome()
    print(palindrome.isPalindrome("A man, a plan, a canal: Panama"))
    print(palindrome.isPalindrome("race a car"))
    print(palindrome.isPalindrome(" "))


if __name__ == "__main__":
    main()
