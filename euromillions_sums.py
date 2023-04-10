## euromillions number generator
##This function uses a while loop to generate sets of five random
# numbers between 1 and 50 until the sum of the numbers falls between 
# 98 and 164. It uses the random.randint() function to generate each 
# number, and stores them in a list called numbers. It calculates the
# sum of the list using the sum() function and stores it in a variable 
# called total. If the sum of the numbers falls within the desired 
# range, the function returns the list of numbers using the return 
# keyword. If the sum is not within the range, the loop continues to 
# generate a new set of numbers until a valid set is found.
# The specific range was chose because of the distribution of the sums of 
# combinations. While, for example, combinations with sums between 98 and
# 164 a more likely to be drawn, this is because there are more such
# combinations. Each such combination, however, has the same chance to 
# be drawn as all others

import random

def generate_numbers():
    while True:
        numbers = [random.randint(1, 50) for i in range(5)]
        total = sum(numbers)
        if 98 <= total <= 164:
            return numbers
print(generate_numbers())
