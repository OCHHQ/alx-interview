0x08 Making Change Project
Overview
This project implements a solution to the classic Coin Change Problem using dynamic programming. The goal is to determine the minimum number of coins needed to make a specific total amount from a given set of coin denominations.
Problem Description
The challenge is to write a function makeChange() that:

Takes a list of coin denominations
Takes a target total amount
Returns the fewest number of coins needed to meet the total
Handles various edge cases

Algorithm Approach
Dynamic Programming Solution
The solution uses a bottom-up dynamic programming approach:

Create a DP table to store minimum coins for each amount
Initialize the table with a "large" value (total + 1)
Set base case: 0 coins needed to make 0 amount
Iterate through all amounts from 1 to total
For each amount, try all coin denominations
Update minimum coins needed using optimal substructure principle

Key Features

Time Complexity: O(total * number of coins)
Space Complexity: O(total)
Handles edge cases like:

Total less than or equal to 0
Impossible to make the total amount



Requirements

Python 3.4.3+
Ubuntu 20.04 LTS
PEP 8 style guidelines
