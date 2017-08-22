def count_elements(given_array):
    """
    A function that counts frequencies of elements in an array of positive numbers
    :param given_array: the input array
    :return: Prints the numbers and how many times they appears
             example :
             0 => 0
             1 => 2
             2 => 2
             3 => 0
             4 => 1
    """

    # length of the array
    n = len(given_array)

    # subtract 1 from the array
    subtracted_array = [x - 1 for x in given_array]

    # Set input[input[0]%n] = input[input[0]%n] + n
    for i in range(n):
        subtracted_array[subtracted_array[i] % n ] = subtracted_array[subtracted_array[i] % n] + n

    # Print all elements
    for i, element in enumerate(subtracted_array):
        frequency = element//n
        if(frequency != 0 ):
            print(i+1, '=>' , frequency)


if __name__ == "__main__":
    given_array = [2, 3, 3, 2, 5, 7, 7, 5, 1, 10]
    count_elements(given_array)