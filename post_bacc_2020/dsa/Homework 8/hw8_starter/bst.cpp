//Mark Boady
//Drexel 2020

#include "bst.h"
#include <cstdlib>
#include <iostream>

BST* makeBST()
{
    BST* B = new BST();
    B->root = NULL;
    return B;
}

Node* getRoot(BST* T)
{
    return T->root;
}

void insert(int value, BST* T)
{
    T->root = insert_value(value,T->root);
}


bool find(int value, BST* T)
{
    return find_value(value, T->root);
}

void delete_from_tree(int value, BST* T)
{
    T->root = delete_value(value,T->root);
}

int min(BST* T)
{
    return find_min(T->root);
}

void inorder(BST* T)
{
    inorder_walker(T->root);
    std::cout << std::endl;
}

void preorder(BST* T)
{
    preorder_walker(T->root);
    std::cout << std::endl;
}

void postorder(BST* T)
{
    postorder_walker(T->root);
    std::cout << std::endl;
}

int height(BST* T)
{
    return node_height(T->root);
}


//You have to start implementing from here down

//Do a walk starting at the node given
//Print the results to cout
//Print N for nulls
//Print a space after each value
//Print out an N for null positions
void inorder_walker(Node* current)
{
    //Implement me
    return;
}
void preorder_walker(Node* current)
{
    //Implement Me
    return;
}
void postorder_walker(Node* current)
{
    //Implement Me
    return;

}

//Insert value v starting at node current
Node* insert_value(int v, Node* current)
{
    //Implement me
    return current;
}

//Find value starting at current node
bool find_value(int value, Node* current)
{
    //Implement Me
    return false;
}

//Find the min of the tree starting at current node
//Return -1 on current is null
int find_min(Node* current)
{
    //Implement Me
    return -1;
}

//Determine the node height of the current node
//Hint: The height of a null is -1
int node_height(Node* current)
{
    //Implement Me
    return -1;
}

//I will provide you with delete
Node* delete_value(int v, Node* current)
{
    if(current==NULL){
        return NULL;
    }else if(current->value == v){
        Node* x = delete_node(current);
        return x;
    }else if(current->value > v){
        current->left=delete_value(v,current->left);
        return current;
    }else{
        current->right=delete_value(v,current->right);
        return current;
    }
}
Node* delete_node(Node* current)
{
    if(current->left == NULL){
        return current->right;
    }
    if(current->right==NULL)
    {
        return current->left;
    }
    int minval = find_min(current->right);
    current->value = minval;
    current->right = delete_value(minval,current->right);
    return current;
}
