   // 单调栈
    stack<int>
        st;
while (!st.empty() && h[st.top()] <= h[i]) {
  st.pop();
}
st.push(i);

// 循环队列
struct myqueue {
  int data[N];
  int head, rear;
  bool init() {
    head = rear = 0;
    return true;
  }
  int size() { return (rear - head + N) % N; }
  bool empty() {
    if (size() == 0)
      return true;
    else
      return false;
  }
  bool push(int e) {
    if ((rear + 1) % N == head)
      return false;
    data[rear] = e;
    rear = (rear + 1) % N;
    return true;
  }
  bool pop(int &e) {
    if (head == rear)
      return false;
    e = data[head];
    head = (head + 1) % N;
    return true;
  }
  int front() { return data[head]; }
};

// 单调队列
// 最大子序和，限制大小
while (!q.empty() && a[q.back()] > a[i])
  q.pop_back(); // 去尾
while (!q.empty() && q.front() <= i - m)
  q.pop_front(); // 删头

// 优先队列
// 升序队列
priority_queue<int, vector<int>, greater<int>> q;
// 降序队列
priority_queue<int, vector<int>, less<int>> q;

// greater和less是std实现的两个仿函数（就是使一个类的使用看上去像一个函数。其实现就是类中实现一个operator()，这个类就有了类似函数的行为，就是一个仿函数类了）

// heap
int heap[N], len = 0;
void push(int x) {
  heap[++len] = x;
  int i = len;
  while (i > 1 && heap[i] < heap[i / 2]) {
    swap(heap[i], heap[i / 2]);
    i = i / 2;
  }
}
void pop() {
  heap[1] = heap[len--];
  int i = 1;
  while (2 * i <= len) {
    int son = 2 * i;
    if (son < len && heap[son] > heap[son + 1])
      son++;
    if (heap[son] < heap[i]) {
      swap(heap[son], heap[i]);
      i = son;
    } else {
      break;
    }
  }
}
// 尺取
while (i < j) {
  i++;
  j--;
}

// 滑动窗口

// 二分答案
// 最大值的最小 左
while (l < r) {
  int mid = l + r >> 1;
  if (check(mid))
    r = mid;
  else
    l = mid + 1;
}

// 最小值的最大 右
while (l < r) {
  int mid = l + r + 1 >> 1;
  if (check(mid))
    l = mid;
  else
    r = mid - 1;
}

// x or x的后继
int bs(int *a, int n, int x) {
  int left = 0, right = n;
  while (left < right) {
    int mid = left + (right - left) / 2;
    if (a[mid] >= x)
      right = mid;
    else
      left = mid + 1;
  }
  return left;
}
// x or x 的前驱
int bs(int *a, int n, int x) {
  int left = 0, right = n;
  while (left < right) {
    int mid = left + (right - left + 1) / 2;
    if (a[mid] <= x)
      left = mid;
    else
      right = mid - 1;
  }
  return left;
}
// 第一个大于 x的位置：pos = upper_bound(a,a+n,x)-a
// 第一个等于或大于 x：lower_bound
// 第一个与 x 相等：lower_bound()且等于 x
// 最后一个与 x 相等：upper_bound()的前一个且等于 x
// 最后一个等于或小于 x：upper_bound()的前一个
// 最后一个小于 x 的元素: lower_bound()的前一个
// 单调序列中 x 的个数：upper_bound()-lower_bound()
// 最大值最小化，最小值最大化
while (left < right) {
  int ans;
  int mid = left + (right - left) / 2;
  if (check(mid)) {
    ans = mid;
  } else {
  }
}

// 倍增
for (int i - 1; (1 << i) <= n; ++i) {
  for (int s = 1; s <= n2; s++) {
    go[s][i] = go[go[s][i - 1]][i - 1];
  }
}

// 差分
// 一维
d[i] = a[i] - a[i - 1]

       // 不修改区间外的值
       d[l] += x;d[r+1] -= x
