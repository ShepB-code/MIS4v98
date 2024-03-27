## Numpy Exercise
import numpy as np 

## Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")

twos = np.full((4,3),2)
print(twos)

## Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

array = np.arange(0,120,10).reshape(3,4)
print(array) 

## Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")

new_array = array.reshape(4,3)
print(new_array)

## Step 4: Multiply every element of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

new_new_array = new_array * 3
print(new_new_array)

## Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")

## twos * array

## This errored out... why?
print()

## Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")

print(twos * new_array)
## this worked! why?
##                              This worked because they have the same number of columns
print()



