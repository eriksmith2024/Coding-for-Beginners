# Define the selection_sort function which takes a list called 'array'
def selection_sort(array):
    
    # Loop through each index of the array except the last one
    for index in range(0, len(array) - 1):
        
        # Store the current value at the current index
        value = array[index]
        
        # Set the current minimum index to the current index
        current = index
        
        # Loop through the rest of the array starting from the next element
        for element in range(index + 1, len(array)):
            
            # If a smaller element is found, update the current minimum index
            if array[element] < array[current]:
                current = element
        
        # Swap the current value with the smallest found value
        array[index] = array[current]
        array[current] = value
        
        # Print the array after placing the correct value at index
        print('\tResolving element[', index, '] to', array)

# Define the array to be sorted
array = [5, 3, 1, 2, 6, 4]

# Print the original unsorted array
print('Selection Sort... \nArray : ', array)

# Call the selection_sort function to sort the array
selection_sort(array)

# Print the final sorted array
print('Array: ', array)
