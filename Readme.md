# *Bracket Check With Stack Algorithm*
This project is an example of using a Stack Algorithm to check the correct matching of brackets { }, [ ], and ( ) in a given string.

### *Objective*

This project was created to:

1. Check the correctness of matching parentheses in a string.
2. Report an error if the bracket matching is incorrect.
3. Report the location of the error if there is an error.

### *Description*

This section explains how the code works.Let's get started.

#### *First (What is Stack Algorithm?)*

A Stack Algorithm is an algorithm that uses a data structure called a "stack", which behaves similarly to placing pillows or boards on top of each other. The principle is "Last In, First Out" (LIFO), which means that data added to the stack most recently is retrieved before data added to the previous stack. this

The operation of an algorithm stack has many interactions. I will walk you through the basic steps:

Stack Creation: We need to create a stack data structure. Most of them use lists. (or arrays in other languages) to store data inside the stack. and set the pointer for the stack (for example, the default value is -1 or 0).

Adding data to the stack (Push): When we want to add any data to the stack, we add it to the list. (or array) and increment the pointer value where this pointer points to the last data added to the stack.

Pulling data from the stack (Pop): When we want to pull data from the stack. We will use the value of the pointer to point to the most recent data that was added to the stack. and we will remove that information from the list. (or array) and lower the pointer value.

Empty Check: We can check whether the stack is empty or not by checking the value of the stack pointer. If the pointer value is -1 (or 0), the stack is empty.

Peek: We can view the most recent item in the stack by using the value of a pointer to point to the item in the list (or array) without deleting the item.


And this is the sample code.

 [![image][linkToImage]
