# Lecture 16
Note: the following blocks of code use the packages: stdio.h, and stdlib.h
## Debugging
Debug as you go, small chunks at a time.
This is a sample file to demonstrate debugging.

Debugging in VS code & Data inspection:
* put a breakpoint and track the variables (in the locals table)
* once you get to the problematic function, step in (you can step over those that aren't causing problems)
* under the WATCH section, ask for things like: num_str[0], num_str[1] by clicking on the plus button



## Converting between data types
A few things to note:
* const indicates that the variable will remain constant (can't be changed)

```C
int is_digit(char c)
{
  return c >= '0' && c <= '9'
}

//Input: something like "g = 9.8"
//Output: "9.8"
const char * get_numeric_str(const char *str)
{
  while(!is_digit(*str)){  //*str is the same as str[0]
    str++;                  // str++ is the same as str = str + 1
  }
  return str;
}

int main()
{
  const char *my_num = get_numeric_str("g = 9.8");
  printf("%s\n", my_num);
}

```

Let's make a function to convert the string to a float (double):
```C
double my_atof(const char *str)
{
  //-12.34
  double result = 0.0;
  int sign = 1;
  
  if(*str == '-'){
    sign = -1;
    str++;
  }
  
  while(*str != '.'){
    result = result * 10 + (*str - '0'); // result is the integer part of the original input
    str++; 
  }
  str++; // skip the decimal point
  
  double fraction = 0;
  double power10 = 0.1; 
  while(*str != '\0'){
    fraction += (*str - '0') * power10;
    str++;
    power10 /= 10;
    }
    
    return sign * (result + fraction);
}

int main()
{
  const char *my_num = get_numeric_str("g = 9.8");
  printf("string: %d\n", my_num);
  printf("Double: %f\n", my_atof(ny_num));

}

```

Logic behind reading in ASCII characters:
Ex: 567 --> 10*(10*5+6)+7
* read in the five
* multiply that five by 10 (add a 0) and add the next number, 6
* multiply 56 by 10 and add the next number, 7

New function (reading in a sum):

```C
void read_in_and_sum(const char *filename)
{
  FILE *fp = fopen(filename, "r");
  if(fp == NULL){
    printf(.Errror opening file %s\n", filename);
    return;
    }
    
   double sum = 0.0;
   char line[100];
   while(fgets(line, 100, fp) != NULL){
    const char *num_str = get_numeric_str(line);
    sum += my_atof(num_str);
   }
  }
}

// gives the wrong sum
```

This will not work. Modified code:

```C
// to be updated . . . 
```



