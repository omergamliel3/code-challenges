"""
*** Two Sum ***

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    value_to_index: dict[int, int] = dict()

    for i, num in enumerate(nums):
        candidate = target - num
        
        if candidate in value_to_index:
            return [i, value_to_index[candidate]]
        
        value_to_index[num] = i

    return []


def main():
    print(two_sum([2, 7, 11, 15], 9))  # [0,1]
    print(two_sum([3, 2, 4], 6))  # [1,2]
    print(two_sum([3, 3], 6))  # [0,1]


if __name__ == "__main__":
    main()
