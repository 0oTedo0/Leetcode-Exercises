# bits[i]=bits[i-highbit]+1
class Solution_1:
    def countBits(self, num):
        bits=[0]
        highBit=0
        for i in range(1,num+1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i-highBit]+1)
        return bits
      
# bits[i]=bits[i>>1]+(i&1)
class Solution_2:
    def countBits(self, num):
        bits=[0]
        for i in range(1,num+1):
            bits.append(bits[i>>1]+(i&1))
        return bits
      
# bits[i]=bits[i&(i-1)]+1
class Solution_3:
    def countBits(self, num):
        bits=[0]
        for i in range(1,num+1):
            bits.append(bits[i&(i-1)]+1)
        return bits
