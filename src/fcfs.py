# With this iteration of the code, we're making processes into objects, collecting related information together


class Process:
    """Stores information about a single simulated process"""

    def __init__(self, name, arrival_time, burst_time):
        """Create a new process with the given name, arrival time, and burst time"""
        self.process_name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
    
    def run(self, start_time):
        """Simulates running the process starting at start_time.

        Returns the completion time of the process
        """
        # The time the process completed
        self.completion_time = start_time + self.burst_time

        # Turnaround time = the time between when the process arrived and when it completed
        self.turnaround_time = self.completion_time - self.arrival_time

        # Wait time = the turnaround time minus the time we actually spent doing work
        self.wait_time = self.turnaround_time - self.burst_time
        return self.completion_time



gantt_t = []
gantt_b = [0]

def main():
    process_list = get_input()
    simulate_process_execution(process_list)
    print_output(process_list)


def get_input():
    """Reads our simulated process information from user input
    """
    process_list = []

    process = int(input("Enter number of process: "))
    for i in range(0, process):
        process_name = "Process " + chr(i + ord('A'))
        process_list.append(get_process_info(process_name))

    return process_list

def get_process_info(process_name):
    """Reads a single process from user input
    """
    print(process_name)
    at = int(input("Enter arrival time: "))
    bt = int(input("Enter burst time: "))
    return Process(process_name, at, bt)

def sort_by_arrival_time(process_list):
    """Sorts our process list by arrival time and returns the newly-sorted list
    """
    # Make a copy since list sorting occurs in place
    sorted_list = process_list.copy()
    sorted_list.sort(key = lambda process: process.arrival_time)
    return sorted_list

def simulate_process_execution(process_list):
    """Simulates executing the processes in a first-come, first-served manner
    """
    # Get a new copy of our process list, sorted by arrival times
    sorted_list = sort_by_arrival_time(process_list)

    time = 0
    
    # Continue as long as there are processes to execute
    while sorted_list:

        # If a new process is ready to start, start it now
        if time >= sorted_list[0].arrival_time:

            # Simulate our process running for its burst time
            current_process = sorted_list.pop(0)
            time = current_process.run(time)

            gantt_t.append(current_process.process_name)
            gantt_b.append(time)
        else:
            gantt_t.append("IDLE")
            time = sorted_list[0].arrival_time
            gantt_b.append(time)


def calculate_summary_stats(process_list):
    """Calculates statistics from our code execution

    Note that process-level statistics calculation now happens in Process.run
    """
    total_tat = total_wt = ave_tat = ave_wt = 0


    for process in process_list:
        total_tat += process.turnaround_time
        total_wt += process.wait_time
    ave_tat = total_tat / len(process_list)
    ave_wt = total_wt / len(process_list)

    return {'total_tat': total_tat, 'total_wt': total_wt, 'ave_tat': ave_tat, 'ave_wt': ave_wt}

def print_output(process_list):
    """Renders output to the user
    """
    print_process_stats(process_list)
    print_separator()
    
    print_gantt_chart()
    print_separator()

    summary_stats = calculate_summary_stats(process_list)
    print_overall_stats(summary_stats)

def print_process_stats(process_list):
    """Prints information about each process
    """
    print("|Processes      |Arrival Time   |Burst Time     |Completion Time|Turnaround Time|Waiting Time   |")
    for process in process_list:
        print("|" + str(process.process_name), end='')
        for j in range(15, len(str(process.process_name)), -1):
            print(" ", end='')
        print("|" + str(process.arrival_time), end='')
        for j in range(15, len(str(process.arrival_time)), -1):
            print(" ", end='')
        print("|" + str(process.burst_time), end='')
        for j in range(15, len(str(process.burst_time)), -1):
            print(" ", end='')
        print("|" + str(process.completion_time), end='')
        for j in range(15, len(str(process.completion_time)), -1):
            print(" ", end='')
        print("|" + str(process.turnaround_time), end='')
        for j in range(15, len(str(process.turnaround_time)), -1):
            print(" ", end='')
        print("|" + str(process.wait_time), end='')
        for j in range(15, len(str(process.wait_time)), -1):
            print(" ", end='')
        print("|")

def print_separator():
    """Prints a separator in between sections of output
    """
    print("====================")

def print_gantt_chart():
    """Prints a gantt chart showing processor utilization
    """
    print("Gantt Chart:")

    for i in range(0, len(gantt_t)):
        print("|" + gantt_t[i], end='')
        for j in range(15, len(str(gantt_t[i])), -1):
            print(" ", end='')
    print("|")
    for i in range(0, len(gantt_b)):
        print(str(gantt_b[i]), end='')
        for j in range(16, len(str(gantt_b[i])), -1):
            print(" ", end='')
    print("")


def print_overall_stats(summary_stats):
    """Prints a summary of statistics across all processes
    """
    print("Total Turnaround Time: ", summary_stats['total_tat'], "ms")
    print("Total Waiting Time: ", summary_stats['total_wt'], "ms")
    print("Average Turnaround Time: ", summary_stats['ave_tat'], "ms")
    print("Average Waiting Time: ", summary_stats['ave_wt'], "ms")

# If this module is called as the main script, run the main method:
if __name__ == "__main__":
    main()