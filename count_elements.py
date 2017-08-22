import time

def count_elements(given_array):
    """
    A function that count frequencies of elements in an array of positive integers
    :param given_array: the input array
    :return: Prints the numbers and how many times they appears
             example :
             0 => 0
             1 => 2
             2 => 2
             3 => 0
             4 => 1
    """
    start = time.time();

    # length of the array
    n = len(given_array)

    # subtract 1 from the array
    subtracted_array = [x - 1 for x in given_array]

    # get the max number
    max_number = max(given_array)

    # append 0 to the subtracted_array x times, where x is the deference between max_number and n,
    # in order the array to have length equal to the max_number
    for i in range(n , max_number):
        subtracted_array.append(0)

    # new length of the array
    n_new = max_number

    # Set input[input[0]%n_new] = input[input[0]%n_new] + n_new
    for i in range(n_new):
        index = subtracted_array[i] % n_new
        subtracted_array[index] = subtracted_array[index] + n_new

    # Print all elements

    # we have to subtract all the elements we append to the array from the first element count
    first_element_count = subtracted_array[0]//n_new-(max_number-n)
    if first_element_count != 0:
        print(1, '=>', first_element_count)

    # continue printing from second element
    for i, element in enumerate(subtracted_array[1:]):
        frequency = element//n_new
        if(frequency != 0 ):
            print(i+2, '=>' , frequency)

    end = time.time()

    print('Elapsed time: ', end - start, 'seconds')

    # # Slow algorithm (for comparison reasons)
    # start = time.time()
    #
    # for number in given_array:
    #     frequency = given_array.count(number)
    #     if frequency != 0:
    #         print(number, '=>', frequency)
    #
    # end = time.time()
    #
    # print('Elapsed time: ', end - start, 'seconds')

if __name__ == "__main__":
    given_array = [431, 132, 490, 439, 262, 418, 282, 366, 464, 276, 199, 431, 262, 77, 356, 52, 39, 36, 103, 326, 493, 139, 368, 284, 202, 377, 290, 13, 184, 493, 86, 492, 20, 353, 327, 490, 452, 229, 197, 302, 53, 198, 162, 235, 350, 100, 337, 165, 407, 21, 112, 462, 103, 95, 391, 232, 470, 489, 196, 301, 419, 330, 452, 320, 499, 449, 79, 448, 325, 438, 404, 43, 90, 137, 341, 345, 370, 222, 57, 25, 153, 427, 298, 246, 338, 286, 18, 171, 264, 144, 117, 354, 490, 301, 44, 88, 126, 84, 325, 75, 49, 406, 461, 390, 257, 365, 279, 414, 52, 81, 290, 334, 432, 379, 445, 182, 351, 450, 264, 50, 81, 380, 294, 336, 127, 158, 299, 254, 162, 117, 423, 88, 393, 457, 138, 34, 40, 223, 243, 112, 172, 196, 463, 197, 127, 64, 274, 267, 188, 65, 116, 221, 220, 205, 253, 380, 206, 79, 161, 211, 435, 312, 257, 313, 204, 347, 438, 235, 182, 357, 401, 249, 22, 134, 432, 373, 231, 24, 358, 327, 292, 266, 214, 26, 442, 482, 208, 123, 436, 151, 231, 297, 314, 66, 457, 443, 233, 227, 354, 287, 67, 400, 409, 187, 373, 235, 176, 335, 300, 365, 177, 476, 355, 197, 299, 113, 145, 328, 162, 391, 167, 66, 166, 180, 393, 247, 319, 250, 212, 185, 464, 264, 63, 291, 56, 90, 434, 344, 361, 46, 414, 140, 284, 465, 78, 258, 354, 202, 487, 392, 56, 207, 315, 170, 368, 432, 384, 243, 13, 3, 204, 11, 421, 343, 134, 248, 188, 500, 50, 267, 444, 491, 158, 287, 310, 425, 224, 454, 113, 53, 150, 232, 28, 264, 202, 107, 132, 459, 117, 210, 108, 106, 111, 70, 396, 57, 486, 338, 458, 3, 327, 426, 252, 147, 368, 112, 377, 281, 224, 425, 500, 494, 475, 78, 309, 378, 199, 163, 120, 73, 74, 47, 1, 156, 110, 202, 388, 448, 230, 290, 91, 24, 356, 354, 356, 425, 297, 58, 263, 69, 51, 368, 344, 455, 257, 313, 334, 365, 197, 171, 440, 414, 43, 221, 346, 414, 77, 407, 386, 55, 51, 132, 193, 229, 482, 58, 294, 429, 316, 424, 148, 405, 62, 378, 500, 404, 486, 55, 96, 198, 131, 174, 355, 477, 197, 424, 145, 245, 113, 217, 493, 86, 81, 224, 325, 335, 281, 309, 137, 224, 170, 354, 247, 106, 200, 319, 246, 289, 33, 51, 324, 436, 477, 358, 256, 407, 204, 280, 105, 404, 96, 284, 15, 128, 146, 33, 34, 351, 96, 355, 156, 18, 125, 280, 432, 133, 259, 220, 266, 96, 492, 313, 99, 381, 195, 264, 350, 88, 146, 417, 231, 467, 189, 499, 318, 21, 61, 420, 419, 177, 77, 145, 466, 45, 468, 263, 295, 235, 372, 481, 54, 319, 121, 453, 418, 176, 399, 152, 101, 228, 283, 487, 232, 125, 240, 63, 270, 53, 478, 242, 4, 340, 234, 333, 53, 465, 209, 334, 263, 474, 582]
    count_elements(given_array)