class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        start = end = 0
        result = len(nums) +1
        total = nums[0]

        while end<len(nums) and start<=end:
            if total >= s:
                result = min(result, end-start+1)
                if result == 1: return result
                total -= nums[start]
                start+=1
            else:
                end+=1
                if end < len(nums):
                    total += nums[end]
        if result == len(nums)+1: return 0
        return result
