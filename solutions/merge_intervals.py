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

    while len(intervals) > 0:
        min_index = 0
        min_start = intervals[0][0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < min_start:
               min_start = intervals[i][0]
               min_index = i
            
        current = intervals[min_index]
        del intervals[min_index]

        found_overlap = True
        while found_overlap:
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
                    found_overlap = True
                    
                    # exit loop 
                    break
        
        merged_intervals.append(current)

    return merged_intervals


def main():
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge([[1, 4], [4, 5]]))
    print(merge([[4, 7], [1, 4]]))


if __name__ == "__main__":
    main()
