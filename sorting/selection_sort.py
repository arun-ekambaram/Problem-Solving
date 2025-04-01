
"""
Selection sort:

Intuition:

Select minimum value and Swap

step 1:

- get the minimum from the entire array and place it at first position and
whoever in the first position will move to the minimum position.

now remember the first portion is sorted. So move the index.

step 2:

- repeat step 1

6 elements - took 5 steps


implementation:

swap happened at index 0 & min index [0 - n-1]
swap happened at index 1 & min index [1 - n-1]
swap happened at index 2 & min index [1 - n-1]
swap happened at index 3 & min index [1 - n-1]
swap happened at index 4 & min index [1 - n-1]
.
.
.
index will go till [n-2]

For eg:

13 46 24 52 20 9

select min: min = 9
first place: first = 13

swap(min, first)

repeat


Input:

13 46 24 52 20 9

dry run:

9 46 24 52 20 13

9 13 24 52 20 46

9 13 20 52 24 46

9 13 20 24 52 46

9 13 20 24 46 52 -  sorted 



-
"""

def selection_sort(arr):



    for i in range(0,len(arr)-1):
        mini = i

        for j in range(i,len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp
    return arr

if __name__ == "__main__":
    arr = [13,46,24,52,20,9]
    print("The sorted array using Selection Sort is: ", selection_sort(arr))









        
