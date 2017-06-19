# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodeD = {}
        nodeList = [node]
        if node is None: return
        while len(nodeList) > 0:
            vNode = nodeList.pop()
            copyNode = None
            if nodeD.has_key(vNode.label):
                if len(nodeD[vNode.label].neighbors) > 0: continue
                copyNode = nodeD[vNode.label]
            else:
                copyNode = UndirectedGraphNode(vNode.label)
                nodeD[vNode.label] = copyNode
            for n0de in vNode.neighbors:
                if nodeD.has_key(n0de.label):
                    copyNode.neighbors.append(nodeD[n0de.label])
                else:
                    neighbor = UndirectedGraphNode(n0de.label)
                    nodeD[n0de.label] = neighbor
                    copyNode.neighbors.append(nodeD[n0de.label])
            nodeList = vNode.neighbors+nodeList
        return nodeD[node.label]
