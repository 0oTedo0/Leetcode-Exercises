class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        m,n,nums1,nums2=(m,n,nums1,nums2) if m>n else (n,m,nums2,nums1)  # ensure m>=n
        if n==0:
            if m%2==0:
                return (nums1[m//2-1]+nums1[m//2])/2
            else:
                return nums1[m//2]
        elif m+n==2:
            return (nums1[0]+nums2[0])/2
        elif m==2 and n==1:
            if nums2[0]<=nums1[0]:
                return nums1[0]
            elif nums2[0]>=nums1[1]:
                return nums1[1]
            else:
                return nums2[0]
        elif m>=3*n:
            if nums2[-1]<nums1[(m+n)//4-1]:
                return self.findMedianSortedArrays(nums1[(m+n)//4-n:m-(m+n)//4],[])
            elif nums2[0]>nums1[m-(m+n)//4]:
                return self.findMedianSortedArrays(nums1[(m+n)//4:m-(m+n)//4+n],[])
            else:
                return self.findMedianSortedArrays(nums1[(m+n)//4:m-(m+n)//4],nums2)
        else:
            if nums1[(m+n)//4-1]>=nums2[(m+n)//4-1]:
                down1=0
                down2=(m+n)//4
            else:
                down1=(m+n)//4
                down2=0
            if nums1[m-(m+n)//4]>=nums2[n-(m+n)//4]:
                up1=m-(m+n)//4
                up2=n
            else:
                up1=m
                up2=n-(m+n)//4
            return self.findMedianSortedArrays(nums1[down1:up1],nums2[down2:up2])
