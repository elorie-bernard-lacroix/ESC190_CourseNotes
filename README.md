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

### Data Types
| Type      | Format Specifier | Description |
| ----------- | ----------- | --------- |
| char      | %c       | single character(in single quotes, double quotes for string), typically one byte|
| int   | %d        | integer (non-decimal numeric value) |
| float | %f  | float (decimal numeric values) |
| double   | %lf | double-precision floating-point value |
| void      |      | the absence of the type |

### Arrays
```C
data_type array_name[array_size];  // declaration
data_type variable_name = array[index]  // accessing an element 
```
Applications:
* strings
* arrays of structs
* linked lists

### Strings
1D character array terminated by a null character ('\0) -- `char str_name[size]`

functions:
* calculate length of string: `strlen(string_name)`
* copy the content of second string int to the first string passed to it: `strcpy(destination, source)`
* concatenate two strings: `strcat(first_string, second_string)`
* compare two strings: `strcmp(first_string, second_string)`


### Input & Output
* print: `printf("Print something")`
* accept input: `scanf("format_specifier", &assigned_variable)`

## File Handling

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
