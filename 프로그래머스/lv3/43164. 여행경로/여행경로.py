def solution(tickets):
    # create a dictionary to store the flights departing from each airport
    flights = {}
    for a, b in tickets:
        if a not in flights:
            flights[a] = []
        flights[a].append(b)

    # sort the flights for each airport in lexicographic order
    for a in flights:
        flights[a].sort()

    # use backtracking to find the route
    route = []
    def backtrack(curr):
        nonlocal route
        if len(route) == len(tickets) + 1:  # found a valid route
            return True
        if curr not in flights:
            return False
        for i, next_airport in enumerate(flights[curr]):
            flights[curr].pop(i)  # remove the flight from the dictionary
            route.append(next_airport)
            if backtrack(next_airport):
                return True
            flights[curr].insert(i, next_airport)  # add the flight back to the dictionary
            route.pop()
        return False

    # start the backtracking from the given start airport
    route.append("ICN")
    backtrack("ICN")

    return route
