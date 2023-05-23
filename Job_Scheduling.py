def schedule_jobs(jobs):
    # Sort the jobs based on their profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find the maximum deadline among all jobs
    max_deadline = max(jobs, key=lambda x: x[1])[1]

    # Array to store the time slots for each job
    time_slots = [-1] * max_deadline

    # Fill the time slots for each job
    total_profit = 0
    for job in jobs:
        # Find the latest available slot before the deadline
        slot = job[1] - 1
        while slot >= 0 and time_slots[slot] != -1:
            slot -= 1

        # If a slot is found, assign the job to that slot
        if slot >= 0:
            time_slots[slot] = job[0]
            total_profit += job[2]

    # Display the scheduled jobs and total profit
    print("Scheduled Jobs:", end=" ")
    for job_id in time_slots:
        if job_id != -1:
            print(job_id, end=" ")
    print("\nTotal Profit:", total_profit)


num_jobs = int(input("Enter the number of jobs: "))

jobs = []
print("Enter job details (id, deadline, profit):")
for i in range(num_jobs):
    job_id, deadline, profit = map(int, input(f"Job {i+1}: ").split())
    jobs.append((job_id, deadline, profit))

# Schedule the jobs and display the result
schedule_jobs(jobs)