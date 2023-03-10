import heapq

def solution(jobs):
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[0])  # Sort jobs by request time
    answer, start_time = 0, 0
    heap = []  # Heap to keep jobs by their required time

    while heap or jobs:
        # Add jobs that arrived while the previous job was running to the heap
        while jobs and jobs[0][0] <= start_time:
            request, required = jobs.pop(0)
            heapq.heappush(heap, (required, request))

        # If the heap is not empty, take the job with minimum required time
        if heap:
            required, request = heapq.heappop(heap)
            start_time += required
            answer += start_time - request
        # Otherwise, jump to the next job's request time
        else:
            start_time = jobs[0][0]

    return answer // n


"""
The solution uses a heap to keep track of the jobs that are currently waiting to be processed. 
It starts by sorting the jobs by their request time and then iterates through the list, 
    adding jobs to the heap as they arrive and processing jobs in the heap as they become available. 
The answer is calculated as the sum of the time it takes to complete each job divided by the number of jobs.
"""
