What to expect on midterm
* problem-solving midterm, kind of thing we would practice in the lab
* small details of C were removed
* will mostly see that it is a lot like a lab but you have to write it on paper
* undefined behaviour and accessing memory, memory leeks, etc.
* there will be some python on the exam (there will not be python memory model on midterm)
* sorting algorithms: will never ask for an algorithm by name (will only ask to write a sorting algorithm that is O(n) )
* very similar structure to ESC180
* the more recent the material is, the more it will be emphasized
* potentially know how to convert from binary to decimal, decimal to binary


## Precedence
* 1 + 5 * 8
* 1 + (5 * 8)
```C
int a = 5;
a = 6;


char *dest = malloc(10 );  // or you could write (char *)malloc(10 )
char *save_dest = dest;
char *src = "Hello";
while(*dest++ = *src++);  // goes through the entire array and copies it to src
  // the value of an assignment expression is the new value of the LHS

printf("%s\n", save_dest); // "Hello"

// a = 6 
int b = 1 + a++; // the value of the expression is a (b is now 7)
    // after the expression is evaluation, increment a (a is now 7)


```
