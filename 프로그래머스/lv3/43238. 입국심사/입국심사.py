def solution(n, times):
    # Sort the given times list in ascending order
    times.sort()
    # Initialize the minimum and maximum time it can take to process all applicants
    left, right = 1, n * times[-1]
    
    while left <= right:
        # Calculate the mid time
        mid = (left + right) // 2
        # Calculate the number of applicants that can be processed with the mid time
        count = 0
        for t in times:
            count += mid // t
            if count >= n:
                break
        
        # If the number of processed applicants is greater than or equal to n, 
        # it means that we can process all applicants with the given mid time or less.
        # So, we update the right bound to mid-1.
        if count >= n:
            right = mid-1
        # Otherwise, the given time is not enough to process all applicants. 
        # So, we update the left bound to mid+1.
        else:
            left = mid+1
    
    # Return the minimum time required to process all applicants
    return left
