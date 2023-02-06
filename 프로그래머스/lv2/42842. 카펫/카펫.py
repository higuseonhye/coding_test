def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            width = yellow // i + 2
            height = i + 2
            if width * height - yellow == brown:
                return [width, height]
   
"""
The code loops through all possible values of the height (i) of the carpet, checking if yellow is divisible by i. 
If it is, the width is calculated as (yellow // i + 2), 
    and then the number of brown squares is calculated by subtracting yellow from the total number of squares in the carpet (width * height). 
If the number of brown squares equals the given brown, the function returns the width and height of the carpet as a list in the format [width, height].
"""

"""
for i in range(1, int(yellow**0.5)+1):

This line of code initializes a loop that will iterate over all numbers from 1 to the square root of the value of yellow plus 1 
    (the int function is used to round down the result of the square root). 
So the loop will iterate over all numbers that can be a potential divisor of yellow.
"""

"""
width = yellow // i + 2

The line width = yellow // i + 2 sets width equal to the result of yellow divided by i (integer division), and then adding 2 to the result. 
This is the calculation for the width of the carpet, taking into account the two brown lines that surround the yellow area.
"""
