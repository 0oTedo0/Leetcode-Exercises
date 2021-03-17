# Solution

## Task

[6. ZigZag Conversion](https://leetcode-cn.com/problems/zigzag-conversion/)


## Problem

The string ``"PAYPALISHIRING"`` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: ``"PAHNAPLSIIGYIR"``

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);
```
### Example 1
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

### Example 2
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

### Example 3
```
Input: s = "A", numRows = 1
Output: "A"
```

### Constraints

* 1 <= ``s.length`` <= 1000
* ``s`` consists of English letters (lower-case and upper-case), ``','`` and ``'.'``.
* 1 <= ``numRows`` <= 1000

## Solution

### Idea
The key point to this problem is **Path Simulation**. That is, you need to figure out the rule of the order of string, and then process the string in order.


## Code
[6. ZigZag Conversion.cpp](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Normal/6.%20ZigZag%20Conversion/6.%20ZigZag%20Conversion.cpp)

[6. ZigZag Conversion.py](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Normal/6.%20ZigZag%20Conversion/6.%20ZigZag%20Conversion.py)

[6. ZigZag Conversion.java](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Normal/6.%20ZigZag%20Conversion/6.%20ZigZag%20Conversion.java)
