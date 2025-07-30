def merge_sort(array):
    # Base case: if the array has more than one element, split it
    if len(array) > 1:
        middle = int(len(array) / 2)  # Find the middle index

        # Split the array into left and right halves
        left = array[0:middle]
        right = array[middle:]

        # Print how the array is split
        print('\tSplit to', left, right)

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        # Initialize pointers for left and right arrays
        i = j = 0

        # Merge the two sorted halves back into the original array
        for element in range(len(array)):
            # Get current elements from left and right (or None if out of bounds)
            L = left[i] if i < len(left) else None
            R = right[j] if j < len(right) else None

            # If both L and R exist and L is smaller, or if R is None
            if ((L and R) and (L < R)) or R is None:
                array[element] = L  # Place L into array
                i += 1  # Move pointer in left array
            # If both L and R exist and L is greater or equal, or L is None
            elif ((L and R) and (L >= R)) or L is None:
                array[element] = R  # Place R into array
                j += 1  # Move pointer in right array

        # Print how the two halves are merged
        print('\t\tMerging', left, right)

# Define the unsorted array
array = [5, 3, 1, 2, 6, 4]

# Print the original array
print('Merge Sort...\nArray', array)

# Call merge_sort to sort the array
merge_sort(array)

# Print the sorted array
print('Array :', array)
