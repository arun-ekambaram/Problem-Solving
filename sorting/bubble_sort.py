"""

Bubble sort:

Intuition:
Pushes the maximum to the last by adjacent swaps

input:
13 46 24 52 20 9

first two elements:
13 46 => 13 < 46

are they in sorted order? yes. do not do anything

13 46 24 52 20 9

next two elements:
46 24 => 46 < 24 

are they in sorted order? no. swap it

13 24 46 52 20 9

next two elements:
46 52 => 46 < 52 

are they in sorted order? yes. do not do anything

13 24 46 52 20 9

next two elements:
52 20 => 52 < 20 

are they in sorted order? no. swap it

13 24 46 20 52 9

next two elements:
52 9 => 52 < 9

are they in sorted order? no. swap it

13 24 46 20 9 52



Notice that after one complete round of adjacent swaps the maximum number 52 
will be at the last

after step 1 last index is sorted
after step 2 last two index is sorted
..
..

Implementation:
                i
first step  0 - n-1

second step 0 - n-2

third step 0  - n-3
..
..
..
            0 - 1


"""

def bubble_sort(arr):
    for i in range(len(arr),1, -1):
        for j in range(0,i-1,1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

if __name__  == "__main__":
    arr = [13,46,24,52,20,9]

    print("The array after the bubble sort is:", bubble_sort(arr))



"""

Time complexity:
O(n^2) 
       - worst
       - Average

Can be optimised
if everything is in the  correct order in the first check.
the array is in the Ascending order

"""

def bubble_sort(arr):
    for i in range(len(arr),1, -1):
        didswap = 0
        for j in range(0,i-1,1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                didswap = 1
        if didswap == 0:
            break
        print("runs")

    return arr


if __name__  == "__main__":
    arr = [13,46,24,52,20,9]
    arr1 = [6,5,4,3,2,1]
    arr2 = [1,2,3,4,5,6]

    print("The array after the bubble sort is:", bubble_sort(arr))
    print("The array after the bubble sort is:", bubble_sort(arr1))
    print("The array after the bubble sort is:", bubble_sort(arr2))



"""

Time complexity:
O(n) - best case


"""