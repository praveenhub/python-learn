# Increase recursion depth if needed for other methods, but DP is iterative
# sys.setrecursionlimit(2000)


def calculate_partitions(max_n):
    """Calculates partition numbers up to max_n using DP."""
    if max_n < 0:
        return {}  # Handle negative input gracefully

    dp = [0] * (max_n + 1)
    if max_n >= 0:
        dp[0] = 1  # Base case

    # DP calculation
    for j in range(1, max_n + 1):
        for i in range(j, max_n + 1):
            dp[i] += dp[i - j]

    # Return results as a dictionary {n: p(n)}
    results = {i: dp[i] for i in range(max_n + 1)}
    return results


# Calculate partitions up to 200
max_val = 200
partitions = calculate_partitions(max_val)

# Get specific values needed for test cases
p_1 = partitions.get(1, "N/A")
p_2 = partitions.get(2, "N/A")
p_3 = partitions.get(3, "N/A")
p_4 = partitions.get(4, "N/A")
p_5 = partitions.get(5, "N/A")
p_6 = partitions.get(6, "N/A")
p_7 = partitions.get(7, "N/A")
p_10 = partitions.get(10, "N/A")
p_20 = partitions.get(20, "N/A")
p_50 = partitions.get(50, "N/A")  # Added a mid-range value
p_100 = partitions.get(100, "N/A")  # Added a higher value
p_200 = partitions.get(200, "N/A")

print(f"{p_1=}")
print(f"{p_2=}")
print(f"{p_3=}")
print(f"{p_4=}")
print(f"{p_5=}")
print(f"{p_6=}")
print(f"{p_7=}")
print(f"{p_10=}")
print(f"{p_20=}")
print(f"{p_50=}")
print(f"{p_100=}")
print(f"{p_200=}")
