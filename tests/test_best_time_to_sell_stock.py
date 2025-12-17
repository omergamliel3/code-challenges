import unittest

from parameterized import parameterized

from solutions.best_time_to_sell_stock import find_max_profit


class TestBestTimeToSellStock(unittest.TestCase):
    @parameterized.expand([
        # --- Edge cases ---
        ([], 0),
        ([5], 0),
        ([5, 3], 0),
        ([3, 5], 2),

        # --- Flat prices ---
        ([3, 3, 3, 3], 0),
        ([1, 1, 2, 2, 3, 3], 2),

        # --- Monotonic patterns ---
        ([1, 2, 3, 4, 5], 4),
        ([5, 4, 3, 2, 1], 0),

        # --- Classic examples ---
        ([7, 1, 5, 3, 6, 4], 7),
        ([7, 1, 5, 3, 6, 7, 4, 10], 14),

        # --- Zig-zag patterns ---
        ([1, 3, 2, 4, 3, 5], 6),
        ([5, 1, 5, 1, 5], 8),

        # --- Same-day buy/sell semantics ---
        ([1, 2, 1, 2, 1, 2], 3),

        # --- Realistic noisy data ---
        ([2, 1, 2, 0, 1], 2),
        ([3, 2, 6, 5, 0, 3], 7),

        # --- Large jumps ---
        ([1, 100, 1, 100], 198),
    ])
    def test_given_stock_prices_then_return_max_profit(
        self,
        prices: list[int],
        expected_max_profit: int,
    ):
        res = find_max_profit(prices)
        self.assertEqual(res, expected_max_profit)


if __name__ == "__main__":
    unittest.main()
