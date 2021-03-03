# Solution

## Task

[303. Range Sum Query - Immutable](https://leetcode-cn.com/problems/range-sum-query-immutable/)


## Problem:

Given an integer array ``nums``, find the sum of the elements between indices ``i`` and ``j`` ``(i ≤ j)``, inclusive.


Implement the ``NumArray`` class:


``NumArray(int[] nums)`` Initializes the object with the integer array nums.

``int sumRange(int i, int j)`` Return the sum of the elements of the ``nums`` array in the range ``[i,j]`` inclusive (i.e., ``sum(nums[i], nums[i + 1], ... , nums[j])``)


## Solution

### Idea
Use **Dynamic programing(DP)** to solve the problem.

**DP** require ``O(n)`` time for initialization and ``O(n)`` space for storing the created array ``self.sums``, but query time becomes ``O(1)``.
