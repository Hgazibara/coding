/*
  Get Nth element from the end in a linked list of integers
  Number of elements in the list will always be greater than N.
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
int GetNode(Node *head,int positionFromTail) {
    Node* first = head;
    Node* second = head;
    
    while(positionFromTail > 0) {
        second = (*second).next;
        --positionFromTail;
    }
    
    while((*second).next != NULL) {
        second = (*second).next;
        first = (*first).next;
    }
    
    return (*first).data;
}