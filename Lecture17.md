# Lecture 17

## Notes on upcoming midterm
* some questions will be closely related to the lab (qsort)

## Walkthrough for last week's lab
* how are structs stored in memory?
* to what extent can we draw an analogy between what is going on in C vs. Python?

```C
type def struct student1{
  char name[3];
  int age;
}student1

void change_name_wrong(student1 s)
{
 s.name[0] = 'b'; 
}

void change_name_right_1(student1 *p_s)
{
 p_s->name[0] = 'b'; 
}

void change_right_2(studnet1 *p_s)
{
  strcpy(p_s->name, "b");
}

int main()
{
 student1 s = {"x", 20}; 
 change.w(s);
 change_r1(&s);
 change_r2(&s);
}
```

| address | contents|
|:------|-----:|
| 32 | 'x', '\0', 0, 0 // c_w |
| 36 | |
| 40 | |
| 44 | 'x', '\0', .., ... //main: s |
| 48 | 20 //s.age |



