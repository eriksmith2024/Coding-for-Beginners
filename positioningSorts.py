# Define the quick_sort function that takes a list called 'array'
def quick_sort(array):

    # Check if the list has more than one element (base case for recursion)
    if len(array) > 1:

        # Set the pivot index as the last element's index
        pivot = int(len(array) - 1)

        # Create empty lists to store values less than and greater than the pivot
        less = []
        more = []

        # Iterate through each element in the array by index
        for element in range(len(array)):
            value = array[element]  # Get the current value

            # Skip the pivot itself
            if element != pivot:
                # Compare value to pivot value
                if value < array[pivot]:
                    less.append(value)  # Add to 'less' if smaller than pivot
                else:
                    more.append(value)  # Add to 'more' if greater or equal to pivot

        # Recursively sort the 'less' and 'more' lists
        quick_sort(less)
        quick_sort(more)

        # Print the split for visual understanding
        print('\tLesss:', less, '\tPivot:', array[pivot], '\tMore:', more)

        # Merge the sorted lists and pivot back into the original array
        array[:] = less + [array[pivot]] + more

        # Print the merged result
        print('\t\t...Merged', array)

# Define a list of unsorted integers
array = [5, 3, 1, 2, 6, 4]

# Print the initial array
print('\nQuick Sort... \nArray :', array)

# Call the quick_sort function on the array
quick_sort(array)

# Print the sorted array
print('Array :', array, '\n')
gbnr