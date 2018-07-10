def getUglyNumber(n):
    # Initialise the array
    uglyArray = [0] * n
    # The First ugly number is 1
    uglyArray[0] = 1

    # Used to track the index for 2,3 and 5
    count2 = 0
    count3 = 0
    count5 = 0

    # Multiples for finding the ugly number
    multipleOf2 = 2
    multipleOf3 = 3
    multipleOf5 = 5


    # Loop to find 2th number ~ nth number
    # The number sequence of ugly number is
    # 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
    # We can see that every ugly number is the multiples of 2,3 or 5
    # of another ugly number
    # 1×2=2, 2×2=4, 3×2=6, 4×2=8, 5×2=10, …
    # 1×3=3, 2×3=6, 3×3=9, 4×3=12, 5×3=15, …
    # 1×5=5, 2×5=10, 3×5=15,...
    # From the observation, we choose the minimum among these multiples
    # and move to next iteration
    for i in range(1, n):

    # Choose the minimum value
        uglyArray[i] = min(multipleOf2, multipleOf3, multipleOf5)

        if uglyArray[i] == multipleOf2:
            count2 += 1
            multipleOf2 = uglyArray[count2] * 2
        if uglyArray[i] == multipleOf3:
            count3 += 1
            multipleOf3 = uglyArray[count3] * 3
        if uglyArray[i] == multipleOf5:
            count5 += 1
            multipleOf5 = uglyArray[count5] * 5
    # Return result
    return uglyArray[n - 1]

# n is the nth ugly number
n = int(input("n?:"))
# Print the result
print(str(n) + "th ugly number is " + str(getUglyNumber(n)))
