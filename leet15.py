class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        length = len(nums)

        for i in xrange(length):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start = i+1
            end = length-1

            while end>start:
                if start>i+1 and nums[start] == nums[start-1]:
                    start+=1
                    continue
                #print start,end,i
                if nums[start]+nums[end]+nums[i] == 0:
                    results.append([nums[i], nums[start], nums[end]])
                    start+=1
                    end-=1
                elif nums[start]+nums[end]+nums[i] < 0:
                    start+=1
                else:
                    end-=1

        return results
