# -- coding: utf-8 --
# @Time : 2022/5/19 10:35
# @Author : HK
# @File : 037.py
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        stack = deque([])
        i = 0
        while i < len(asteroids):
            ast = asteroids[i]
            if stack and stack[len(stack)-1] > 0 and ast < 0:
                last = stack[len(stack)-1]
                if last > -ast:
                    i += 1
                elif last == -ast:
                    i += 1
                    stack.pop()
                else:
                    stack.pop()
                continue
            stack.append(ast)
            i += 1

        return list(stack)




if __name__ == '__main__':
    str = input("数组:\n").split()
    arr = [int(a) for a in str]
    s = Solution()
    res = s.asteroidCollision(arr)
    print(res)