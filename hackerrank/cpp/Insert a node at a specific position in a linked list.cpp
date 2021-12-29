/*
  Insert Node at a given position in a linked list 
  The linked list will not be empty and position will always be valid
  First element in the linked list is at position 0
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* InsertNth(Node *head, int data, int position) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    (*new_node).data = data;
    (*new_node).next = NULL;    
    
    if(head == NULL || position == 0) {
        (*new_node).next = head;
        return new_node;
    }
    
    Node* current = head;
    while(position > 1) {
        current = (*current).next;
        --position;
    }
    
    (*new_node).next = (*current).next;
    (*current).next = new_node;
    
    return head;
}