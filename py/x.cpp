#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  /**
   * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
   *
   *
   * @param nums int整型vector
   * @return int整型
   */
  int maxAscendingSum(vector<int> &nums) {
    // write code here

    int len = nums.size();
    vector<int> dp(len);

    dp[0] = nums[0];

    for (int i = 1; i < len; i++) {
      if (nums[i] < nums[i - 1]) {
        dp[i] = dp[i - 1] + nums[i];
      } else {
        dp[i] = nums[i];
      }
    }

    int ans = -10001;
    for (int i = 0; i < len; i++) {
      ans = max(ans, dp[i]);
    }

    return ans;
  }
};

int main() {
  vector<int> nums = {50, 30, 20};
  Solution s;
  int ans = s.maxAscendingSum(nums);
  std::cout << ans << std::endl;
}
