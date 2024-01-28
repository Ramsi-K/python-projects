class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_nums = sorted(nums1 + nums2)
        print(combined_nums)
        length = len(combined_nums)
        print(length)
        print(length % 2)
        if not length % 2:
            print("even")
            print(math.ceil(length/2))
            print(math.floor(length/2))
            print((combined_nums[math.ceil(length/2)-1] + combined_nums[math.floor(length/2)])/2)
            return (combined_nums[math.ceil(length/2)-1] + combined_nums[math.floor(length/2)])/2
        else:
            print("odd")
            print((length/2 - 0.5))
            return combined_nums[int(length/2 - 0.5)]

        