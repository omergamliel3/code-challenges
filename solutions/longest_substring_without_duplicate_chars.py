"""
Longest Subs Without Repeating Characters

Given a s s, find the length of the longest subs without duplicate characters.
A subs is a contiguous non-empty sequence of characters within a s.

s consists of English letters, digits, symbols and spaces.
"""


def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


def main():
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))


if __name__ == "__main__":
    main()
