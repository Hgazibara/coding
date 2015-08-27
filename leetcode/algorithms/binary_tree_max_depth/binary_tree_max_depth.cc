class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }

        return max(
            this->maxDepth(root->left),
            this->maxDepth(root->right)
        ) + 1;
    }
};