a[x] = d[1]+d2] + d[3] + … + d[x]

// 二维
d[i][j] = a[i][j]-a[i-1][j]-a[i][j-1] + a[i-1][j-1]
d[x1][y1] += x;
d[x1][y2 + 1] -= x;
d[x2 + 1][y1] -= x;
d[x2 + 1][y2 + 2] += x

    // 离散化
    // 去重，不去重， 特殊处理
    sort(olda + 1, olda + n + 1);
int cnt = n;
// cnt  = unique(olda + 1, olda + n + 1) - (olda+1);
for (int i = 1; i <= cnt; ++i) {
  newa[i] = lower_bound(olda + 1, olda + n + 1, newa[i]) - olda;
}

// 分组背包二进制优化
int new_n = 0;
for (int i = 1; i <= n; i++) {
  for (int j = 1; j <= m[i]; j <<= 1) {
    m[i] -= j;
    new_c[++new_n] = j * c[i];
    // new_w[new_n] = j * w[i];
  }
  if (m[i]) {
    new_c[++new_n] = m[i] * c[i];
    // new_w[new_n] = m[i] * w[i];
  }
}

// 排列
void dfs(int s, int t) {
  if (s == t) {
    for (int i = 0; i < t; i++) {
      cout << b[i] << " ";
    }
    cout << endl;
    return;
  }
  for (int i = 0; i < t; i++) {
    if (!vis[i]) {
      vis[i] = true;
      b[s] = a[i];
      dfs(s + 1, t);
      vis[i] = false;
    }
  }
}

// 第 k 大
int qs(int left, int right, int k) {
  int mid = a[left + (right - left) / 2];
  int i = left, j = right - 1;
  while (i <= j) {
    while (a[i] < mid)
      ++i;
    while (a[j] > mid)
      --j;
    if (i <= j) {
      swap(a[i], a[j]);
      ++i;
      --j;
    }
  }
  if (left <= j && k <= j)
    return qs(left, j, k);
  if (i < right && k >= i)
    return qs(i, right, k);
}

// 并查集
void init_set() {
  for (int i = 1; i <= N; i++) {
    s[i] = i;
  }
}

// int find_set(int x) { return x == s[x] ? x : find_set(s[x]); }
int find_set(int x) {
  if (x != s[x])
    s[x] = find_set(s[x]);
  return s[x];
}

void merge_set(int x, int y) {
  x = find_set(x);
  y = find_set(y);
  if (x != y)
    s[x] = s[y];
}

// 树状数组
#define lowbit(x) ((x) & -(x))

int tree[N] = {0};
void update(int x, int d) {
  while (x <= N) {
    tree[x] += d;
    x += lowbit(x);
  }
}

int sum(int x) {
  int ans = 0;
  while (x > 0) {
    ans += tree[x];
    x -= lowbit(x);
  }
  return ans;
}
// 线段树
using ll = long long;

const int N = 1e5 + 10;
ll a[N];

// tree[i] 为第 i
// 个节点的值，表示一个线段区间的值，ex：最值，区间和
ll tree[N << 2];
// tag[i]为第i个节点的懒标记，统一记录这个区间的修改
ll tag[N << 2];
ll ls(ll p) { return p << 1; }
ll rs(ll p) { return p << 1 | 1; }
void push_up(ll p) {
  // 区间和
  tree[p] = tree[ls(p)] + tree[rs(p)];
}
void build(ll p, ll pl, ll pr) {
  tag[p] = 0;
  if (pl == pr) {
    tree[p] = a[pl];
    return;
  }
  ll mid = (pl + pr) >> 1;
  build(ls(p), pl, mid);
  build(rs(p), mid + 1, pr);
  // 从下往上传递区间值
  push_up(p);
}

void add_tag(ll p, ll pl, ll pr, ll d) {
  tag[p] += d;
  tree[p] += d * (pr - pl + 1);
}

