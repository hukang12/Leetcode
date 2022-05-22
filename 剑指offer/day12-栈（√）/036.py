# -- coding: utf-8 --
# @Time : 2022/5/19 10:06
# @Author : HK
# @File : 036.py
from collections import deque

class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        tmp = None
        stack = deque([])
        for t in tokens:
            if len(stack) >= 2 and t in ["+","-","*","/"]:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == "+": tmp = n1+n2
                if t == "-": tmp = n1-n2
                if t == "*": tmp = n1*n2
                if t == "/": tmp = int(n1/n2)
                stack.append(tmp)
                continue
            stack.append(int(t))
        if tmp is None:
            # 没有操作
            return 0
        else:
            return tmp



if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    tokens = ["4","13","5","/","+"]
    tokens = ["4"]
    s = Solution()
    res = s.evalRPN(tokens)
    print(res)
    print(6/10)
    print(6//10)
    print(6//-10)
    print(6/-10)
    print(int(6/-10))
