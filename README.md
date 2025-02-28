[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18248514)
## The Sorting Problem

### Coding directions

In this assignment we will be implementing several common sorting
algorithms but with some slight variations. You'll use `sorting.py` 
as a starting point and complete the functions given in that file
there. Be sure to leave the function definitions exactly as they are
since the automated tests done later on will expect these exact names and arguments. 

For this assignment, you'll likely want to implement
other "_helper_" functions that can be called from the main sorting functions you
will implment.  For example, with `quickSort()` you will likely want to
implement a separate `partition()` function. 

The exact sorting algorithms you will be implementing are: 
* bubbleSort(alist) 
* insertionSort(alist) 
* mergeSort(alist) 
* quickSort(alist)
* hybridSort(alist) 
* radixSort(alist)

Note that your `hybridSort()` function should be a combination of your
insertionSort() and mergeSort() functions. That is, when the size of input list
is small (e.g. n < 100), then it should use insertionSort(). When the size of
the input is large (e.g. n > 100), then it should use mergeSort(). This is
actually how the built-in sorting method in Python and Java (and probably other
languages) is implemented. Be sure that you implement this correctly!

As always, be sure to document your code well, include your name, etc.

Also be sure that your functions return the runtime so that we can
compare the performance of the algorithms. Additionally, you'll be using
Generative AI (e.g.  ChatGPT/Gemini/etc.) for certain parts of the assignment. Specifically, 
you will be asking the AI too to quiz you on your knowledge of these sorting algorithms. 

Here is a link to your dialogue should roughly look like (using Gemini):
* [https://g.co/gemini/share/090474d4498e](https://g.co/gemini/share/090474d4498e)

Note that although there were only two questions answered there, you need to answer 
at least 3 (and ideally more). See the assignment in Canvas for more details, and 
be sure to look closely at the rubric. 

Note that it is recommended that you try to implement the algorithms on your own
But if you want to ask Generative AI to help with coding and implementation, you can 
do that as well.
