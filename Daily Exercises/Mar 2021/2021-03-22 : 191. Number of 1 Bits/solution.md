# Solution

## Task

[191. Number of 1 Bits](https://leetcode-cn.com/problems/number-of-1-bits/)

## Problem

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the ``Hamming weight``).

### Note

* Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using ``2's complement notation``. Therefore, in **Example 3**, the input represents the signed integer ``-3``.
 
### Example 1
```
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

### Example 2
```
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
```

### Example 3
```
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

### Constraints

* The input must be a binary string of length 32.
 
### Follow up
  If this function is called many times, how would you optimize it?

## Solution

### Idea
**Bit operations**

There are 2 ways to get '1's.
  1. We can figure out whether the last element is '1' via ``x&1``. (implemented in codes) ———— Time complexity: ``O(k)`` where ``k`` is the position of the highest '1'.
  2. We can set the lowest '1' to 0 via ``x=x&(x-1)``.  ———— Time complexity: ``O(l)`` where ``l`` the ``Hamming weight``.

## Code
[191. Number of 1 Bits.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-22%20:%20191.%20Number%20of%201%20Bits/191.%20Number%20of%201%20Bits.cpp)

[191. Number of 1 Bits.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-22%20:%20191.%20Number%20of%201%20Bits/191.%20Number%20of%201%20Bits.py)

[191. Number of 1 Bits.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-22%20:%20191.%20Number%20of%201%20Bits/191.%20Number%20of%201%20Bits.java)
