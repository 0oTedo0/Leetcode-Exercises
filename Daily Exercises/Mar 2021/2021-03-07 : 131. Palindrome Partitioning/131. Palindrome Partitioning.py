class Solution:
    def partition(self, s):
        n = len(s)
        f = [[True] * n for _ in range(n)]  # f(i,j) stands for whether s[i:j+1] is a palindrome

        for i in range(n - 1, -1, -1):  # note the correct the process order
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]  # DP

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:  # DFS meets the end, append ans to ret
                ret.append(ans[:])  # note that it should be a deep copy, otherwise ret varies when ans does
                return
            
            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret
