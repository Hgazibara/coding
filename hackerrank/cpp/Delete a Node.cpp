/*
  Delete Node at a given position in a linked list 
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Delete(Node *head, int position) {
    if(position == 0) { return (*head).next; }
    
    Node* current = head;
    while(position > 1) {
        current = (*current).next;
        --position;
    }
    
    Node* deleted = (*current).next;
    (*current).next = (*current).next->next;
    free(deleted);
    
    return head;
}