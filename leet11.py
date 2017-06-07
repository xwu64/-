class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        result = 0

        while start!=end:
        	result = max(result, min(height[start], height[end])*(end-start))
        	if height[start] > height[end]: end-=1
        	else: start+=1

        return result
