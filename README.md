# Course Summary

## Fundamentals of C Programming
### Boilerplate Code
```C
#include<stdio.h>                         //header files
int main()                               //main function
{
  return(0);                              //returning value to int main()
}
```

### Comments

```C
// This is a single line comment

/* This is
a multi-line
comment
*/
```

### Functions
```C
return_type function_name(parameter variable_name)
{
  //code
  return [value that matches return_type]
}
```
Note: when using input parameters, teh function will make a copy of them (and therefore uses a local reference frame). If we want to change the original variable, we use its pointer as a parameter and reference the value through the pointer.

### Data Types
| Type      | Format Specifier | Description |
| ----------- | ----------- | --------- |
| char      | %c       | single character(in single quotes, double quotes for string), typically one byte|
| int   | %d        | integer (non-decimal numeric value) |
| float | %f  | float (decimal numeric values) |
| double   | %lf | double-precision floating-point value |
| void      |      | the absence of the type |

Type casting:
* `(type_name) expression` 
* we can also use `atoi(string)` (string to int), `atof(string)` (string to float), etc.

Const keyword:
* indicates that value is not changing (changing it will result in compilation warning or warning
* string literals like "hello" are a type of const char* (not when they are initialized as an array though)
* example of comstant address (but value at address can be changed)
```C
int * const p_n = (int*)malloc(sizeof(int))
p_n = 0; // error
*p_n = 1; // fine
```
* to disallow both contents and address
```C
const int * const p_n = (int*)malloc(sizeof(int))
p_n = 0; // error
*p_n = 1; // error
```
* note: when you make a char array a constant, you can change the array as a whole but not individual chars


### Arrays
```C
data_type array_name[array_size] = {e1, e2, e3, ...};  // declaration (second part isn't necessary though), must specify size (not dynamic like python)
data_type variable_name = array[index]  // accessing an element 
data_type variable_name = *(array+1)  // another way to access an element (but keep in mind that pointer arithmetic is concious of type of pointer so it will add 1x8 bytes in this case)
```
Applications:
* strings
* arrays of structs
* linked lists

### Strings
1D character array terminated by a null character ('\0) -- `char str_name[num characters + 1]`
* the code below shows ways to initialize it (using double quotes will automatically include the null character at the end)

```C
  char arr1[4] = "uvw";
  char arr2[] = {'x', 'y', 'z', '\0'}; // you can choose whether or not you want to specify size in this case
  char arr3[3] = {'a', 'b', 'c'}; // Incorrect, will produce weird results bc there is no null character
  printf("%s\n", arr1); // uvw
  printf("%s\n", arr2); // xyz
  printf("%s\n", arr3); // something weird! 
```
* memory: the variable name is stored elsewhere and is equal to the address of the first character
* memory can also be edited differently depending on how it is defined (if you don't define it as an array, it is immutable)

```C
  // Defining string using address of character
  char *str = "abc";
  // not allowed to go str[1] = 'x';
  printf("%c\n", str[1]); // allowed to print str[1]
  printf("%zu\n", sizeof(str)); // 8 (since pointers are long ints)

  // Defining string using array
  char str2[] = "abc"; // alternatively char str2[] = {'a','b','c','\0'};
  str2[0] = 'x'; // fine
  printf("%s\n", str2); // xbc
  printf("%zu\n", sizeof(str2)); // 4 ({'a','b','c','\0'} takes up 4 bytes)
  
  // Defining using malloc
  char *str3 = (char *)malloc(3*sizeof(char)); // same as malloc(3)
  str3[0] = 'b';
  str3[1] = '\0';
  printf("%s\n", str3); // b
  free(str3); // frees memory
  
```

#### Strings and characters in binary
* if you cast a char to an int (i.e. `(int)'x'`) it will give the ASCII code (120) -- each character takes up 8 bites

### Functions
* calculate length of string: `strlen(string_name)`
* copy the content of second string int to the first string passed to it: `strcpy(destination, source)`
* concatenate two strings: `strcat(first_string, second_string)`
* compare two strings: `strcmp(first_string, second_string)`


### Input & Output
* print: `printf("Print something")`
* accept input: `scanf("format_specifier", &assigned_variable)`

### File Handling
```C
FILE *fp = fopen("fileName.txt", "r"); // open file
char line[200];
fgets(line, 200, fp);  // reads a line
line[strlen(line) - 1] = '\0';  // replace last element with null
int num_itmes = atoi(line);  //

fclose(fp); // close file
```

## Memory Allocation
Basic primitive variables:
* to allocate `int a = 42` in memory, it will choose an address (e.g. 3040) for that variable, when we change variable it will look for the variable, a, in memory and change the value in that location
* we can also use the malloc function to allocate space and then free the memory
```C 
int *a = (int *)malloc(sizeof(int) * 12);
\\ do something with the space
free(a);
```
* you can modify arrays (that includes strings) within functions because when you write arr[4] you are referencing the address first

### Pointers
Used to store the address of variables (convention: p_a)
* `&`: gets address of a variable
* `*[variable type it is pointer to]`: pointer type, depending on variable type it points to 
* we can initialize pointers with the malloc function or using the address of a preexisting variable
```C
int a = 42;
int* p_a = &a; // & is the "address-of" operator
               // int* is the type "address of int"
printf("%p", p_a); // will print pointer
printf("%ld\n", (long int)p_a); // can also cast it as a long int
printf("%d", *p_a); // will print int (because of the dereferencing operator *)
```

Void pointers: We use void pointers to overcome the issue of assigning separate values to different data types in a program. The pointer to void can be used in generic functions in C because it is capable of pointing to any data type.

Note on style: it is standard practice to write it as `int *p_a` instead of `int* p_a` but functionally, there is no difference

Pointer Arithmetic: 
```C
char *str = "hello";
printf(%c\n", str[1]);  // will print e (one index after h)
printf("%c\n", *(str + 1));  // will print e (one index after h)
```

## Data Structures

## Structures
Structure syntax:
```C
struct structureName 
{
dataType member1;
dataType member2;
...
};
```

typedef keyword
typedef function allows users to provide alternative names for the primitive and user-defined data types.
```C
typedef struct structureName 
{
dataType member1;
dataType member2;
...
}new_name;
```

## Linked Lists
* used to dyamically add elements more effectively
* consists of nodes which have
  * data: the actual data you need to store
  * next: the address of the next node
* operations:
  * insert: O(1)
  * remove: O(1)
  * get: O(n) or O(1) if index is known
* note: it takes up more space in memory but it is more time efficient in general

Implementation:
```C
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} node;

typedef struct LL{
    node *head;
    int size;
} LL;

void create_node(node **p_n, int data)
{
    *p_n = (node*)malloc(sizeof(node));
    (*p_n)->data = data;
    (*p_n)->next = NULL;
}


void create_LL_from_data(LL **p_LL, int *data_arr, int size)
{
    (*p_LL) = (LL*)malloc(sizeof(LL));
    (*p_LL)->size = 0; // initialize size to 0
    
    // keep track of the last node of the linked list
    node *tail = 0;

    for(int i = 0; i < size; i++){

        // n is a pointer to a node with data = data[i], next = NULL
        node *n;
        create_node(&n, data_arr[i]);

        // If the last node is the 1st node
        if(tail == 0){
            (*p_LL)->head = n;
        }

        // If the last node is not the 1st node
        else{
            // append the new node to the end of the linked list
            tail->next = n;
        }

        // update the tail
        tail = n;

        // update the size
        (*p_LL)->size++;
    }
}

int main(){
    int data_arr[] = {1, 2, 3, 4, 5};
    LL *p_LL;
    create_LL_from_data(&p_LL, data_arr, 5);
}
```

## Index Array

## Absract Data Type (ADT)
* any collection of values, together with operations on those values
  * ints with operations +, -, *, %, /
  * lists with operations insert, remove, get

# Algorithms
## Sorting

### qsort -- time complexity of O(n logn)
four main arguments
* array to be sorted
* number of elements in array
* size of each element in array
* comparator function: 
  * negative number = *p1 goes before *p2
  * 0 = *p1 is equivalent to *p2
  * positive number = *p1 goes after *p2

```C
int compare_ints(const void *p_a, const void *p_b)
{
  int *p_a_i = (int *)p_a;
  int *p_b_i = (int *)p_b;
  return *p_a_i - *p_b_i;
}
    
int main()
{
  int arr[] = {6, 5, 10, 2};
  qsort(arr, 4, sizeof(int), compare_ints);
}
```


### bubble sort -- time complexity of O(n^2), space complexity of O(1)

```C
void bubble_sort(void *arr, int num_items, int item_size,
                 int (*compare)(const void *, const void *))
{
  int i, j;
  void *temp = malloc(item_size);

  for (i = 0; i < num_items - 1; i++){
    for (j = 0; j < num_items - i - 1; j++){
      // compare arr[j] and arr[j + 1], swap if necessary
      // arr[j] only makes sense if array is of type int*, float*, etc.
      void *p_j = arr + j * item_size;
      void *p_j1 = arr + (j + 1) * item_size;

      // Now can compute compare(p_j, p_j1)
      if (compare(p_j, p_j1) > 0){
        // kind of want to swap *p_j and *p_j1
        memcpy(temp, p_j, item_size); // temp = *p_j
        memcpy(p_j, p_j1, item_size);
        memcpy(p_j1, temp, item_size);
        
        swapped = 1;
      }
    }
    if(!swapped){
      break;
     }
  }
  free(temp);
}
```