// 不能覆盖时，传递给子树
void push_down(ll p, ll pl, ll pr) {
  if (tag[p]) {
    ll mid = (pl + pr) >> 1;
    add_tag(ls(p), pl, mid, tag[p]);
    add_tag(rs(p), mid + 1, pr, tag[p]);
    tag[p] = 0;
  }
}

void update(ll L, ll R, ll p, ll pl, ll pr, ll d) {
  if (L <= pl && pr <= R) {
    add_tag(p, pl, pr, d);
    return;
  }
  push_down(p, pl, pr);
  ll mid = (pl + pr) >> 1;
  if (L <= mid)
    update(L, R, ls(p), pl, mid, d);
  if (R > mid)
    update(L, R, rs(p), mid + 1, R, d);
  push_up(p);
}

ll query(ll L, ll R, ll p, ll pl, ll pr) {
  if (pl >= L && pr <= R)
    return tree[p];
  push_down(p, pl, pr);
  ll res = 0;
  ll mid = (pl + pr) >> 1;
  if (L <= mid)
    res += query(L, R, ls(p), pl, mid);
  if (R > mid)
    res += query(L, R, rs(p), mid + 1, pr);
  return res;
}

// LCA
class Solution {
public:
  TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
    if (root == q || root == p || root == NULL)
      return root;
    TreeNode *left = lowestCommonAncestor(root->left, p, q);
    TreeNode *right = lowestCommonAncestor(root->right, p, q);
    if (left != NULL && right != NULL)
      return root;
    if (left == NULL)
      return right;
    return left;
  }
};

// 用来求a,b两点的最短距离， da+db - lca(a,b)

// 快速幂
ll fastPow(ll a, ll n, ll mod) {
  ll ans = 1;
  a %= mod;
  while (n) {
    if (n & 1)
      ans = (ans * a) % mod;
    a = (a * a) % mod;
    n >>= 1;
  }
  return ans;
}

// 进制 HASH
ull BKDRHash(char *s) {
  ull P = 131, H = 0;
  int n = strlen(s);
  for (int i = 0; i < n; i++) {
    H = H * P + s[i] - 'a' + 1;
  }
  return H;
}
// kmp
class Solution {
public:
  void getNext(int *next, const string &s) {
    int j = 0;
    next[0] = 0;
    for (int i = 1; i < s.size(); i++) {
      while (j > 0 && s[i] != s[j]) {
        j = next[j - 1];
      }
      if (s[i] == s[j]) {
        j++;
      }
      next[i] = j;
    }
  }
  int strStr(string haystack, string needle) {
    if (needle.size() == 0) {
      return 0;
    }
    vector<int> next(needle.size());
    getNext(&next[0], needle);
    int j = 0;
    for (int i = 0; i < haystack.size(); i++) {
      while (j > 0 && haystack[i] != needle[j]) {
        j = next[j - 1];
      }
      if (haystack[i] == needle[j]) {
        j++;
      }
      if (j == needle.size()) {
        return (i - needle.size() + 1);
      }
    }
    return -1;
  }
};

// Kruskal
struct Edge {
  int l, r, val;
};
int n = 10001;
vector<int> father(n, -1);
void init() {
  for (int i = 0; i < n; ++i) {
    father[i] = i;
  }
}
int find(int u) { return u == father[u] ? u : father[u] = find(father[u]); }
void join(int u, int v) {
  u = find(u);
  v = find(v);
  if (u == v)
    return;
  father[v] = u;
}
int main() {
  int v, e;
  int v1, v2, val;
  vector<Edge> edges;
  int result_val = 0;
  cin >> v >> e;
  while (e--) {
    cin >> v1 >> v2 >> val;
    edges.push_back({v1, v2, val});
  }
  sort(edges.begin(), edges.end(),
       [](const Edge &a, const Edge &b) { return a.val < b.val; });
  vector<Edge> result; // 存储最小生成树的边
  init();
  for (Edge edge : edges) {
    int x = find(edge.l);
    int y = find(edge.r);
    if (x != y) {
      result.push_back(edge); // 保存最小生成树的边
      result_val += edge.val;
      join(x, y);
    }
  }
  // 打印最小生成树的边
  for (Edge edge : result) {
    cout << edge.l << " - " << edge.r << " : " << edge.val << endl;
  }
  return 0;
}

