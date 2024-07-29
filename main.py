import math

def find_the_smallest_gap(array):
    """
    Finds the smallest gap between all pairs of elements in an array

    :parameter:
    -----------------------------------------------------------------------------------
        array: A list of real numbers.

    :return:
    -----------------------------------------------------------------------------------
        float: The smallest absolute difference between any two elements in the array
    """
    # Initialize with infinity to find the minimum
    smallest_gap = math.inf

    # Iterate over all possible pairs of elements
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            # Calculate the absolute difference between the current pair
            gap = abs(array[i] - array[j])
            # Update the smallest gap if the current gap is smaller
            if gap < smallest_gap:
                smallest_gap = gap
    return smallest_gap

if __name__ == "__main__":
    # Test case a
    array1 = [50, 120, 250, 100, 20, 300, 200]
    result1 = find_the_smallest_gap(array1)
    print(f'Smallest gap in {array1} is: {result1}')

    # Test case b
    array2 = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
    result2 = find_the_smallest_gap(array2)
    print(f'The smallest gap in {array2} is: {result2}')

