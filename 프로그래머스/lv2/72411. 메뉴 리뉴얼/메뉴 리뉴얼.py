from itertools import combinations
from collections import Counter

def solution(orders, course):
    # The variable answer is an empty list that will be used to store the result.
    answer = []
    
    # The for loop iterates through the list course and the value of each iteration is stored in the variable n.
    for n in course:
    
        # The menu list is used to store the combinations of n characters sorted in lexicographic order.
        menu = []
        
        # The inner for loop iterates through the list orders and the value of each iteration is stored in the variable order.
        for order in orders:

            # The combinations function from the itertools library is used to generate all combinations of n characters sorted in lexicographic order.
            # The result of each iteration is appended to the menu list.
            menu += list(combinations(sorted(order), n))
            
        # The Counter function from the collections library is used to count the frequency of each item in the menu list.
        menu_counts = Counter(menu)

        # The variable max_count is initialized to 2.
        max_count = 2

        # The for loop iterates through the items in the menu_counts dictionary sorted by frequency in descending order.
        # The variables menu_item and count represent the key and value of each item respectively.
        for menu_item, count in menu_counts.most_common():

            # If the frequency of the current menu item is greater than max_count, the item is added to the answer list and max_count is updated.
            if count > max_count:
                answer.append(''.join(menu_item))
                max_count = count
            # If the frequency of the current menu item is equal to max_count, the item is added to the answer list.
            elif count == max_count:
                answer.append(''.join(menu_item))
            # If the frequency of the current menu item is less than max_count, the loop is broken as we are only interested in the most frequent items.
            else:
                break

    # The answer list is sorted lexicographically.
    answer.sort()
    # The final answer list is returned.
    return answer