class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        recorder = []
        if len(s) == 0: return 0
        result = 0
        start = end = 0
        while end<len(s):
        	if s[end] in recorder:
        		recorder = recorder[recorder.index(s[end])+1:]
        		recorder.append(s[end])
        	else:
        		recorder.append(s[end])
        	end+=1
        	result = max(result, len(recorder))

       	return result
