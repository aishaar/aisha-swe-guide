"""
Fibonacci pattern is used when a problem requires me to find the total number of ways, minimun cost, or 
maximum value to reach a specific state, and that state depends exclusively on a fixed number of 
immediately preceding states (usually last 1 or 2 steps)

This type of problems usually have two constraints
1. Step size -> problem explicitly states that only move in fixed increments 
2. No-adjacency -> problem bans me from picking consecutive elements. Choosing something directly
   impacts the ability to choose the next item

    Thinking steps:
    1. I need to first initialize the dp array. As this is 1D, I need to multiply it with the n + 1
    2. Initialize the base case depending on the problem, but I atleast need the 0 and 1
    3. To make it efficient, I will return the same number which is the starting if statement
    4. The loop iterates from 2 to n+1 (as python is not inclusive of the last index)
    5. The dp is simple, just the previous two steps so i-1 and i-2
    6. Returning the last one in the dp array. If I use n in the initialization, 
       I return n-1 and as I used n+1, I return n in the return statement
    
    Time Complexity: O(n) contributed by iterating the array once. The addition is O(1) 
    Space Complexity: O(n) as we are using the dp array

"""
def fibonacci_tabulation(n:int) -> int:
    if n <= 1:
        return n

    # Initialize
    dp = [0] * (n+1)

    # Base case
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]