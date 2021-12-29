/*
  Reverse a linked list and return pointer to the head
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Reverse(Node *head) {
    if(head == NULL) { return head; }
    
    Node *prev, *curr, *next;
    prev = NULL;
    curr = head;
    
    while(curr != NULL) {
        next = (*curr).next;
        (*curr).next = prev;
        prev = curr;
        curr = next;
    }
    
    return prev;
}