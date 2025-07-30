def insertion_sort(array):
    # Loop through each element in the array starting from the second one
    for index in range(1, len(array)):
        value = array[index]  # Store the current value to be inserted

        # Shift elements of the sorted part of the array to the right
        # until the correct position for 'value' is found
        while array[index - 1] > value and index >= 1:
            array[index] = array[index - 1]  # Shift the element to the right
            index -= 1  # Move to the previous index

        array[index] = value  # Insert 'value' at its correct sorted position

        # Print the array status after each insertion step
        print('\tResolving element[', index, '] to', array)

# Define the unsorted array
array = [5, 3, 1, 2, 6, 4]

# Print the original array
print('insertion Sort...\nArray:', array)

# Perform insertion sort
insertion_sort(array)

# Print the sorted array
print('Array :', array)


