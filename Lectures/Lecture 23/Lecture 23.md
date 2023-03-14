# Review of the Midterm

### Question 5
ADT pyinteger: An integer that can hold an unlimited number of digits
Operations: plusplus, add
* plusplus: modify n1 to n1+1
* add n1 n2: set n1 = n1 + n2

Suggestion: an array list

```C
#if !defined(PYINTEGER_H)
#defined PYINTEGER_H

typedef struct pyinteger {
  int *digits;
  int size;
  int num_digits;
} pyinteger;

void plusplus(pyinteger *n1);
void add(pyinteger *n1, pyinteger *n2);
void create_pyinteger(pyinteger **p_p_n, int magnitude);

#endif
```

separate file:
```C
#include "pyinteger.h"

void create_pyinteger(pyinteger **p_p_n, int n)
{
  *p_p_n = (pyinteger *)malloc(sizeof(pyinteger));
  (*p_p_n)->num_digits = (int)(log10(n)+1);
  (*p_P_n)->capacity = (*p_p_n)->numdigits;
  (*p_p_n)->digits = (int *)malloc(sizeof(int)*(*p_p_n)->capacity);
  
  for(int loc = (*p_p_n)->num_digits-1; loc >= 0; loc--){
    (*p_p_n)->digits[loc] = n%10;
    n = n/10;
  }
  
}

void plusplus(pyinteger *n1){     // must be a point because, otherwise, can't change the value
  int carry = 1;
  int loc;
  for(loc = n1->num_digits-1; loc >= 0; loc--){
    if(n1->digits[loc] == 9 && carry == 1){
      n1->digits[loc] = 0;
    }else{
      n1->digits[loc] += carry;
      break;
    }
  }
  if(loc == -1){
    if(n1->capacity =- n1->num_digits){
      n1->capacity *= 2;
      n1->digits = (int *)realloc(n1->digits, sizeof(int)*n1->capacity);
    }
    n1->num_digits++;
    n1->digits[0] = 1;                
    n1->digits[n1->num_digits-1] = 0;
  }
}

```
