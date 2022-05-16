# 快速乘
def quick_multiple(x, n):
    if x == 0.0: return 0.0
    res = 1
    if n < 0: x, n = 1 / x, -n
    while n:
        if n & 1: res *= x
        x += x
        n >>= 1
    return res


# 快速幂
def quick_bow(x, n):
    if x == 0.0: return 0.0
    res = 1
    if n < 0: x, n = 1 / x, -n
    while n:
        if n & 1: res *= x
        x *= x
        n >>= 1
    return res


if __name__ == '__main__':
    a = quick_bow(3, 4)
    print(a)
    b = quick_multiple(3, 4)
    print(b)