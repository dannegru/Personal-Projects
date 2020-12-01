import random


def testAlgorithm(algorithm):
    """Check if the algorithm sorts correctly

    Args:
        algorithm (function): the sorting function which is being checked

    Returns:
        boolean: True if algorithm sorts correctly, otherwise False
    """
    checks = 100

    for check in range(checks):
        randomLength = random.randint(500, 1000)
        randomArray = generateRandomArray(randomLength, -1000, 1000)

        arrayOne = algorithm(randomArray)
        arrayTwo = sorted(randomArray)

        if not areEqual(arrayOne, arrayTwo): return False

    return True


def generateRandomArray(length, minValue, maxValue):
    """Generate a random array

    Args:
        length (integer): the length of the random array
        minValue (integer): minimum value to be inserted in the array
        maxValue (integer): maximum value to be inserted in the array

    Returns:
        list: the randomly generated array
    """
    randomArray = list()

    for index in range(length):
        randomNumber = random.randint(minValue, maxValue)
        randomArray.append(randomNumber)

    return randomArray


def areEqual(arrayOne, arrayTwo):
    """Check if both arrays have the same elements, in the same order

    Args:
        arrayOne (list): array sorted by written algorithm
        arrayTwo (list): array sorted by Python sorted() function

    Returns:
        boolean: True if arrays are equal, otherwise False
    """
    if len(arrayOne) != len(arrayTwo): return False

    for index in range(len(arrayOne)):
        if arrayOne[index] != arrayTwo[index]: return False

    return True
