/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head,int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    (*new_node).data = data;
    (*new_node).next = NULL;
    
    if(head == NULL) { return new_node; }
    
    Node* current = head;
    while((*current).next != NULL) {
        current = (*current).next;
    }
    
    (*current).next = new_node;
    return head;
}