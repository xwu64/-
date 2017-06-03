class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        result = length = len(A)
        for _ in xrange(length):
            popNum = A.pop()
            if popNum == elem:
                result -=1
                continue
            else:
                A.insert(0,popNum)
        return result
