![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Matplotlib Version](https://img.shields.io/badge/matplotlib-3.8.2-blue.svg)
![Memory Profiler Version](https://img.shields.io/badge/memory__profiler-0.61.0-blue)


## Three array search algorithms
___________________________________
### Made by: Camilo Castro


## Description

This repository can search a target number from an entry array using a linear,binary and ternary methods, and specifie whats is the position of that target number in input array,
if the target number isn't in the input array, it'll show you a unique message saying that you should try again, but with another number.

### What's linear search?

 * Linear search, also known as sequential search, is a simple search method where each element of the array is compared sequentially with the value we are searching for.
   
 * It starts from the first element and moves one by one until it finds the desired element or loops through the entire array without success.
   
 * It is effective on unordered arrays, but its efficiency is linear in the worst case, meaning that its execution time can grow linearly with the size of the array.

### What's binary search?

 * Binary search is an efficient algorithm for finding an element in an ordered array.
   
 * Repeatedly splits the array into two halves and then compares the searched element with the value in the middle.
   
 * If the searched value is equal to the value in the middle, the search ends.
   If the searched value is less than the value in the middle, the bottom half of the array is searched.
   If the searched value is greater than the value in the middle, the top half of the array is searched.

*  This process is repeated until the searched element is found or determined not to be in the array.
  
*  Binary search is much more efficient than linear search, since its execution time is logarithmic in the worst case, meaning that the execution time increases in proportion to the logarithm of the array size.
