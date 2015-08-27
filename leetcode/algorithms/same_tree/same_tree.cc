class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL || q == NULL) {
            return p == NULL && q == NULL;
        }

        if (p->val != q->val) {
            return false;
        }

        bool is_left_same = this->isSameTree(p->left, q->left);
        bool is_right_same = this->isSameTree(p->right, q->right);

        return is_left_same and is_right_same;
    }
};
