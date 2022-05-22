# -- coding: utf-8 --
# @Time : 2022/5/16 10:21
# @Author : HK
# @File : 021.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addNode(self, val):
        node = ListNode(val)
        node.next = self

class Solution:
    """给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。"""
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = right = head
        count = 0
        while count < n:
            right = right.next
            count += 1
        # 如果此时右指针为空，那么说明已经遍历完整个链表，也就是说n==链表长度，所以删除倒数第n个结点即删除头结点head。
        if not right:
            return head.next
        # 左右指针同时向右移动，右指针到达链表尾部时，左指针的next即为需要删除的结点
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head


if __name__ == '__main__':
    a=5
    print(a//2)
