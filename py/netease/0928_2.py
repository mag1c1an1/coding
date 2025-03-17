"""
给一个字符串x代表一个数字，x的长度小于等于一百万。求一个最小的y（可能超过long的表示范围且y必须大于等于0），使得x加上y是回文串。
"""


def main():
    s = input().strip()
    n = len(s)

    # 左右一样
    left = s[: n // 2]
    right = s[n - n // 2 :]
    left_reversed = left[::-1]
    if left_reversed == right:
        print(0)
    elif left_reversed < right:
        left = s[: (n + 1) // 2]
        left = str(int(left) + 1)
        right = left[: n // 2][::-1]
        after = left + right
        ans = int(after) - int(s)
        print(ans)
    else:
        print(int(left_reversed) - int(right))


if __name__ == "__main__":
    main()
