#include "queue.h"
#include <iostream>

struct Queue* make_queue()
{
	return nullptr;
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
	return 0;
}

char empty(struct Queue* queue)
{
	return 0;
}

void enqueue(struct Queue* queue, int x)
{
	return;
}

int dequeue(struct Queue* queue)
{
	return 0;
}
