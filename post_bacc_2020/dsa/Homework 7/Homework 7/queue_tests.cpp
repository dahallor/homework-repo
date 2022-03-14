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

	std::cout << "Press any key to proceed to the Josephus Problem" << std::endl;
	std::cin.ignore();

    int n;
    int m;

    std::cout << "Enter Number of People(N):" << std::endl;
    std::cin >> n;
    std::cout << "Enter Person of Eliminate(M):" << std::endl;
    std::cin >> m;

    josephus(n, m);

	return 0;
}

void josephus(int n, int m)
{
    std::cout << "Order Eliminated:" << std::endl;
    struct Queue* Q = make_queue();
    for(int i = 0; i < n; i++){
        enqueue(Q, i);
    }
    while(empty(Q)!=1)
	{
        for(int i = 0; i < m-1; i++){
            int val = dequeue(Q);
            enqueue(Q, val);
        }
		std::cout << front(Q) << " ";
		dequeue(Q);

	}

}
