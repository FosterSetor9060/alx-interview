Minimum Operations: Calculating Fewest Operations
Overview
Welcome to the “Minimum Operations” project! In this algorithmic challenge, we’ll explore how to achieve a specific number of characters using only “Copy All” and “Paste” operations. The goal is to find the fewest number of operations needed to result in exactly n H characters in the file.

Learning Objectives
By completing this project, you’ll gain knowledge in the following areas:

Dynamic programming: Breaking down problems into simpler subproblems and building up the solution.
Prime factorization: Understanding how to find the sum of prime factors for a given number.
Code optimization: Approaching problems from an optimization perspective.
Greedy algorithms: Choosing the best option at each step.
Basic Python programming: Proficiency in loops, conditionals, and functions.
Project Tasks
0. Minimum Operations
Given a number n, write a method minOperations(n) that calculates the fewest number of operations needed to result in exactly n H characters in the file.
The method should return an integer.
If achieving n H characters is impossible, return 0.
Example:
For n = 9:

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHH => Paste => HHHHHHHH
Number of operations: 6
Usage Example
Python

# Example usage of minOperations function
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 4

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))  # Output: 7
