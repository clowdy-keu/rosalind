# Problem
# Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2
# and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).
# Given: Positive integers n≤100
# and m≤20
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m
# months.
# Sample Dataset
# 6 3
# Sample Output
# 4

# Doesn't work for death <= 2
from functools import lru_cache
@lru_cache()
def recursive_rabbit (n = 10, death = 4):
    print('Вызов n = ', n)
    if n == 3:
        return 2
    elif n == 2 or n == 1 or n == 0:
        return 1
    elif n <= -1:
        return 0
    else:
        return (recursive_rabbit(n-1) + recursive_rabbit(n-2) - recursive_rabbit(n - death - 1))
print(recursive_rabbit())