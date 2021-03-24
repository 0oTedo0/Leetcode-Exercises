# Solution

## Task

[456. 132 Pattern](https://leetcode-cn.com/problems/132-pattern/)

## Problem

Given an array of ``n`` integers ``nums``, a **132 pattern** is a subsequence of three integers ``nums[i]``, ``nums[j] ``and ``nums[k]``
such that ``i < j < k`` and ``nums[i] < nums[k] < nums[j]``.

Return *true* if there is a **132 pattern** in ``nums``, otherwise, return *false*.

### Follow up
  The O(n<sup>2</sup>) is trivial, could you come up with the ``O(n logn)`` or the ``O(n)`` solution?

### Example 1
```
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
```

### Example 2
```
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
```

### Example 3
```
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
```

### Constraints

* ``n`` == ``nums.length``
* 1 <= ``n`` <= 104
* -109 <= ``nums[i]`` <= 109

## Solution

### Idea
**Monotonic Stack**

We choose to enumerate the ``1`` in **132 pattern** in reversed order.

At first, there will be one element ``nums[n-1]`` in the stack ``s``, and the ``2`` is set to be *negative infinity*, denoted as ``max_2``.

In the following, steps are:
  1. We first see whether it can be ``1``. If ``nums[i]<max_2``, it means we have found a solution, with ``nums[i]`` as ``1``, ``max_2`` = max(``2``,``max_2``), and a certain visited element as ``3``.
  2. We then see whether it can be ``3``. If ``nums[i]>s.top``, it means the top element in stack can actually be ``2`` and ``nums[i]`` can be ``3``, and thus we set the ``max_2`` as the top element.
  3. We then see whether it can be ``2``. Since ``max_2`` is updated when an element is pop, then if ``nums[i]``<``2``, it is unnecessary to push ``nums[i]`` into stack ``s``. In other words, there is another better choice for ``2`` and meanwhile we ensure the moniticity of the stack. 

## Code
[456. 132 Pattern.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-24%20:%20456.%20132%20Pattern/456.%20132%20Pattern.cpp)

[456. 132 Pattern.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-24%20:%20456.%20132%20Pattern/456.%20132%20Pattern.py)

[456. 132 Pattern.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-24%20:%20456.%20132%20Pattern/456.%20132%20Pattern.java)
