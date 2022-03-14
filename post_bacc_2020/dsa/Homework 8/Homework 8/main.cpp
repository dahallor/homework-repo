//Mark Boady
//Drexel 2020

//Tests for Binary Search Tree

#include "bst.h"
#include <iostream> //For printing
#include <cstdlib> //For null pointers
#include <iomanip> //For formatting
#include <cstdlib> //For Random Numbers
#include <ctime> //To find out what time it is
void test_insert(int v, BST* B);
void test_delete(int v, BST* B);
int single_experiment(int n);
void run_experiment();

int main(){
    //Set up the random number generator
    srand(time(0));

    //First we do some simple examples.
    BST* B = makeBST();
    //Insert some numbers to make an expected tree
    test_insert(6,B);
    test_insert(4,B);
    test_insert(1,B);
    test_insert(10,B);
    test_insert(8,B);
    test_insert(5,B);
    test_insert(12,B);
    //Check the height
    std::cout << "The Tree Height is " << height(B) << std::endl;
    //Check find
    for(int i=0; i < 13; i++)
    {
        std::cout << "Is " << i << " in the tree? " << std::endl;
        std::cout << find(i,B) << std::endl;
    }
    //Delete the values in order
    test_delete(6,B);
    test_delete(4,B);
    test_delete(1,B);
    test_delete(10,B);
    test_delete(8,B);
    test_delete(5,B);
    test_delete(12,B);

    //Implement this once you have
    //Everything else working
    run_experiment();
    return 0;
}

void test_insert(int v, BST* B)
{
    insert(v,B);
    std::cout <<"Tree After Insert of " << v << std::endl;
    std::cout <<"Inorder:"<<std::endl;
    inorder(B);
    std::cout <<"Preorder:"<<std::endl;
    preorder(B);
    std::cout <<"Postorder:"<<std::endl;
    postorder(B);
}
void test_delete(int v, BST* B)
{
    delete_from_tree(v,B);
    std::cout <<"Tree After Delete of " << v << std::endl;
    std::cout <<"Inorder:"<<std::endl;
    inorder(B);
    std::cout <<"Preorder:"<<std::endl;
    preorder(B);
    std::cout <<"Postorder:"<<std::endl;
    postorder(B);
}

//****Time to Run Your Experiment
void run_experiment()
{
    std::cout << "Experiments" << std::endl;
    std::cout << "|  N  |  T1  |  T2  |  T3  |  T4  |  T5  | Average |";
    std::cout << std::endl;
    int n=2;
    for(int i=1; i < 11; i++)
    {
        //Print the Row
        std::cout << "|"
            << std::left
            << std::setw(5)
            << std::setfill(' ')
            << n;
        //Run 5 Tests
        float avg=0;
        for(int j=0; j < 5; j++)
        {
            int res = single_experiment(n);
            std::cout << "|"
                << std::left
                << std::setw(6)
                << std::setfill(' ')
                << res;
            avg=avg+static_cast<float>(res);
        }
        std::cout << "|"
            << std::left
            << std::setw(9)
            << std::setfill(' ')
            << (avg/5);
        //End
        std::cout << "|" << std::endl;
        n = n * 2;
    }
}

//Have this function run 1 test
//Generate a random tree with n elements
//and return it's height
//This function should insert n random numbers
//into a BST.
//Then return the height of the tree
int single_experiment(int n)
{
   //Generate n random integers
   //Insert into a new tree
   //return the height of the tree
   return 0;
}
