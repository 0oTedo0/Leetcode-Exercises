# Solution

## Task

[705. Design HashSet](https://leetcode-cn.com/problems/design-hashset/)


## Problem

Design a HashSet without using any built-in hash table libraries.

Implement ``MyHashSet`` class:

* void ``add(key)`` Inserts the value ``key`` into the HashSet.
* bool ``contains(key)`` Returns whether the value ``key`` exists in the HashSet or not.
* void ``remove(key)`` Removes the value ``key`` in the HashSet. If ``key`` does not exist in the HashSet, do nothing.
 

### Example 1

```
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]

Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
```

### Constraints

* 0 <= ``key`` <= 106
* At most 104 calls will be made to add, remove, and contains.
 

### Follow up
  Could you solve the problem without using the built-in HashSet library?

## Solution

### Idea
The key point to this task is designing a hash function and how to deal with collision.

A simple has function is ``mod`` function.

Collision problem is solved by a ``list``. That is, all elements having the same hash value are put into a list together.

## Code
[705. Design HashSet](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-13%20:%20705.%20Design%20HashSet/705.%20Design%20HashSet.py)

