class Solution(object):
    result = []
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        def helper(cur, left, right, n):
            if left+right == n*2:
                self.result.append(cur)

            if left<n:
                helper(cur+"(", left+1, right, n)

            if left>right:
                helper(cur+")", left, right+1, n)

        helper("", 0, 0, n)
        return self.result