// dij

// 小顶堆
class mycomparison {
public:
  bool operator()(const pair<int, int> &lhs, const pair<int, int> &rhs) {
    return lhs.second > rhs.second;
  }
};
// 定义一个结构体来表示带权重的边
struct Edge {
  int to;  // 邻接顶点
  int val; // 边的权重

  Edge(int t, int w) : to(t), val(w) {} // 构造函数
};

int main() {
  int n, m, p1, p2, val;
  cin >> n >> m;

  vector<list<Edge>> grid(n + 1);

  for (int i = 0; i < m; i++) {
    cin >> p1 >> p2 >> val;
    // p1 指向 p2，权值为 val
    grid[p1].push_back(Edge(p2, val));
  }

  int start = 1; // 起点
  int end = n;   // 终点

  // 存储从源点到每个节点的最短距离
  std::vector<int> minDist(n + 1, INT_MAX);

  // 记录顶点是否被访问过
  std::vector<bool> visited(n + 1, false);

  // 优先队列中存放 pair<节点，源点到该节点的权值>
  priority_queue<pair<int, int>, vector<pair<int, int>>, mycomparison> pq;

  // 初始化队列，源点到源点的距离为0，所以初始为0
  pq.push(pair<int, int>(start, 0));

  minDist[start] = 0; // 起始点到自身的距离为0

  while (!pq.empty()) {
    // 1. 第一步，选源点到哪个节点近且该节点未被访问过 （通过优先级队列来实现）
    // <节点， 源点到该节点的距离>
    pair<int, int> cur = pq.top();
    pq.pop();

    if (visited[cur.first])
      continue;

    // 2. 第二步，该最近节点被标记访问过
    visited[cur.first] = true;

    // 3. 第三步，更新非访问节点到源点的距离（即更新minDist数组）
    for (Edge edge :
         grid[cur.first]) { // 遍历 cur指向的节点，cur指向的节点为 edge
      // cur指向的节点edge.to，这条边的权值为 edge.val
      if (!visited[edge.to] &&
          minDist[cur.first] + edge.val < minDist[edge.to]) { // 更新minDist
        minDist[edge.to] = minDist[cur.first] + edge.val;
        pq.push(pair<int, int>(edge.to, minDist[edge.to]));
      }
    }
  }

  if (minDist[end] == INT_MAX)
    cout << -1 << endl; // 不能到达终点
  else
    cout << minDist[end] << endl; // 到达终点最短路径
}
// topo

using namespace std;
int main() {
  int m, n, s, t;
  cin >> n >> m;
  vector<int> inDegree(n, 0); // 记录每个文件的入度

  unordered_map<int, vector<int>> umap; // 记录文件依赖关系
  vector<int> result;                   // 记录结果

  while (m--) {
    // s->t，先有s才能有t
    cin >> s >> t;
    inDegree[t]++;        // t的入度加一
    umap[s].push_back(t); // 记录s指向哪些文件
  }
  queue<int> que;
  for (int i = 0; i < n; i++) {
    // 入度为0的文件，可以作为开头，先加入队列
    if (inDegree[i] == 0)
      que.push(i);
    // cout << inDegree[i] << endl;
  }
  // int count = 0;
  while (que.size()) {
    int cur = que.front(); // 当前选中的文件
    que.pop();
    // count++;
    result.push_back(cur);
    vector<int> files = umap[cur]; // 获取该文件指向的文件
    if (files.size()) {            // cur有后续文件
      for (int i = 0; i < files.size(); i++) {
        inDegree[files[i]]--; // cur的指向的文件入度-1
        if (inDegree[files[i]] == 0)
          que.push(files[i]);
      }
    }
  }
  if (result.size() == n) {
    for (int i = 0; i < n - 1; i++)
      cout << result[i] << " ";
    cout << result[n - 1];
  } else
    cout << -1 << endl;
}

