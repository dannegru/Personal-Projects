from functions import testAlgorithm


# algorithm logic
def bubbleSort(array):
    length = len(array)

    for i in range(length):
        swap = False

        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True

        if not swap:
            break

    return array

# testing algorithm
print(testAlgorithm(bubbleSort))
