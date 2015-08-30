class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (node == NULL) {
            return node;
        }

        map<UndirectedGraphNode*, UndirectedGraphNode*> clones;

        queue<UndirectedGraphNode*> q;
        q.push(node);

        UndirectedGraphNode* head = new UndirectedGraphNode(node->label);
        clones[node] = head;

        while (!q.empty()) {
            UndirectedGraphNode* top = q.front();
            q.pop();

            for (int i = 0; i < top->neighbors.size(); ++i) {
                UndirectedGraphNode* other = top->neighbors[i];
                if (clones.count(other) == 0) {
                    UndirectedGraphNode* new_other = new UndirectedGraphNode(other->label);
                    clones[top]->neighbors.push_back(&new_other);
                    clones[other] = new_other;
                    q.push(other);
                } else {
                    clones[top]->neighbors->push_back(clones[other]);
                }
            }
        }

        return head;
    }
};
