def bubble_sort(array):
    # Outer loop runs once for each element in the array
    for index in range(len(array)):

        # Inner loop compares adjacent elements up to the unsorted portion
        for element in range((len(array) - 1) - index):
            # If the current element is greater than the next, swap them
            if array[element] > array[element + 1]:
                array[element], array[element + 1] = array[element + 1], array[element]

                # Print the array status after each swap
                print('\tResolving element[', element, '] to', array)

# Define the unsorted array
array = [5, 3, 1, 2, 6, 4]

# Print the original array
print('Bubble Sort..\nArray:', array)

# Perform bubble sort
bubble_sort(array)

# Print the sorted array
print('Array:', array)
