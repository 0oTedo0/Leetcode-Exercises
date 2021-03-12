# Solution

## Task

[331. Verify Preorder Serialization of a Binary Tree](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/)


## Problem

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value.
If it is a null node, we record using a sentinel value such as ``#``.

```
       _9_
      /   \
     3     2
    / \   / \
   4   1  #  6
  / \ / \   / \
  # # # #   # #
```

For example, the above binary tree can be serialized to the string ``"9,3,4,#,#,1,#,#,2,#,6,#,#"``, where ``#`` represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character ``'#'`` representing ``null`` pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as ``"1,,3"``.

### Example 1
```
Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
```

### Example 2
```
Input: "1,#"
Output: false
```
### Example 3
```
Input: "9,#,#,1"
Output: false
```

## Solution

### Idea
Use **Stack** to solve the problem. The **stack** checks whether the string obeys the pre-order.

When there are 2 ``#``s on the top of the stack, it means the current node have 2 ``null`` children.
Then we pop them out, and replace the current node with ``#`` (i.e. ``null``). We continue the process until only 1 ``#`` left (return *true*) or finding that is disobeys the pre-order
(return *false*).

## Code
[331. Verify Preorder Serialization of a Binary Tree](https://github.com/0oTedo0/Leetcode-Exercises/blob/main/Daily%20Exercises/Mar%202021/2021-03-12%20:%20331.%20Verify%20Preorder%20Serialization%20of%20a%20Binary%20Tree/331.%20Verify%20Preorder%20Serialization%20of%20a%20Binary%20Tree.py)

