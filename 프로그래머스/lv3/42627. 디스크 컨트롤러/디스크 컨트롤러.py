import heapq

def solution(jobs):
    running_time = -1 # 현재 진행중인 작업
    waiting_jobs = []
    total_time = 0
    num_jobs = len(jobs)

    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))  # 일찍 시작하고, 시간이 짧은 순으로 
    job_index = 0

    while True:
        if not waiting_jobs and job_index >= num_jobs:
            break

        if running_time == -1 or (job_index < num_jobs and running_time < jobs[job_index][0] and not waiting_jobs):
            start_time, duration = jobs[job_index]
            total_time += duration
            running_time = start_time + duration
            job_index += 1
            continue

        while job_index < num_jobs: # 입력칸 -> 대기열로 올려줄때 
            if running_time >= jobs[job_index][0]:
                start_time, duration = jobs[job_index]
                heapq.heappush(waiting_jobs, [duration, start_time])
                job_index += 1
            else: 
                break    

        while waiting_jobs: # 대기열 -> 실행열에 쌓기
            duration, start_time = heapq.heappop(waiting_jobs)
            total_time += running_time - start_time + duration # 지연시간 + 처리시간 
            running_time += duration # 끝나는 시간 업데이트 
            break # 대기열 -> 실행열로 1회 수행 이후엔 바로 다음 jobs 목록을 확인해야한다.

    return total_time // num_jobs
