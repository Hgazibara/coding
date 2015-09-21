class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_sum = INT_MIN;
        findMaxPathSum(root, max_sum);
        return max_sum;
    }

    int findMaxPathSum(TreeNode* node, int& max_sum) {
        if (node == NULL) {
            return 0;
        }

        int leftPathSum = findMaxPathSum(node->left, max_sum);
        int rightPathSum = findMaxPathSum(node->right, max_sum);

        int currentMax = max(node->val, max(leftPathSum, rightPathSum) + node->val);
        max_sum = max(max_sum, max(currentMax, leftPathSum + node->val + rightPathSum));

        return currentMax;
    }
};
