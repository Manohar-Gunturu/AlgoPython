# Written with love by atm1504
from typing import List


def mincostTickets(days: List[int], costs: List[int]) -> int:
    # get last day
    n = days[-1]
    days = set(days)
    periods = [1, 7, 30]
    dp = [0] * (n + 30)
    for day in range(1, n + 1):
        if day in days:
            dp[day] = min([dp[day - period] + c for c, period in zip(costs, periods)])
        else:
            dp[day] = dp[day - 1]

    return dp[n]


r = mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15])
print(r)
