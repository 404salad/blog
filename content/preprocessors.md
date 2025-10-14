```toml
title = "The C Preprocessor"
tags = ["C","compiler"] 
date = 2025-04-20
```
Preprocessors are used to make writing code easier by enabling macros and other utilities like splitting a string across several lines using a \  
we can see the expansion of macros in c using the -E flag  
```bash
    gcc -E source_file.c -o output_file.i
```
this will just run the preprocessor and enable use to see the actual input to our compiler  
[Great video on c preprocessors](https://www.youtube.com/watch?v=t5JtyDlESns)

even an empty file  
```c
void main() {
}
```  
the preprocessed file looks like this  
```c
# 0 "empty.c"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 0 "<command-line>" 2
# 1 "empty.c"
void main() {
}
```  
these are the default preprocessor actions, atleast for gcc  

but if you include <stdio.h>
```c
#include <stdio.h>
#define PI 3.141459

int main() {
    printf("%d", PI);
    return 0;
}
```
the resultant preprocessed file is over **700 lines**!!! now that is interesting  

constants are directly replaced  
io.c  
```c
#define FIVE 5
int main() {
    int a = FIVE;
    int b = a+4;
    return 0;
}
```
io_pre.i  
```c
# 0 "io.c"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "/usr/include/stdc-predef.h" 1 3 4
# 0 "<command-line>" 2
# 1 "io.c"

int main() {
    int a = 5;
    int b = a+4;
    return 0;
}
```
lua does not have preprocessors it would be interesting project to try to add preprocessing to the lua compiler  
