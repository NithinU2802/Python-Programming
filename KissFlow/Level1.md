Expression - (a+b)*c 

      * 
     / \
    +   c
   / \
  a   b


Basic Implementation:
   1. Create Node for each character.
   2. InterConnect with each other.
   3. Then Make postfix traversal.

Create Node:
  
    struct Node {
        char value;
        struct Node* left;
        struct Node* right;
    };

Allocate Memory and Connection:

    struct Node* createNode(char c){
        struct Node* node=(struct Node*)malloc(sizeof(struct Node));
        node->value=c;
        node->left=null;
        node->right=null;
        return node;
    }

Connection Between Nodes:

    struct Node* Create(){
      struct Node* head = createNode('*');
      head->right=createNode('c');
      head->left=createNode('+');
      head->left->left=createNode('a');
      head->left->right=createNode('b');
      return root;
    }

Postfix Expression:

    void Postfix(struct Node* head){
      if(head!=null){
        postfix(head->left);
        printf("%d ",head->value);
        postfix(head->right);
      }
    }

