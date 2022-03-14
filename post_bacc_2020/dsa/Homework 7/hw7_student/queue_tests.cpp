//Mark Boady
//Some Basic Queue Tests

//These working DOES NOT mean your code works.
//It just means you have no big obvious mistakes.

#include <iostream>
#include "queue.h"

int main()
{
	//Create a new Queue
	struct Queue * Q = make_queue();
	std::cout << "If correct, the next line should say \"Queue Empty\"" << std::endl;
	print(Q);
	//We will now add Elements to the queue.
	//This will have a very predicable order.
	for(int i=0; i < 10; i++)
	{
		std::cout << "Adding "<< i << " to the end of the queue." << std::endl;
        enqueue(Q,i);
		print(Q);
	}
	//Now lets delete all the values
	int predict=0;
	while(empty(Q)!=1)
	{
		printf("We expect Front and Dequeue to return %d\n",predict);
		printf("The current front of the Queue is %d\n",front(Q));
		int temp = dequeue(Q);
		printf("Dequeue returned %d\n",temp);
		print(Q);
		predict+=1;
	}
	return 0;
}
