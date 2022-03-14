#include <iostream>
#include <algorithm>
#include "heap.h"


struct Heap* H;
int minValue = 0;


void insert(int x, struct Heap* H);
void print_heap(struct Heap* H);
int min(struct Heap* H);
void swap(struct Heap* H, int i, int j);
int parent(int n);
int left_child(int n);
int right_child(int n);
void deletemin(struct Heap* H);
char empty(struct Heap* H);

void heap_sort(int* Array, int size) {

	H = makenull(size);

	for (int i = 0; i < size; i++) {
		int x = Array[i];
		insert(x, H);
		int parentIndex = parent(i);
		if (H->vect[i] < H->vect[parentIndex]) {
			upheap(H, i);
		}

	}


	char answer = empty(H);
	while (answer != 89) {
		int minValue = min(H);

		int iterations = 0;
		int minIndex;
		while (1) {
			if (minValue == H->vect[iterations]) {
				minIndex = iterations;
				break;
			}
			iterations++;
		}
		swap(H, minIndex, H->vect.size()-1);
		deletemin(H);
		for (int i = 0; i < H->current_size; i++) {
			int parentIndex = parent(i);
			if (H->vect[parentIndex] > H->vect[i]) {
				downheap(H, parentIndex);

			}

		}
		answer = empty(H);
	}



}

struct Heap* makenull(int capacity) {
	Heap* H = new Heap();
	H->max_size = capacity;
	H->current_size = 0;
	std::vector<int> vect = {};
	return H;
}


void insert(int x, struct Heap* H) {
	H->vect.push_back(x);
	H->current_size = H->current_size + 1;
}

int min(struct Heap* H) {
	for (int i = 0; i < H->current_size; i++) {
		if (i == 0) {
			minValue = H->vect[i];
		}
		if (i > 0 && H->vect[i] < minValue) {
			minValue = H->vect[i];
		}
	}
	return minValue;
}

void swap(struct Heap* H, int i, int j) {
	int temp = H->vect[i];
	H->vect[i] = H->vect[j];
	H->vect[j] = temp;

}

void print_heap(struct Heap* H)
{
	printf("Heap Current Size: %d\n", H->current_size);
	printf("Heap Max Size: %d\n", H->max_size);
	printf("Contents:\n");
	for (int i = 0; i < H->current_size; i++)
	{
		int parentIndex = parent(i);
		printf("parent: %d i: %d number: %d\n", parentIndex, i, H->vect[i]);
	}
	printf("\n");
}

int parent(int n) {
	int parentNode = std::floor((n-1)/2);
	return parentNode;
}

int left_child(int n) {
	int left = (n + 1) * 2 - 1;
	return left;
}

int right_child(int n) {
	int right = (n+1) * 2;
	return right;
}

void deletemin(struct Heap* H) {
	H->vect.pop_back();
	H->current_size = H->current_size - 1;

}

char empty(struct Heap* H) {
	char answer;
	if (H->current_size == 0) {
		answer = 'Y';
		return answer;
	}
	else {
		answer = 'N';
		return answer;
	}
}

void upheap(struct Heap* H, int i) {
	int parentIndex = parent(i);
	while (H->vect[i] < H->vect[parentIndex]) {
		swap(H, i, parentIndex);
		i = parentIndex;
		parentIndex = parent(i);

	}
}

void downheap(struct Heap* H, int i) {
	int leftChildIndex = left_child(i);
	int rightChildIndex = right_child(i);

	
	if (rightChildIndex < H->current_size) {
		if (H->vect[leftChildIndex] < H->vect[rightChildIndex]) {
			swap(H, i, leftChildIndex);
		}
		else {
			swap(H, i, rightChildIndex);

		}
	}

		


	
}
