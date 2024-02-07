![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Matplotlib Version](https://img.shields.io/badge/matplotlib-3.8.2-blue.svg)
![Memory Profiler Version](https://img.shields.io/badge/memory__profiler-0.61.0-blue)


## Three array search algorithms

### Made by: Camilo Castro
_____________________________________________________


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


### What's ternary search?

   * Ternary search is similar to binary search, but instead of splitting the array into two parts, it splits it into three equal parts.
     
   * Compares the searched element with the values at two division points.
     
   * Depending on how these values are compared, it can be determined in which of the three parts (left, middle or right) of the array the desired element is located.
     
   * Then, repeat the process in the part of the array where it is determined that the searched element could be.

   * Like binary search, ternary search is efficient and has a worst-case logarithmic execution time.

_________________________________________________________________________________


 ## How to use this repository?


  * First clone this repository and install the requirements.txt.

       **-> For clone this repository use:** git clone https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms.git

       **-> And, to install all the dependencies use:** pip install -r requirements.txt
    
  * Second, run the main.py file

  **Then, you should got this:**

   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/2c8175b0-2b07-4e9c-b4dd-7c869a3b0f92)
     
   **In this screen, you should type a number to choose the method**

   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/c0b37692-5e2e-4e7f-95fd-4f83cb4b4d06)

   **In this case, i wanna use the linear method, and as entry array i type: [1, 2, 3, 4, 5, 6, 7, 8, 9]**

   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/544ae9d5-0e17-428a-9a76-5dc277f7f5b3)

   **Then pull the enter key, and select a target number (number to search in the input array), for this example, i'll select 9 as target number.**

   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/877fc6ed-bd35-4824-95fd-b12b2b1e7c54)

   **And we got this, a graph of the current memory used and the elapsed time:**

   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/5b738128-2c2b-49c1-991c-a2cce6d79b36)
   
_____________________________________________________________________________________________________________________________________________

   **Another example**
   
   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/813008a8-6901-41b5-89f6-dddc0f0b7362)
   
   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/69a2bb3b-81ad-4d62-8f32-ab1d6b17c496)

 ____________________________________________________________________________________________________________________________________________

 

   **Coverage result**

   
   ![image](https://github.com/BlutLucifugeKrieger/Three-array-search-algorithms/assets/130005378/b7de2fea-6c72-43cd-8665-1e2cbe2cd518)




 
