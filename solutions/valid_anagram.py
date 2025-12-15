"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

"""


from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()

    if len(s) != len(t):
        return False

    counts: dict[str, int] = defaultdict(int)
    for char in s:
        counts[char] += 1

    for char in t:
        counts[char] -= 1
        if counts[char] < 0:
            return False

    return True