// 多源最短路径 floyd
int main() {
  int n, m, p1, p2, val;
  cin >> n >> m;

  vector<vector<vector<int>>> grid(
      n + 1, vector<vector<int>>(
                 n + 1, vector<int>(n + 1, 10005))); // 因为边的最大距离是10^4
  for (int i = 0; i < m; i++) {
    cin >> p1 >> p2 >> val;
    grid[p1][p2][0] = val;
    grid[p2][p1][0] = val; // 注意这里是双向图
  }
  // 开始 floyd
  for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        grid[i][j][k] =
            min(grid[i][j][k - 1], grid[i][k][k - 1] + grid[k][j][k - 1]);
      }
    }
  }
  // 输出结果
  int z, start, end;
  cin >> z;
  while (z--) {
    cin >> start >> end;
    if (grid[start][end][n] == 10005)
      cout << -1 << endl;
    else
      cout << grid[start][end][n] << endl;
  }
}

// prim

int main() {
  int v, e;
  int x, y, k;
  cin >> v >> e;
  vector<vector<int>> grid(v + 1, vector<int>(v + 1, 10001));
  while (e--) {
    cin >> x >> y >> k;
    grid[x][y] = k;
    grid[y][x] = k;
  }

  vector<int> minDist(v + 1, 10001);
  vector<bool> isInTree(v + 1, false);

  // 加上初始化
  vector<int> parent(v + 1, -1);

  for (int i = 1; i < v; i++) {
    int cur = -1;
    int minVal = INT_MAX;
    for (int j = 1; j <= v; j++) {
      if (!isInTree[j] && minDist[j] < minVal) {
        minVal = minDist[j];
        cur = j;
      }
    }

    isInTree[cur] = true;
    for (int j = 1; j <= v; j++) {
      if (!isInTree[j] && grid[cur][j] < minDist[j]) {
        minDist[j] = grid[cur][j];

        parent[j] = cur; // 记录边
      }
    }
  }
  // 输出 最小生成树边的链接情况
  for (int i = 1; i <= v; i++) {
    cout << i << "->" << parent[i] << endl;
  }
}
// bellman-ford
int main() {
  int n, m, p1, p2, val;
  cin >> n >> m;

  vector<vector<int>> grid;

  for (int i = 0; i < m; i++) {
    cin >> p1 >> p2 >> val;
    // p1 指向 p2，权值为 val
    grid.push_back({p1, p2, val});
  }
  int start = 1; // 起点
  int end = n;   // 终点

  vector<int> minDist(n + 1, INT_MAX);
  minDist[start] = 0;
  bool flag = false;
  for (int i = 1; i <= n; i++) { // 这里我们松弛n次，最后一次判断负权回路
    for (vector<int> &side : grid) {
      int from = side[0];
      int to = side[1];
      int price = side[2];
      if (i < n) {
        if (minDist[from] != INT_MAX && minDist[to] > minDist[from] + price)
          minDist[to] = minDist[from] + price;
      } else { // 多加一次松弛判断负权回路
        if (minDist[from] != INT_MAX && minDist[to] > minDist[from] + price)
          flag = true;
      }
    }
  }

  if (flag)
    cout << "circle" << endl;
  else if (minDist[end] == INT_MAX) {
    cout << "unconnected" << endl;
  } else {
    cout << minDist[end] << endl;
  }
}

// Nim
int sum = 0, ans = 0;
for (int i = 0; i < n; i++)
  sum ^= a[i];
if (sum == 0)
  cout << 0 << endl;
else {
  for (int i = 0; i < n; i++) {
    if (sum ^ a[i] <= a[i])
      ans++
  }
  cout << ans << endl;
}

// bash
if (n % (m + 1) == 0) // 后手win
```
