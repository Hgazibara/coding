class Solution {
public:
    ListNode* sortList(ListNode* head) {
        mergeSort(&head);
        return head;
    }

    void mergeSort(ListNode** root) {
        ListNode* head = *root;

        if (head == NULL || head->next == NULL) {
            return;
        }

        ListNode* left_part;
        ListNode* right_part;

        splitList(head, &left_part, &right_part);

        mergeSort(&left_part);
        mergeSort(&right_part);

        *root = mergeParts(left_part, right_part);
    }

    void splitList(ListNode*head, ListNode** left_part, ListNode** right_part) {
        if (head == NULL || head->next == NULL) {
            *left_part = head;
            *right_part = NULL;
            return;
        }

        ListNode* left = head;
        ListNode* right = head;

        while (right != NULL && right->next != NULL) {
            right = right->next->next;
            if (right == NULL) {
                break;
            }
            left = left->next;
        }

        *left_part = head;
        *right_part = left->next;
        left->next = NULL;
    }

    ListNode* mergeParts(ListNode* left_part, ListNode* right_part) {
        ListNode* head = new ListNode(-1);
        ListNode* node = head;

        while (left_part || right_part) {
            if (left_part == NULL) {
                node->next = right_part;
                break;
            }
            if (right_part == NULL) {
                node->next = left_part;
                break;
            }
            if (left_part->val < right_part->val) {
                node->next = left_part;
                left_part = left_part->next;
            } else {
                node->next = right_part;
                right_part = right_part->next;
            }

            node = node->next;
        }

        return head->next;
    }
};
