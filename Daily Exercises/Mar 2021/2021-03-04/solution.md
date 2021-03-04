# Solution

## Task

[354. Russian Doll Envelopes](https://leetcode-cn.com/problems/russian-doll-envelopes/)


## Problem

You have a number of envelopes with widths and heights given as a pair of integers ``(w, h)``. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

### Note

* Rotation is not allowed.

### Example

```
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

## Solution

### Idea
Use **Dynamic programing(DP)** and **Longest Increasing Subsequence(LIS)** to solve the problem.

We first sort the array with the first value increasing and the second value decreasing and then we just need to focus on the second value.

### Key formula

* ``f[j]`` stands for the minimal value of the last element of LIS of length ``j`` in the first ``i`` elements of ``envelops``.
* If current value (second value) **h<sub>i</sub>** is larger than the maxmimum of ``f``, then we append it to ``f`` and thus it forms a longer increasing subsequence with the 
last element **h<sub>i</sub>**.
* Otherwise we use bisection to find where to insert **h<sub>i</sub>** in ``f`` and then replace the minimal value of the last element of the corresponding LIS.

## Code
[354. Russian Doll Envelopes](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-04/354.%20Russian%20Doll%20Envelopes.py)
