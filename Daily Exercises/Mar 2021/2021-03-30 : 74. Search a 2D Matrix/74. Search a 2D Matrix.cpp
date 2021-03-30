class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size(),n=matrix[0].size();
        int left=0,right=m*n-1;
        while(left<=right){
            int mid=(left+right)/2;
            int row=mid/n;
            int col=mid%n;
            if(matrix[row][col]<target){
                left=mid+1;
            }else if(matrix[row][col]>target){
                right=mid-1;
            }else{
                return true;
            }
        }
        return false;
    }
};
