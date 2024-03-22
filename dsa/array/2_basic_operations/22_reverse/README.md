# Quick notes

## Reverse array **_in-place_**

- [x] When reversing an array in-place, the elements of the array are swapped directly within the same array without
  creating a new array.
- [x] This means that the original array will be modified after the reversal process
- [x] It saves memory because there is no need to create a copy of the array, but it might affect other elements in the
  program if they share the same reference to the array.

## Reverse array **_not in-place_**

- [x] When reversing an array not in-place, a new array is created, and the elements of the original array are copied
  into the new array in reverse order.
- [x] The original array remains unchanged, and the result of the reversal process is stored in a new array.
- [x] This preserves the original data and ensures that other elements are not affected, but it consumes additional
  memory to store the new array.

&rarr; In summary, reversing an array in-place modifies the original array directly without creating a new array, while
reversing an array not in-place creates a new array to store the result of the reversal without modifying the original
array.
