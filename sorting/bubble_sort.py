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



