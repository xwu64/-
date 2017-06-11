class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        start = 0
        end = length-1
        leftMax = rightMax = 0
        result = 0
        while start<end:
            if leftMax < height[start]:
                leftMax = height[start]

            if rightMax < height[end]:
                rightMax = height[end]

            if leftMax > rightMax:
                result+=rightMax-height[end]
                end-=1
            else:
                result+=leftMax-height[start]
                start+=1
        return result
