import time

# Matrix Chain Multiplication using Dynamic Programming
def matrix_chain_order(p):
    n = len(p) - 1

    # dp[i][j] stores the minimum multiplication cost
    # for matrices Ai to Aj
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


# Dimensions of matrices
# A1 = 10x30
# A2 = 30x5
# A3 = 5x60
# A4 = 60x20
# A5 = 20x10
dimensions = [10, 30, 5, 60, 20, 10]

# Start execution timer
start_time = time.perf_counter()

# Calculate minimum multiplication cost
minimum_cost = matrix_chain_order(dimensions)

# Stop execution timer
end_time = time.perf_counter()

execution_time = end_time - start_time

print("Matrix Chain Multiplication")
print("--------------------------------")
print("Matrix dimensions:", dimensions)
print("Minimum number of scalar multiplications:", minimum_cost)
print("Execution time:", execution_time, "seconds")