class Solution:
    def minCut(self, s):
        n = len(s)
        f = [[True] * n for _ in range(n)]  # f(i,j) stands for whether s[i:j+1] is a palindrome

        for i in range(n - 1, -1, -1):  # note the correct the process order
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]  # DP

        g=[n]*n

        for i in range(n):
            if f[0][i]:  # a palindrome needs no split
                g[i]=0
            else:
                for j in range(i):
                    if f[j+1][i]:  # transition formula: g[i] = min(g[j])+1, where 0<=j<=i-1
                        g[i]=min(g[i],g[j]+1)
        
        return g[n-1]
