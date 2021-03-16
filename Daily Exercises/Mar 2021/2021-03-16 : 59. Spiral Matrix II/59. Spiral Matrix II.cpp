class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n));
        
        int x=0,y=0;
        int policies[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
        int policy=0;
        int incre_x=0,incre_y=1;
        int up=0,right=n-1,down=n-1,left=0;

        for(int i=0;i<n*n;i++){
            ans[x][y]=i+1;
            if(policy==0){
                if(y+1<=right){
                    y++;
                }else{  // touch right boundary, the up boundary should move downwards (because this (up) row has been traversed)
                    up++;
                    policy=1;
                    x++;
                }
            }else if(policy==1){
                if(x+1<=down){
                    x++;
                }else{  // touch down boundary, the right boundary should move leftwards (because this (right) column has been traversed)
                    right--;
                    policy=2;
                    y--;
                }
            }else if(policy==2){
                if(y-1>=left){
                    y--;
                }else{  // touch left boundary, the down boundary should move upwards (because this (down) row has been traversed)
                    down--;
                    policy=3;
                    x--;
                }
            }else if(policy==3){
                if(x-1>=up){
                    x--;
                }else{  // touch up boundary, the left boundary should move rightwards (because this (left) column has been traversed)
                    left++;
                    policy=0;
                    y++;
                }
            }
        }
        return ans;
    }
};
