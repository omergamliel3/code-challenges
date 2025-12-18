"""
* Merge Intervals * 

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:
- 1 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 104
"""


Interval = list[int]


def merge(intervals: list[Interval]) -> list[Interval]:
    merged_intervals: list[Interval] = []
    intervals.sort(key=lambda x: x[0])

    while len(intervals) > 0:
        current = intervals[0]
        del intervals[0]

        while True:
            found_overlap = False

            # search for overlapc
            for i in range(len(intervals)):
                is_overlap = intervals[i][0] <= current[0] <= intervals[i][1] \
                    or intervals[i][0] <= current[1] <= intervals[i][1] \
                    or current[0] <= intervals[i][0] <= current[1] \
                    or current[0] <= intervals[i][1] <= current[1]
                if is_overlap:
                    # update current merged interval
                    current[0] = min(current[0], intervals[i][0])
                    current[1] = max(current[1], intervals[i][1])

                    # remove interval from the list
                    del intervals[i]

                    # exit loop
                    found_overlap = True
                    break

            if not found_overlap:
                break

        merged_intervals.append(current)

    return merged_intervals


def merge_optimal(intervals: list[Interval]) -> list[Interval]:
    if not intervals:
        return []

    # Step 1: sort intervals by start
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    # Step 2: merge overlapping intervals
    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            # overlap → merge
            merged[-1][1] = max(last_end, end)
        else:
            # no overlap → add new interval
            merged.append([start, end])

    return merged


def main():
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge([[1, 4], [4, 5]]))
    print(merge([[4, 7], [1, 4]]))


if __name__ == "__main__":
    main()
