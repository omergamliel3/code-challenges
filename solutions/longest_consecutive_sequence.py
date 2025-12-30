"""
* Longest Consecutive Sequence *

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Constraints:
- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109
"""

# O(n * log n) solution


def longest_consecutive_1(nums: list[int]) -> int:
    longest = 0

    nums_sorted = sorted(set(nums))
    sequence_len = 0
    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i + 1] - nums_sorted[i] == 1:
            sequence_len += 1
            longest = max(sequence_len, longest)
        else:
            sequence_len = 0

    return longest


# O(n^2) solution
def longest_consecutive_2(nums: list[int]) -> int:
    longest = 0
    nums_set = set(nums)

    for num in nums_set:
        sequence = 1
        comparor = num

        while comparor + 1 in nums_set:
            sequence += 1
            comparor += 1

        comparor = num
        while comparor - 1 in nums_set:
            sequence += 1
            comparor -= 1

        longest = max(longest, sequence)

    return longest

# O(n) solution


def longest_consecutive(nums: list[int]) -> int:
    longest = 0
    nums_set = set(nums)

    for num in nums_set:
        sequence_len = 1
        if num - 1 not in nums_set:
            comparor = num

            # while loop can run max n' times total
            while comparor + 1 in nums_set:
                sequence_len += 1
                comparor += 1

            longest = max(longest, sequence_len)

    return longest


def main():
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longest_consecutive([1, 0, 1, 2]))


if __name__ == "__main__":
    main()
