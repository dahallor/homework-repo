//Mark Boady - CS520
//Heap Data Structure

#ifndef _HEAP_H_
#define _HEAP_H_
#include<vector>

//*********Functions Required to make a heap***********
//Heapsort Sort
//Sort using a heap data structure
void heap_sort(int* Array, int size);
//The Heap data structure
struct Heap {
    int* data;
    int max_size;
    int current_size;
    std::vector<int> vect = {};
    
};
//Make a new Heap
struct Heap* makenull(int capacity);
//Is the heap empty?
char empty(struct Heap* H);
//What is the min?
int min(struct Heap* H);
//Delete the min
void deletemin(struct Heap* H);
//Downheap a value at index i
void downheap(struct Heap* H, int i);
//Insert a new value
void insert(int x, struct Heap* H);
//Upheap a value at index i
void upheap(struct Heap* H, int i);
//Get Index of Parent
int parent(int n);
//Get index of Left Child
int left_child(int n);
//Get index of Right Child
int right_child(int n);
//Swap i and j in heap
void swap(struct Heap* H, int i, int j);
//Just to help debug
//You can have this do whatever you want.
//We suggest you have a way to print the heap
//So you can test it when you get errors
void print_heap(struct Heap* H);

#endif