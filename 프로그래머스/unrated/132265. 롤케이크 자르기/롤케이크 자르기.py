def solution(topping):
    answer = 0
    forward = set()
    backward = {}
    for i in topping:
        backward[i] = backward.get(i, 0) + 1
    for i in topping:
        forward.add(i)
        backward[i] -= 1
        if backward[i] == 0:
            del backward[i]
        if len(forward) == len(backward):
            answer += 1
    return answer

"""
def solution(topping):
    answer = 0                                # Initialize the variable 'answer' to 0
    forward = set()                           # Create an empty set 'forward'
    backward = {}                             # Create an empty dictionary 'backward'
    for i in topping:                         # Iterate through each element 'i' in the 'topping' list
        backward[i] = backward.get(i, 0) + 1  # Add element 'i' to the 'backward' dictionary and increment its count by 1
    for i in topping:                         # Iterate through each element 'i' in the 'topping' list again
        forward.add(i)                        # Add element 'i' to the 'forward' set
        backward[i] -= 1                      # Decrement the count of element 'i' in the 'backward' dictionary by 1
        if backward[i] == 0:                  # If the count of element 'i' in the 'backward' dictionary is 0
            del backward[i]                   # Delete the element 'i' from the 'backward' dictionary
        if len(forward) == len(backward):     # If the length of 'forward' set is equal to the length of keys in 'backward' dictionary
            answer += 1                       # Increment the 'answer' variable by 1
    return answer                             # Return the final value of 'answer' variable
"""

"""
This code is a solution to a problem that requires counting the number of ways to make a pizza with different toppings. 
The problem requires that each pizza must have at least one topping and different pizzas must have different sets of toppings. 
The solution() function takes in a list of toppings as an input and returns the number of ways to make a pizza with different sets of toppings.

Here's a step-by-step explanation of the code:
1. The answer variable is initialized to 0 to keep track of the number of pizzas that can be made with different sets of toppings.
2. The forward set is created to keep track of the toppings that have already been considered for the current pizza.
3. The backward dictionary is created to keep track of the frequency of each topping in the remaining list of toppings.
4. The first loop iterates over the topping list, and for each element i in the list, it increments the count of i in the backward dictionary. 
   This dictionary is used to keep track of the frequency of each topping.
5. The second loop also iterates over the topping list, and for each element i in the list, 
   it adds i to the forward set and decrements its count in the backward dictionary.
6. If the count of i in the backward dictionary is 0, 
   it means that all the occurrences of i have already been considered for the current pizza, 
   so i is deleted from the backward dictionary.
7. If the length of forward set is equal to the length of keys in the backward dictionary, 
   it means that all the toppings that have not yet been considered for the current pizza have different sets of toppings from the ones already considered. 
   So, a new pizza can be made with the remaining toppings, and answer is incremented by 1.
8. Finally, the function returns the final value of the answer variable.

In summary, the function uses sets and dictionaries to keep track of the toppings that have already been considered and those that have not, respectively. 
It checks whether a new pizza can be made with the remaining toppings and increments the answer variable if it is possible to make a new pizza with different toppings.
"""
