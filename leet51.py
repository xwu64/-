class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        line = ['x']*n
        panel = []
        for i in range(n): panel.append(line[:])
        self.result = []
        def helper(panel, n, qNum):
            '''
            print qNum
            for line in panel:
                print line
            print '==========================='
            '''
            if qNum == 0:
                re = []
                for line in panel:
                    re.append("".join(line))
                self.result.append(re)
                return
            for i in range(n-qNum, n-qNum+1):
                for j in range(n):
                    if panel[i][j]=='x':

                        origin = []
                        for each in panel:
                            origin.append(each[:])

                        for k in range(n):
                            panel[k][j] = '.'
                            panel[i][k]='.'

                        k = 1
                        while (i+k<n and j+k<n) or (i-k>=0 and j-k>=0) or (i-k>=0 and j+k<n) or (i+k<n and j-k>=0):
                            if i+k<n and j+k<n: panel[i+k][j+k] = '.'
                            if i-k>=0 and j-k>=0: panel[i-k][j-k] = '.'
                            if i-k>=0 and j+k<n: panel[i-k][j+k] = '.'
                            if i+k<n and j-k>=0: panel[i+k][j-k] = '.'
                            k+=1
                        panel[i][j] = 'Q'
                        helper(panel, n, qNum-1)

                        panel = origin

        helper(panel, n, n)
        return self.result
