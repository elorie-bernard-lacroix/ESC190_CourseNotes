# Lecture 20
## What to expect on midterm
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

## Precedence and Associativity
![image](https://user-images.githubusercontent.com/67354651/223187675-ff8d44c0-8287-44dd-a699-03f78d5d788b.png)
![image](https://user-images.githubusercontent.com/67354651/223187810-86c8043d-9bb7-4f8c-b54a-b46d3c100980.png)

## structs in python
```Python
class Student:
  # constructor
  def __init __(self, name, age):
    self.name = name
    self.age = age
   
  def __str__(self):
    return "Name: " + self.name + ", Age: " + str(self.age)
    
  def __lt__(self, other):
    return self.age < other.age:
      return True
     elif self.age > other.age:
      return False
     else:
      return self.name < other.name
  
 def f():
  return 42
 
 s = Student("Jake", 20)
 s.blah = 42
 print(s)  # will print "Name: Jake, Age: 20"
 
```

* you can use the functions instead of using the operator
`s1.__lt__(s2)`
`Student.__lt__(s1, s2)`

## using .sort
```C
student_list = [Student("Jake", 20), Student("John", 20), Student("Jane", 21)]
student_list.sort()

def get_name(s):
  return s.name
  
student_list.sort(key=get_name) # sort lexicographically by name
student_list.sort(key=lambda s: s.name) # same as above
```
* writing lrt is like using qsort
