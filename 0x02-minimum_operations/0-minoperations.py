#!/usr/bin/python3
""" Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly
n H characters in the file. """


def minOperations(n):
    if n == 1:
        return 0

    """Initialize an array to store the minimum number
    of operations for each position"""
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    """Iterate from 2 to n to calculate the minimum
    operations for each position"""
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    """If dp[n] is still infinity, it means it's
    impossible to achieve n H characters"""
    return dp[n] if dp[n] != float('inf') else 0
