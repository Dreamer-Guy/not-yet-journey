#url: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        res=[]
        queue=[root,None]
        sum=0
        count=0
        while len(queue)>0:
            cur=queue.pop(0)
            if cur is None:
                if count==0:
                    break
                print(sum)
                print(count)
                res.append(float(sum)/float(count))
                sum=0
                count=0
                queue.append(None)
                continue
            else:
                count+=1
                sum+=cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res

node15 = TreeNode(15)
node7 = TreeNode(7)
node9 = TreeNode(9)

# Node 20 with children 15 and 7
node20 = TreeNode(20, left=node15, right=node7)

# Root node 3 with children 9 and 20
root = TreeNode(3, left=node9, right=node20)
sol=Solution()
print(sol.averageOfLevels(root))