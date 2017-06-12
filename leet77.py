class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.results = []
        def helper(n,k,cur,pos):
            if k==0:
                self.results.append(cur)
                return
            i=pos+1
            while i<n+1:
                helper(n,k-1,cur+[i], i)
                i+=1
        helper(n,k,[],0)
        return self.results
