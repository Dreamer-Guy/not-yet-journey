#url: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recursion(self,cur,target,k,res):
        if cur is None:
            return -1
        if cur.val==target.val:
            self.getChildFromKDistance(cur,k,res)
            return 1
        left_distance=self.recursion(cur.left,target,k,res)
        if left_distance!=-1:
            if k==left_distance:
                res.append(cur.val)
            else:
                self.getChildFromKDistance(cur.right,k-left_distance-1,res)
            return left_distance+1
        right_distance=self.recursion(cur.right,target,k,res)
        if right_distance!=-1:
            if k==right_distance:
                res.append(cur.val)
            else:
                self.getChildFromKDistance(cur.left,k-right_distance-1,res)
            return right_distance+1
        return -1
    def getChildFromKDistance(self,cur,k,arr):
        if cur is None:
            return
        if k==0:
            arr.append(cur.val)
            return
        self.getChildFromKDistance(cur.left,k-1,arr)
        self.getChildFromKDistance(cur.right,k-1,arr)
    def distanceK(self, root, target, k):
        """
        :type root: TreeNrode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        res=[]
        self.recursion(root,target,k,res)
        return res

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
target=5
k=2
sol=Solution()

        