# Lecture 24

## review of pyinteger
```C

create_pyinteger(pyinteger **p_p_n, int n)
{
  *p_p_n = (pyinteger *)malloc(sizeof(pyinteger));
  (*p_p_n)->num_digits = (int)(log10(n)+1;
  (*p_p_n)->capacity = (*p_p_n)->num_digits;
  (*p_p_n)->digits = (int *)malloc(sizeof(int))*(*p_p_n)->capacity);
  for(int loc = (*p_p_n)->num_digits-1; loc >= 0; loc--){
    (*p_p_n)->digits[loc] = n%10;
    n /= 10;
  }
}

void deep_copy_pyint(pyinteger *dest, pyinteger  *src)
{
  dest->capacity = src->num_digits;
  dest->digits = (int *)realloc(dest->digits, sizeof(int)*dest->capacity);
  memcpy(dest->digits, src->digits, sizeof(int)*src->num_digits);
  ....
  dest->num_digits = src->num_digits;
}

void add(pyinteger *n1, pyinteger *n2)
{
  pyinteger *m1;
  pyinteger *m2;
  if(n1->num_digits > n2->num_digits){
    deep-copy_pyinteger(m1, n1);
    deep_copy_pyinteger(m2, n2)
   } else {
     deep_copy_pyinteger(m2, n1);
     deep_copy_pyinteger(m1, n2);    
    
  }
  
}

// m1 has at least as many digits as m2
int offset = m1->num_digits - m2->num_digits;
int carry = 0;

int loc;
for(loc = m1->num_digits-1; loc-offset >= 0; loc--){
  int sum = m1->digits[loc] + m2->digits[loc-offset] + carry;
  if(loc-offset >= 0){
    sum += m2 m2->digits[loc-offset];
  }
  
  if(sum > 9){
    carry = 1;
    sum -= 10;
  } else {
    carry = 0;
  }
}
while (carry != 0 && loc >= 0){
  int sum = m1->digits[loc] + carry;
  if(sum > 9){
    carry = 1;
    sum -= 10;
  } else {
    carry = 0;
  }
}

if (carry == 1){
  if(m1->capacity == m1->num_digits){
    m1->capacity *= 2;
    m1->digits = (int *)realloc(m1->digits, sizeof(int)*m1->num_digits);
  }
  memmove(m1->digits+1, m1->digits, sizeof(int)**m1->num_digits);
  m1->digits[0] = 1;
  m1->num_digits++;
  
 }

deep_copy_pyinteger(n1, m1);

}


```

calculating runtime of the program
* copying all the digits: O(# of digits)
* adding the digits: O(# of digits)
* n: magnitude of the input
* number of digits in n: floor(log10(n))+1
* note on floor(): a library function in C defined in the <math.h> header file. This function returns the nearest integer value, which is less than or equal to the floating point number (float or double) passed to it as an argument
* complexity: O(log n), where n is the max (n1, n2)
* this is the best you can do for addition
