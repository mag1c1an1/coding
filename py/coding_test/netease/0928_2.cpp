#include <iostream>
#include <string>
using namespace std;

// 给一个字符串x代表一个数字，x的长度小于等于一百万。求一个最小的y（可能超过long的表示范围且y必须大于等于0），使得x加上y是回文串。
using namespace std;

int main() {
  string s;
  cin >> s;
  int n = s.size();

  auto sub = [&](string a, string b) -> string {
    int m = a.size();
    string ans;
    for (int i = m - 1; i >= 0; i--) {
      int d1 = a[i] - '0';
      int d2 = b[i] - '0';
      if (d1 < d2) {
        d1 = d1 + 10;
        a[i - 1]--;
      }
      ans += (char)(d1 - d2 + '0');
    }
    reverse(ans.begin(), ans.end());
    return ans;
  };

  auto add = [&](string a) -> string {
    int progress = 1;
    int m = a.size();
    for (int i = m - 1; i >= 0; i--) {
      int digit = a[i] - '0';
      digit += progress;
      progress = digit / 10;
      digit %= 10;
      a[i] = (char)(digit + '0');
    }
    if (progress == 1) {
      a = "1" + a;
    }
    return a;
  };

  string left = s.substr(0, n / 2);
  string right = s.substr(n - n / 2);
  reverse(left.begin(), left.end());
  if (left == right) {
    cout << 0 << "\n";
    return 0;
  }

  if (left < right) {
    left = s.substr(0, (n + 1) / 2);
    left = add(left);
    string right = left.substr(0, n / 2);
    reverse(right.begin(), right.end());
    string after = left + right;
    string ans = sub(after, s);
    int idx = 0;
    while (idx < ans.size() && ans[idx] == '0') {
      idx++;
    }
    cout << ans.substr(idx) << "\n";

  } else {
    string ans = sub(left, right);
    int idx = 0;
    while (idx < ans.size() && ans[idx] == '0') {
      idx++;
    }
    cout << ans.substr(idx) << "\n";
  }
}