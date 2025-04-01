"""
Insertion sort:

Intuition:
Takes an element and places in it correct order

14 9 15 12 6 8 13

step 1:
let's   14

Let's assume 14 in the only element and  size 1 array. 
it is in correct position


step 2:

let's take 14 9.

Is 9 at correct position for a size of 2? No

you go to the next element and ask on the left side where 9 should be
9 14

9 14 15 12 6 8 13

step 3:

Let's take 9 14 15 

is 15 at correct position for a size of 3? Yes

step 4:
Let's take 9 14 15  12

is 12 at correct position for a size of 4? No
Everyone right shift by 1

first swap:
9 14 12 15

second swap:
9 12 14 15

9 12 14 15 6 8 13

step 5:

Let's take 9 12 14 15 6

is 6 at correct position for a size of 5? No

Everyone right shift by 1

first swap:
9 12 14 6 15

second swap:
9 12 6 14 15

third swap:
9 6 12 14 15

fourth swap:

6 9 12 14 15

final output:
6 9 12 14 15 8 13


step 6:

Let's take 6 9 12 14 15 8

is 8 at correct position for a array size of 6? No

Everyone right shift by 1

first swap:
6 9 12 14 8 15

second swap:
6 9 12 8 14 15

third swap:
6 9 8 12 14 15

fourth swap:

6 8 9 12 14 15

final output:
6 8 9 12 14 15 13

step 7:

Let's take 6 8 9 12 14 15 13

is 13 at correct position for a array size of 7? No

Everyone right shift by 1

first swap:
6 8 9 12 14 13 15

second swap:
6 8 9 12 13 14 15

final output:
6 8 9 12 13 14 15

"""

def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i
        while(j > 0 and arr[j-1] > arr[j]):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
    return arr


if __name__ == "__main__":
    arr = [14,9,15,12,6,8,13]

    print("sorted array is:", insertion_sort(arr))
            