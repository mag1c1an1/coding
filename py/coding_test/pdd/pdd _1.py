from functools import lru_cache

# 手动缓存
is_lucky_cache = {}

def is_lucky_number(num):
    """判断一个数是否是幸运数字（包含连续子串且该子串是3的倍数）"""
    # 检查缓存
    if num in is_lucky_cache:
        return is_lucky_cache[num]
    
    # 特殊情况：如果数字本身是3的倍数，直接返回True
    if num % 3 == 0:
        is_lucky_cache[num] = True
        return True
    
    num_str = str(num)
    n = len(num_str)
    
    # 遍历所有可能的子串，使用O(n²)检查
    for i in range(n):
        # 初始化当前子串的值
        val = 0
        for j in range(i, n):
            # 累加数字到子串
            val = val * 10 + int(num_str[j])
            # 检查子串是否是3的倍数，不考虑前导0的子串
            if val % 3 == 0 and (i == 0 or num_str[i] != '0'):
                is_lucky_cache[num] = True
                return True
    
    is_lucky_cache[num] = False
    return False

# 手动缓存
count_cache = {}

def count_lucky_in_range(start, end):
    """计算范围内的幸运数字个数"""
    # 检查缓存
    key = (start, end)
    if key in count_cache:
        return count_cache[key]
    
    count = 0
    for num in range(start, end + 1):
        if is_lucky_number(num):
            count += 1
    
    # 存入缓存
    count_cache[key] = count
    return count

def main():
    # 读取测试样例数量
    T = int(input())
    
    # 处理每个测试样例
    for _ in range(T):
        # 读取输入
        L, R = map(int, input().split())
        
        result = count_lucky_in_range(L, R)
        print(result)

if __name__ == "__main__":
    main()
