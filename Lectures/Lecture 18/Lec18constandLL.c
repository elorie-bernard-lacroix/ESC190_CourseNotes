#include <stdlib.h>
#include <stdio.h>

typedef struct node{
    int data;
    struct node *next;
} node;

typedef struct LL{
    node *head;
    int size;
} LL;

void create_node(node **p_n, int data) {
    *p_n = (node*)malloc(sizeof(node));
    (*p_n)->next = NULL;
    (*p_n)->data = data;
}

void create_LL_from_data(LL **p_LL, int *data_arr, int size) {
    *p_LL = (LL*)malloc(sizeof(LL));
    (*p_LL)->size = 0;

    node* tail = 0;
    for(int i = 0; i <size; i++) {
        node *n;
        create_node(&n, data_arr[i]); // n is a pointer to a node with data = data[i], next = NULL
        if (tail == 0) {
            (*p_LL)->head = n;
        } else {
            tail->next = n;
        }
        tail = n;
        (*p_LL)->size++;
    }
}

char* p_c = (char*)malloc(sizeof(char)); // allowed to change p_c, but not *p_c 
                                                // makes it the same as a python string
                                                // ie. you can change the string but not elements (chars) in the string
*p_c = 0; // compilation error
p_c = "hello"; // fine

char *str = "hello"; // warning, converting a const char* to char*
str[0] = 'H'; // not a compiler error, but undefined behaviour

int main() {
    int a = 42;
    int arr[100];
    int *p_a;
    // want to be able to store an int at address p_a
    p_a = (int*)malloc(sizeof(int));
}
