class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # Write your code here

        def binary_search(s, start, end, target):
            if start>end:
                return -1

            mid = start + (end -start)/2
            if s[mid] > target: return binary_search(s, start, mid-1, target)
            if s[mid] < target: return binary_search(s, mid+1, end, target)
            return mid

        length = len(nums)
        for i in xrange(length):
            index = binary_search(nums,0, length-1, target-nums[i])
            if index != -1 and index != i:
                if index > i : return [i+1,index+1]
                else: return [index+1, i+1]

        return []
