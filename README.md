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
`(type_name) expression` 

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
````C
typedef struct structureName 
{
dataType member1;
dataType member2;
...
}new_name;
```
