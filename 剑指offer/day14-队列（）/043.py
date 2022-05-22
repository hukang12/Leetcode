# -- coding: utf-8 --
# @Time : 2022/5/22 18:37
# @Author : HK
# @File : 043.py
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root  # 根节点
        self.dfs = deque([root])
        # 遍历初始二叉树，找到第一个非满的结点（左空 或者 右空）
        while self.dfs:
            tmp = self.dfs[0]
            if tmp.left:
                self.dfs.append(tmp.left)
            else:
                break
            if tmp.right:
                self.dfs.append(tmp.right)
            else:
                break
            self.dfs.popleft()

    def insert(self, v: int) -> int:
        insert_node = TreeNode(v)
        while self.dfs:
            cur_node = self.dfs[0]
            kids = 0
            if cur_node.left: kids += 1
            if cur_node.right: kids += 1
            if kids == 2:  # 有左右孩子
                self.dfs.popleft()
                continue
            if kids == 1:  # 只有左孩子,插入为右节点
                cur_node.right = insert_node
            else:  # 无孩子，插入为左孩子
                cur_node.left = insert_node

            self.dfs.append(insert_node)
            return cur_node.val

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()