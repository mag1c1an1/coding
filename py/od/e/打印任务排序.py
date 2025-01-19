def main():
    priority_list = list(map(int, input().split(",")))
    task_list = [(i, priority_list[i]) for i in range(len(priority_list))]

    sort = sorted(task_list, key=lambda x: -x[1])
    # task_list.sort(key=lambda x: -x[1])
    d = {}

    for i, v in enumerate(sort):
        d[v] = i

    ans = []
    for t in task_list:
        ans.append(d[t])

    # curr = 0
    # print_order = []
    # while curr < len(task_list):
    #     for i in range(len(task_list)):
    #         if task_list[i][0] == curr:
    #             print_order.append(i)
    #     curr += 1
    print(",".join(map(str, ans)))


if __name__ == "__main__":
    main()
