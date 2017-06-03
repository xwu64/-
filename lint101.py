class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        length = result = len(A)
        if length <3: return A
        init = A.pop()
        A.insert(0,init)
        B = [A.pop()]
        for _ in xrange(length-2):
            B.insert(0,A.pop())
            if B[0] == B[1]:
                if A[0] == B[0]:
                    B.pop()
                    result -=1
                    continue
                else:
                    A.insert(0,B.pop())
                    continue
            else:
                A.insert(0,B.pop())
        A.insert(0,B.pop())
        return A
