# Solution

## Task

[303. Range Sum Query - Immutable](https://leetcode-cn.com/problems/range-sum-query-immutable/)


## Problem

Given an integer array ``nums``, find the sum of the elements between indices ``i`` and ``j`` ``(i ≤ j)``, inclusive.


Implement the ``NumArray`` class:


``NumArray(int[] nums)`` Initializes the object with the integer array nums.

``int sumRange(int i, int j)`` Return the sum of the elements of the ``nums`` array in the range ``[i,j]`` inclusive (i.e., ``sum(nums[i], nums[i + 1], ... , nums[j])``)

### Example 1

```
Input
["NumArray", "sumRange", "sumRange", "sumRange"]

[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

Output

[null, 1, -1, -3]

Explanation

NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
```

### Constraints

* 0 <= ``nums.length`` <= 104
* -105 <= ``nums[i]`` <= 105
* 0 <= i <= j < ``nums.length``
* At most 104 calls will be made to sumRange.

## Solution

### Idea
Use **Dynamic programing(DP)** to solve the problem.

**DP** requires ``O(n)`` time for initialization and ``O(n)`` space for storing the created array ``self.sums``, but query time becomes ``O(1)``.

### Key formula

```
sum(i->j)=sum(0->j)-sum(0->i-1)
```

## Code
[303 - Range Sum Query - Immutable](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-01/303%20-%20Range%20Sum%20Query%20-%20Immutable.py)



