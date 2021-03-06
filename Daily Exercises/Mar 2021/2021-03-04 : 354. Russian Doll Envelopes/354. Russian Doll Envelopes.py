class Solution:
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        if not n:
          return 0
        
        envelopes.sort(key=lambda x: (x[0],-x[1]))  # The first value increases and the second value decreases

        f = [envelopes[0][1]]
        for i in range(1,n):
            num=envelopes[i][1]
            if num>f[-1]:  # If the current value is larger, it forms a longer increasing subsequence
                f.append(num)
            else:
                index = bisect.bisect_left(f,num)  # Otherwise we replace the minimal value of the last element of the corresponding LIS
                f[index] = num
        
        return len(f)
