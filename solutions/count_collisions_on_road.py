"""
Count collisions on a road

There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

The number of collisions can be calculated as follows:

When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
When a moving car collides with a stationary car, the number of collisions increases by 1.
After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.
"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        # skip left-moving cars at the start (they escape freely)
        i = 0
        while i < len(directions) and directions[i] == 'L':
            i += 1

        # skip right-moving cars at the end
        j = len(directions) - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1

        # count all R and L within the middle segment
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1

        return collisions


def main():
    solution = Solution()
    print(solution.countCollisions("RLRSLL"))
    print(solution.countCollisions("LLLRRR"))
    print(solution.countCollisions("RRRRL"))
    print(solution.countCollisions("LLRR"))


if __name__ == "__main__":
    main()
