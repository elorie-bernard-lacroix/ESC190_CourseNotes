#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// implement heap that can store integer values in C
// make sure to realloc if you run out of space
// implement the c file, the header file and testing code
// show TA that you can compile and debug your heap in VS code

typedef struct heap {
    int *data;
    int size;
    int capacity;
} heap;


int get_left_child_index(int parent_index) {
    return 2 * parent_index;
}
int get_right_child_index(int parent_index) {
    return 2 * parent_index + 1;
}
int get_parent_index(int child_index) {
    return child_index / 2;
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int has_left_child(int index, int size) {
    return get_left_child_index(index) <= size;
}
int has_right_child(int index, int size) {
    return get_right_child_index(index) <= size;
}
int has_parent(int index) {
    return get_parent_index(index) >= 1;
}

int left_child(int index, heap *h) {
    return h->data[get_left_child_index(index)];
}
int right_child(int index, heap *h) {
    return h->data[get_right_child_index(index)];
}
int parent(int index, heap *h) {
    return h->data[get_parent_index(index)];
}

void heapify_up(heap *h) {
    int index = h->size;
    while (has_parent(index) && parent(index, h) > h->data[index]) {
        swap(&h->data[index], &h->data[get_parent_index(index)]);
        index = get_parent_index(index);
    }
}

void heapify_down(heap *h) {
    int index = 1;
    while (has_left_child(index, h->size)) {
        int smaller_child_index = get_left_child_index(index);
        if (has_right_child(index, h->size) && right_child(index, h) < left_child(index, h)) {
            smaller_child_index = get_right_child_index(index);
        }
        if (h->data[index] < h->data[smaller_child_index]) {
            break;
        } else {
            swap(&h->data[index], &h->data[smaller_child_index]);
        }
        index = smaller_child_index;
    }
}

void ensure_extra_capacity(heap *h) {
    if (h->size == h->capacity) {
        h->capacity *= 2;
        h->data = realloc(h->data, h->capacity * sizeof(int));
    }
}

void insert(heap *h, int value) {
    ensure_extra_capacity(h);
    h->data[h->size + 1] = value;
    h->size++;
    heapify_up(h);
}


