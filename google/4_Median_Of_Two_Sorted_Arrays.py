class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    nums = nums1 + nums2
    print(nums)
    total = 0
    for i in nums:
      total += i
    
    mean = total / len(nums)
    print(total, mean)
    return mean

if __name__ == "__main__":
  nums1, nums2 = [1,3], [2]
  #nums1, nums2 = [1,2], [3,4]
  x = Solution().findMedianSortedArrays(nums1, nums2)
  print(x)

