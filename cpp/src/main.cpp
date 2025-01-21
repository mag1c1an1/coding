#include <stack>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  /**
   * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
   *
   * 每日温度
   * @param dailyTemperatures int整型vector
   * @return int整型vector
   */
  vector<int> temperatures(vector<int> &dailyTemperatures) {
    // write code here

    auto n = dailyTemperatures.size();
    vector<int> res(n);

    stack<int> stk;

    for (int i = 0; i < n; i++) {
      while (!stk.empty() && dailyTemperatures[stk.top()] < dailyTemperatures[i]) {
        auto t = stk.top();
        stk.pop();
        res[t] = i - t;
      }
      stk.push(i);
    }

    return res;
  }
};

int main() {
  Solution s;
  vector<int> v{2, 4, 5, 9, 10, 0, 9};
  auto r = s.temperatures(v);
  for (auto x : r) {
    std::cout << x << std::endl;
  }
}