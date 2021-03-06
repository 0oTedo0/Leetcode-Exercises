class Solution:
    def spiralOrder(self, matrix):
        m=len(matrix)
        n=len(matrix[0]) if matrix else 0
        
        ans=list()
        point=[0,0]  # current position
        increment=[0,1]  # move direction
        
        # boundary setting
        up=0
        right=n-1
        down=m-1
        left=0
        
        while(len(ans)<m*n):
            ans.append(matrix[point[0]][point[1]])
            if increment==[0,1]:
                if point[1]+1<=right:
                    point[1]+=1
                else:  # touch right boundary, the up boundary should move downwards (because this (up) row has been traversed)
                    up+=1
                    increment=[1,0]
                    point[0]+=1
            elif increment==[1,0]:
                if point[0]+1<=down:
                    point[0]+=1
                else:  # touch down boundary, the right boundary should move leftwards (because this (right) column has been traversed)
                    right-=1
                    increment=[0,-1]
                    point[1]-=1
            elif increment==[0,-1]:
                if point[1]-1>=left:
                    point[1]-=1
                else:  # touch left boundary, the down boundary should move upwards (because this (down) row has been traversed)
                    down-=1
                    increment=[-1,0]
                    point[0]-=1
            elif increment==[-1,0]:
                if point[0]-1>=up:
                    point[0]-=1
                else:  # touch up boundary, the left boundary should move rightwards (because this (left) column has been traversed)
                    left+=1
                    increment=[0,1]
                    point[1]+=1
        return ans
            
            
