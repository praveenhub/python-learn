import fileinput

inputData = ""
for line in fileinput.input():
    inputData += line


def count_ways(n):
    """
    Count the number of ways to sum up to n using positive integers in descending order.

    Args:
        n: The target sum

    Returns:
        The number of ways to sum up to n
    """
    # Create a memoization array
    dp = [1] + [0] * n

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]


def code_here():
    # Parse all numbers from inputData
    all_numbers = [int(x) for x in inputData.split()]

    # First number is the count of test cases
    t = all_numbers[0]

    # The next t numbers are the test cases
    results = []
    for i in range(1, min(t + 1, len(all_numbers))):
        n = all_numbers[i]
        results.append(str(count_ways(n)))

    return "\n".join(results)


print(code_here())
