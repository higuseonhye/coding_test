"""
The code implements a solution for the English word chain problem as described. 
It takes two parameters n and words where n is the number of people playing the game and words is a list of words said in the order by the people.

The code uses the used_words list to keep track of words already used in the game. 
For each word in the words list, it checks if the word has already been used or if the word's first letter doesn't match the last letter of the previous word. 
If either of these conditions is true, the function returns the number of the person who made a mistake and the round they made the mistake in. 
If no mistakes were made, the function returns [0, 0].
"""

"""
The line return [(i % n) + 1, (i // n) + 1] calculates the person's number and the round they made a mistake in and returns the result as a list.
The person's number is calculated as (i % n) + 1. i % n calculates the remainder of i divided by n, which gives us the number of the person in the current round. 
Since the person numbers are 1-indexed and not 0-indexed, we add 1 to the result to get the actual person number.
The round number is calculated as (i // n) + 1. i // n calculates the number of full rounds completed so far, and adding 1 gives us the actual round number.
"""

def solution(n, words):
    used_words = []
    for i, word in enumerate(words):
        if word in used_words or (i > 0 and word[0] != words[i - 1][-1]):
            return [(i % n) + 1, (i // n) + 1]
        used_words.append(word)
    return [0, 0]
