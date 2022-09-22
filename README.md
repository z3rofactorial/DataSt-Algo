# Sorting Algorithms
**Selection Sort**
* Dividing the list in sorted and unsorted parts and then checking the unsorted part of the list for the smallest element.
* When the smallest element is found then the element is placed at the starting position and the element at that position previously is shifted.

* arr[0]; the first element is set as the parity smallest element, i.e. small=arr[0]
* if arr[0]>arr[1]; then mark arr[1]==small
* else; move to next element keeping arr[0]==small