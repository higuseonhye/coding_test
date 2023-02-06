from collections import OrderedDict

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    answer = 0
    cache = OrderedDict()
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.move_to_end(city)
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.popitem(last=False)
            cache[city] = None
    return answer


"""
This is a Python function that implements a LRU cache (Least Recently Used Cache). It takes two arguments:

cacheSize: an integer representing the size of the cache
cities: a list of strings, representing the cities that will be processed in the cache
The function returns an integer representing the time taken to process all the cities in the list.

The function works as follows:
1. If the cache size is 0, the function immediately returns 5 * len(cities), meaning it takes 5 seconds to process each city.
2. The function initializes a variable answer to store the total processing time 
    and an ordered dictionary cache to store the processed cities.
3. For each city in cities, it first converts it to upper case and checks if it's in the cache.
4. If it is in the cache, the processing time is incremented by 1 second and the city 
    is moved to the end of the ordered dictionary, indicating it was just used.
5. If it is not in the cache, the processing time is incremented by 5 seconds and the ordered dictionary is checked for size. 
    If the size is equal to the cache size, the least recently used item is popped from the ordered dictionary. 
    The new city is then added to the cache.
6. The function returns the total processing time, answer.
"""
