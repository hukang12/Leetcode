

class Solution:
    def divide(self, a: int, b: int) -> int:
        a_is_neg = 1 if a < 0 else 0
        b_is_neg = 1 if b < 0 else 0
        abs_a, abs_b = abs(a), abs(b)
        div_res = 0
        while abs_a:
            if abs_a >= abs_b:
                div_res += 1
                abs_a -= abs_b
            else:
                break

        if a_is_neg + b_is_neg == 1:
            return -div_res
        else:
            return div_res


if __name__ == '__main__':
    solu = Solution()
    a, b = input("请输入两个整数：\n").split()
    a, b = int(a), int(b)

    res = solu.divide(a, b)
    print(res)
