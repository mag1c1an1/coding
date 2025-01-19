def exchange(unit):
    match unit:
        case "CNY":
            return 100.0
        case "JPY":
            return 100.0 / 1825 * 100
        case "HKD":
            return 100.0 / 123 * 100  # 港元
        case "EUR":
            return 100.0 / 14 * 100  # 欧元
        case "GBP":
            return 100.0 / 12 * 100  # 英镑
        case "fen":
            return 1.0  # 人民币分
        case "cents":
            return 100.0 / 123  # 港元分
        case "sen":
            return 100.0 / 1825  # 日元分
        case "eurocents":
            return 100.0 / 14  # 欧元分
        case "pence":
            return 100.0 / 12  # 英镑分
        case _:
            return 0.0  # 无效单位返回0


def main():
    n = int(input())
    total = 0.0
    for _ in range(n):
        record = input()
        amount = 0
        unit = ""
        for j, c in enumerate(record):
            if c.isdigit():
                amount = amount * 10 + int(c)
            else:
                unit += c
            if j == len(record) - 1 or (
                j + 1 < len(record) and record[j + 1].isdigit() and unit
            ):
                total += amount * exchange(unit)
                amount = 0
                unit = ""
    print(int(total))


if __name__ == "__main__":
    main()
