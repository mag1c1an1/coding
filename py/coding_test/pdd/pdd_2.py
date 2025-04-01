T = int(input())


def solve(n, m, A, B, X):
    # 将B按字典序排序
    B_sorted = sorted(B)
    
    # 统计X中每个位置出现的次数
    position_counts = {}
    for pos in X:
        position_counts[pos] = position_counts.get(pos, 0) + 1
    
    # 按从小到大排序位置
    unique_positions = sorted(position_counts.keys())
    
    # 当前B_sorted的索引
    b_idx = 0
    
    # 记录当前使用到的B中的字符索引
    b_index = 0

    # 对每个位置，分配对应数量的字符
    for pos in unique_positions:
        count = position_counts[pos]
        # 取出B中对应数量的最小字符
        chars_for_pos = B_sorted[b_index:b_index+count]
        b_index += count
        # 使用最小的一个字符进行替换
        A_list[pos-1] = chars_for_pos[0]

    return ''.join(A_list)


    
    
    


for _ in range(T):
    n, m = map(int, input().split())
    A = input().strip()
    B = input().strip()
    X = list(map(int, input().split()))
    b = sorted(B)
    res = solve(n, m, A, B, X)
    print(res)
