"""
* Best Time to Buy and Sell Stock II *

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.

You can only hold at most one share of the stock at any time.

However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.
"""


def find_rising_sequences(prices: list[int]) -> list[list[int]]:
    rising_sequences = []
    i = 0
    while i < len(prices) - 1:
        if prices[i] < prices[i + 1]:
            sequence = []
            sequence.append(prices[i])
            i += 1

            while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                sequence.append(prices[i])
                i += 1

            sequence.append(prices[i])
            rising_sequences.append(sequence)

        i += 1

    return rising_sequences


def find_max_profit(prices: list[int]) -> int:
    rising_sequences = find_rising_sequences(prices)
    max_profit = 0

    for seq in rising_sequences:
        profit = seq[-1] - seq[0]
        max_profit += profit

    return max_profit


def find_max_profit_optimal(prices: list[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


def main():
    print(find_rising_sequences([7, 1, 5, 3, 6, 4]))
    print(find_rising_sequences([1, 2, 3, 4, 5]))
    print(find_rising_sequences([7, 6, 4, 3, 1]))
    print(find_rising_sequences([7, 1, 5, 3, 6, 7, 4, 10]))

    print(find_max_profit([7, 1, 5, 3, 6, 4]))  # 7
    print(find_max_profit([1, 2, 3, 4, 5]))  # 4
    print(find_max_profit([7, 6, 4, 3, 1]))  # 0
    print(find_max_profit([7, 1, 5, 3, 6, 7, 4, 10]))  # 14


if __name__ == "__main__":
    main()
