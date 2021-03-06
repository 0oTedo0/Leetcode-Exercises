# Solution

## Task

[4. Median of Two Sorted Arrays](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)


## Problem

Given two sorted arrays ``nums1`` and ``nums2`` of size ``m`` and ``n`` respectively, return **the median** of the two sorted arrays.

### Example 1
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

### Example 2
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

### Example 3
```
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
```

### Example 4
```
Input: nums1 = [], nums2 = [1]
Output: 1.00000
```

### Example 5
```
Input: nums1 = [2], nums2 = []
Output: 2.00000
```

### Constraints

* ``nums1.length == m``
* ``nums2.length == n``
* 0 <= ``m`` <= 1000
* 0 <= ``n`` <= 1000
* 1 <= ``m + n`` <= 2000
* -106 <= ``nums1[i], nums2[i]`` <= 106

## Solution

### Idea
**Bisection**.

As long as we cut down the scale by a half everytime, the time complexity is ``O(log(m+n))``.

There is a better but not intuitive solution in [LeetCode official solution](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/)
whose time complexity is ``O(log(min(m+n)))``.
## Code
[4. Median of Two Sorted Arrays](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Basic%20Exercises/Hard/4.%20Median%20of%20Two%20Sorted%20Arrays/4.%20Median%20of%20Two%20Sorted%20Arrays.py)
