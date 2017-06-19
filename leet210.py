class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        matrix = []
        path = []
        for _ in xrange(numCourses): matrix.append([])
        pre = [0]*numCourses
        for i,j in prerequisites:
            pre[j]+=1
            matrix[i].append(j)

        nodeQ = []
        counter = 0
        for i, each in enumerate(pre):
            if each == 0:
                nodeQ.append(i)
                path.append(i)
                counter+=1

        while len(nodeQ) > 0:
            i = nodeQ.pop(0)
            for j in matrix[i]:
                pre[j] -= 1
                if pre[j] == 0:
                    counter+=1
                    nodeQ.append(j)
                    path.append(j)
        if counter == numCourses: return path[::-1]
        else: return []

