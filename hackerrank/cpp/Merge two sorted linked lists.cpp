/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB) {
    if(headA == NULL) { return headB; }
    if(headB == NULL) { return headA; }
    
    Node* new_head;
    
    if((*headA).data <= (*headB).data) {
        new_head = headA;
        (*new_head).next = MergeLists((*headA).next, headB);
    } else {
        new_head = headB;
        (*new_head).next = MergeLists(headA, (*headB).next);
    }
    
    return new_head;
}