# -- coding: utf-8 --
# @Time : 2022/5/18 16:55
# @Author : HK
# @File : 029.py

def insert(li:list, in_num):
    min_num = 1e6
    min_id = -1
    for i in range(len(li)):
        num = li[i]
        tmp = num-in_num
        if abs(tmp) == abs(min_num) and tmp<0:
            if tmp < 0 or min_num >= 0:
                min_num = tmp
                min_id = i
        if abs(tmp) < abs(min_num):
            if tmp<0 or min_num >= 0:
                min_num = tmp
                min_id = i

    print(min_num, min_id)
    if min_num>0:
        li.insert(min_id, in_num)
    else:
        li.insert(min_id + 1, in_num)
    print(li)

if __name__ == '__main__':
    a = [1]
    b = -1
    insert(a,b)
    a = [1,3,3]
    b = 4
    insert(a, b)
    a = [-4, -3, 1, 3, 4, 10, ]
    b = -1
    insert(a, b)
    a = {1:0}
