"""
Fibonacci pattern is used when a problem requires me to find the total number of ways, minimun cost, or 
maximum value to reach a specific state, and that state depends exclusively on a fixed number of 
immediately preceding states (usually last 1 or 2 steps)

This type of problems usually have two constraints
1. Step size -> problem explicitly states that only move in fixed increments 
2. No-adjacency -> problem bans me from picking consecutive elements. Choosing something directly
   impacts the ability to choose the next item

    Thinking steps:
    1. To make it efficient, I will return the same number which is the starting if statement
    2. Here I do not need the dp array, instead I am using two variables to store the info
    3. Initialize the variables to the respective base cases
    4. The loop iterates from 2 to n+1 (as python is not inclusive of the last index)
    5. For the dp, we use tuple assignment or parallel assignment - because of this I do not have to worry 
       about a getting overwritten. 
       [ The way it works is that first the right side is computed and stored as a tuple. Then it is
       unpacked and assigned to the respective variables on the left side]
    6. Return the second variable as that is the summation of the previous two
    
    Time Complexity: O(n) contributed by iterating the array once. The addition is O(1) 
    Space Complexity: O(1), we have optimized the array with two variables

"""

def fibonacci_space_optimized(n:int) -> int:
    if n <= 1:
        return n

    a = 0
    b = 1

    for _ in range(2, n+1):
        a, b = b, a+b
    return b