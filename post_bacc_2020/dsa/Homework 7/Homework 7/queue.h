#ifndef QUEUE_H_INCLUDED
#define QUEUE_H_INCLUDED


struct Node {
    int value;
    Node* next;
};
struct Queue {
    Node* front;
    Node* back;
};

void enqueue(struct Queue* queue, int x);
int dequeue(struct Queue* queue);

char empty(struct Queue* queue);
struct Queue* make_queue();
void print(struct Queue* queue);
int front(struct Queue* queue);
void josephus(int n, int m);




#endif // QUEUE_H_INCLUDED
