#ifndef BST_H_INCLUDED
#define BST_H_INCLUDED

struct Node{

};

struct BST{

};

BST* makeBST();

//Get Root
//This function returns a pointer to the root node
//It will be useful to implement later functions
//You may assume T is not null
Node* getRoot(BST* T);

//Primary Operations
//Insert value into tree
void insert(int value, BST* T);

//Find a value in the tree
bool find(int value, BST* T);

//Delete a value
void delete_from_tree(int value, BST* T);

//Find the min of the tree
int min(BST* T);

//Prints
//These will print directly to cout.
//Print Inorder
void inorder(BST* T);
//Prints Preorder
void preorder(BST* T);
//Prints Postorder
void postorder(BST* T);

//Determine the height
int height(BST* T);

//Helpers needed for recursion
void inorder_walker(Node* current);
void preorder_walker(Node* current);
void postorder_walker(Node* current);

//Insert Helper
Node* insert_value(int v, Node* current);
//Find Helper
bool find_value(int value, Node* current);
//Find the min starting at node current
int find_min(Node* current);
//Find Height of a Node
int node_height(Node* current);
//Delete Helper
Node* delete_value(int v, Node* current);
Node* delete_node(Node* current);



#endif // BST_H_INCLUDED
