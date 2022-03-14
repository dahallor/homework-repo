#include "queue.h"
#include <iostream>




struct Queue* make_queue()
{
    struct Queue* queue = new Queue;
    queue->front = nullptr;
    queue->back = nullptr;
	return queue;
}

void print(struct Queue* queue)
{
	if(queue->front==nullptr)
	{
		std::cout << "Queue Empty" << std::endl;
	}else
	{
		std::cout << "FRONT -> ";
		struct Node* current = queue->front;
		while(current!=nullptr)
		{
			std::cout << current->value << " -> ";
			current=current->next;
		}
		std::cout << "END" << std::endl;
	}
}

int front(struct Queue* queue)
{
    Queue* Q = new Queue;
    if(queue->front == nullptr){
        return 0;
    }
    return queue->front->value;
}

char empty(struct Queue* queue)
{
    if(queue->front == nullptr){
        return 1;
    }
	return 0;
}

void enqueue(struct Queue* queue, int x)
{
    struct Node* temp = new struct Node;
    temp->value = x;
    temp->next = nullptr;

    if(queue->front == nullptr){
       queue->front = temp;
       queue->back = temp;
    }

    else{
        queue->back->next = temp;
        queue->back = temp;
    }
	return;
}

int dequeue(struct Queue* queue)
{
    if(queue->front == nullptr){
        return 0;
    }
    struct Node* temp = queue->front;
    int retVal = 0;
    retVal = temp->value;

    queue->front = queue->front->next;
    delete temp;


	return retVal;
}
