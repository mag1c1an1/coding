# fast slow


def main():
    start, n = map(int, input().split())
    d = {}
    lst = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        d[a] = (b, c)
    while True:
        b, c = d[start]
        lst.append(b)
        if c == -1:
            break
        start = c
    assert len(lst) == n
    print(lst[n // 2])

    # # 初始化慢指针和快指针，均指向头节点
    # slow = head_address
    # fast = head_address

    # # 快指针每次走两步，慢指针每次走一步，直到快指针到达链表末尾
    # while fast != "-1" and fast in node_map:
    #     fast = node_map[fast][1]  # 快指针走一步
    #     if fast == "-1" or fast not in node_map:
    #         break  # 快指针到达链表末尾，结束循环
    #     fast = node_map[fast][1]  # 快指针再走一步
    #     slow = node_map[slow][1]  # 慢指针走一步


if __name__ == "__main__":
    main()
