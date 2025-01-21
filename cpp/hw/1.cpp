#include <queue>
using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  // 1
  int countNodes(TreeNode *root) {
    if (root == nullptr)
      return 0;
    queue<TreeNode *> q;
    q.push(root);
    int res = 1;
    while (!q.empty()) {
      auto *x = q.front();
      q.pop();
      if (x->left) {
        q.push(x->left);
        res++;
      }
      if (x->right) {
        q.push(x->right);
        res++;
      }
    }
    return res;
  }
};
