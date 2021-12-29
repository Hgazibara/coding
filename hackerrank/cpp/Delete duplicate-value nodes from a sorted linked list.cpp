/*
  Remove all duplicate elements from a sorted linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* RemoveDuplicates(Node *head) {
    Node* current = head;
    
    while((*current).next != NULL) {
        Node* ahead = (*current).next;
        
        while(ahead != NULL && (*ahead).data == (*current).data) {
            ahead = (*ahead).next;
        }
        
        (*current).next = ahead;
        
        if(ahead != NULL) {
            current = (*current).next;
        } else {
            break;
        }
    }
    
    return head;
}