#include <iostream>
#include "queue.h"

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
