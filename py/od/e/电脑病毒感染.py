def main():
    INF = float("inf")
    N = int(input())
    M = int(input())
    times = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        times.append((u - 1, v - 1, w))
    K = int(input()) - 1

    def network_delay_time(times):
        dist = [INF] * N
        dist[K] = 0
        for _ in range(N):
            for u, v, w in times:
                dist[v] = min(dist[v], dist[u] + w)
        max_wait = max(dist)
        return max_wait if max_wait < INF else -1

    print(network_delay_time(times))


if __name__ == "__main__":
    main()
