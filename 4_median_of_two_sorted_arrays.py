#----------------------First Try--------------------------O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        N=m+n
        nums=[]
        if m==0 or n==0:
            if n%2==0 and m%2==0:
                try:
                    return (nums2[n//2]+nums2[n//2-1])/2
                except:
                    return (nums1[m//2]+nums1[m//2-1])/2
            else:
                try:
                    return nums2[n//2]
                except:
                    return nums1[m//2]
        for i in range(N//2+1):
            if  len(nums1)==0 :
                nums.append(nums2[0])
                if i!=(N//2):nums2=nums2[1:]
            if  len(nums2)==0 :
                nums.append(nums1[0])
                if i!=(N//2):nums1=nums1[1:]
            if len(nums1) and len(nums2):
                if nums1[0]<=nums2[0]:
                    nums.append(nums1[0])
                    nums1=nums1[1:]
                else:
                    nums.append(nums2[0])
                    nums2=nums2[1:]
        return (nums[N//2]+nums[N//2-1])/2 if N%2==0 else nums[N//2]

//-------------------Second Try--------------------------------O(lg(m+n))
class Solution:
       
    def findKth(self,nums1:List[int],nums2:List[int],k:int):
        m,n=len(nums1),len(nums2)
        if m==0:return nums2[k-1]
        if n==0:return nums1[k-1]
        if k==1:return min(nums1[0],nums2[0])        
        if k//2>m:return self.findKth(nums1,nums2[k//2:],k-k//2)
        if k//2>n:return self.findKth(nums1[k//2:],nums2,k-k//2)
        return self.findKth(nums1,nums2[k//2:],k-k//2) if nums1[k//2-1]>=nums2[k//2-1] else self.findKth(nums1[k//2:],nums2,k-k//2)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n=len(nums1),len(nums2)
        left=(m+n+1)//2
        right=(m+n+2)//2
        l=self.findKth(nums1,nums2,left)
        r=self.findKth(nums1,nums2,right)
        print(l,r)
        return 0.5*(l+r)

//-----------------------KEY--------------------------------------O(lg(m+n))
class Solution:
    def get_kth(self, nums1, nums2, k):
        # print(nums1, nums2, 'k=', k)
        m, n = len(nums1), len(nums2)
        if m == 0: return nums2[k-1]
        if n == 0: return nums1[k-1]
        if k == 1: return min(nums1[0], nums2[0])
        drop1, drop2 = min(k//2, m), min(k//2, n)   # 丢弃个数
        # print('m={},n={},k/2={},drop1={},drop2={}'.format(m,n,k//2,drop1,drop2))
        if nums1[drop1-1] <= nums2[drop2-1]:  # 丢弃nums1部分
            return self.get_kth(nums1[drop1:m], nums2, k-drop1)
        else:
            return self.get_kth(nums1, nums2[drop2:n], k-drop2)
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # 整合奇偶数情况
        mid_left = self.get_kth(nums1, nums2, (m+n+1)//2)
        mid_right = self.get_kth(nums1, nums2, (m+n+2)//2)
        return (mid_left+mid_right)/2 
