# def copy_sort( array ):
#     copy = array[ : ]
#     sorted_copy = [ ]
#     # Algorithm sequence to be added here
#     return sorted_copy


#     while len( copy )  > 0 :
#         minimum = 0
#         for element in range( 0, len(copy)):
#             if copy[element] < copy[ minimum ]:
#                 minimum = element
#         print( '\tRemoving', copy [ minimum ],\
#               'from', copy)
#         sorted_copy.append(copy.pop( minumum ))

#     array = [ 5, 3, 1, 2, 6, 4]

#     print('Copy Sort...\nArray:', array)

#     print( 'Copy:', copy_sort( array ))
#     print('Array:', array)

# def copy_sort(array):
#     copy = array[:]  # Make a shallow copy
#     sorted_copy = []

#     while len(copy) > 0:
#         minimum = 0

#         for element in range(1, len(copy)):
#             if copy[element] < copy[minimum]:
#                 minimum = element
#         print('\tRemoving', copy[minimum], 'from', copy)
#         sorted_copy.append(copy.pop(minimum))

#     return sorted_copy

# # Test the function
# array = [5, 3, 1, 2, 6, 4]

# print('Copy Sort...\n\nArray:', array)

# print('\nCopy:', copy_sort(array))
# print('\nArray:', array)


# Define a function called 'copy_sort' that takes one input: a list called 'array'
def copy_sort(array):
    
    # Create a copy of the original array so we don't change it directly
    copy = array[:]

    # Create an empty list to store the sorted values
    sorted_copy = []

    # Keep looping as long as the copied list still has elements in it
    while len(copy) > 0:

        # Start by assuming the first element in the copy is the smallest
        minimum = 0

        # Go through the rest of the list to find the actual smallest value
        for element in range(1, len(copy)):
            # If we find a smaller number, update 'minimum' to its position
            if copy[element] < copy[minimum]:
                minimum = element

        # Print which number is being removed, and the current state of the list
        print('\tRemoving', copy[minimum], 'from', copy)

        # Remove the smallest number from the copy and add it to the sorted list
        sorted_copy.append(copy.pop(minimum))

    # After the loop is done, return the sorted list
    return sorted_copy

# Define the original list to sort
array = [5, 3, 1, 2, 6, 4]

# Print a header and the original array
print('Copy Sort...\n\nArray:', array)

# Call the copy_sort function, print the sorted result
print('\nCopy:', copy_sort(array))

# Print the original array again to show that it hasn't changed
print('\nArray:', array)
