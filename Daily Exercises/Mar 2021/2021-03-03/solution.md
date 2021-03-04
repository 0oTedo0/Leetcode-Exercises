# Solution

## Task

[338. Counting Bits](https://leetcode-cn.com/problems/counting-bits/)


## Problem:

Given a non negative integer number ``num``. For every numbers ``i`` in the range ``0 ≤ i ≤ num`` calculate the number of 1's in their binary representation and return them as an array.

### Example 1

```
Input: 2
Output: [0,1,1]
```

### Example 2

```
Input: 5
Output: [0,1,1,2,1,2]
```
### Follow up:

* It is very easy to come up with a solution with run time ``O(n*sizeof(integer))``. But can you do it in linear time ``O(n)`` /possibly in a single pass?
* Space complexity should be ``O(n)``.
* Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

## Solution

### Idea
Use **Dynamic programing(DP)** and **bit operation** to solve the problem.

**DP** requires ``O(n)`` space for storing the created array ``bits``.

**Bit operation** helps determine whether a number is even or odd.

### Key formula

* If ``i`` is the integer power of 2, ``i&(i-1)==0``.
* If ``i`` even, ``i&1==0``.
* ``bits[i]=bits[i-highbit]+1`` where ``highbit`` satisfies ``highbit<=i`` and is the integer power of 2.
  #### Example
  ```
  bits[1101]=bits[101]+1
  ```
* ``bits[i]=bits[i>>1]+(i&1)``
  #### Example
  ```
  bits[1010]=bits[101]+0
  bits[10101]=bits[1010]+1
  ```
* ``bits[i]=bits[i&(i-1)]+1`` Note that ``i&(i-1)`` sets the lowest ``1`` to ``0``.
  #### Example
  ```
  bits[101000100]=bits[101000000]+1
  ```
## Code
[304. Range Sum Query 2D - Immutable](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-02/304.%20Range%20Sum%20Query%202D%20-%20Immutable.py)
