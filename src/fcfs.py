# For now we're leaving these as global variables, to be cleaned up in the next iteration of the code
# Having multiple lists where corresponding values are conceptually related is a code smell that usually
# indicates we should be looking to a list of more complex data types (dictionaries / objects)

gantt_t = []
gantt_b = [0]
prl = []
atl = []
btl = []
ctl = []
tatl = []
wtl = []
atlcopy = []
atlsort = []
ganttct = 0
gantt_tc = 0
gantt_bc = 0
process = 0
total_tat = total_wt = ave_tat = ave_wt = 0

def main():
    get_input()
    simulate_process_execution()
    calculate_statistics()
    print_output()


def get_input():
    """Reads our simulated process information from user input
    """
    global process
    process = int(input("Enter number of process: "))
    for i in range(0, process):
        get_process_info(i)

def get_process_info(i):
    """Reads a single process from user input
    """
    print("Process", chr(i + 65))
    prl.append("Process " + chr(i + 65))
    at = int(input("Enter arrival time: "))
    atl.append(at)
    atlsort.append(at)
    atlcopy.append(at)
    bt = int(input("Enter burst time: "))
    btl.append(bt)
    ctl.append(bt)
    tatl.append(bt)
    wtl.append(bt)

def sort_by_arrival_time():
    """Sorts our process list by arrival time
    """
    atlsort.sort()

def simulate_process_execution():
    """Simulates executing the processes in a first-come, first-served manner
    """
    global ganttct,gantt_tc,gantt_bc

    sort_by_arrival_time()

    ind = 0
    while True:
        if ganttct >= atlsort[ind]:
            gantt_t.append("Process " + chr(atlcopy.index(atlsort[ind]) + 65))
            ganttct = ganttct + btl[atlcopy.index(atlsort[ind])]
            ctl[atlcopy.index(atlsort[ind])] = ganttct
            atlcopy[atlcopy.index(atlsort[ind])] = -1
            gantt_b.append(ganttct)
            ind = ind + 1
            gantt_tc = gantt_tc + 1
            gantt_bc = gantt_bc + 1
        else:
            gantt_t.append("IDLE")
            ganttct = atlsort[ind]
            gantt_b.append(ganttct)
            gantt_tc = gantt_tc + 1
            gantt_bc = gantt_bc + 1
        if ind == process:
            break
def calculate_statistics():
    """Calculates statistics from our code execution
    """
    global total_tat,  total_wt,  ave_tat, ave_wt

    for i in range(0, process):
        tatl[i] = ctl[i] - atl[i]
        wtl[i] = tatl[i] - btl[i]
        total_tat = total_tat + tatl[i]
        total_wt = total_wt + wtl[i]
    ave_tat = total_tat / process
    ave_wt = total_wt / process

def print_output():
    """Renders output to the user
    """
    print_process_stats()
    print_separator()
    print_gantt_chart()
    print_separator()
    print_overall_stats()

def print_process_stats():
    """Prints information about each process
    """
    print("|Processes      |Arrival Time   |Burst Time     |Completion Time|Turnaround Time|Waiting Time   |")
    for i in range(0, process):
        print("|" + str(prl[i]), end='')
        for j in range(15, len(str(prl[i])), -1):
            print(" ", end='')
        print("|" + str(atl[i]), end='')
        for j in range(15, len(str(atl[i])), -1):
            print(" ", end='')
        print("|" + str(btl[i]), end='')
        for j in range(15, len(str(btl[i])), -1):
            print(" ", end='')
        print("|" + str(ctl[i]), end='')
        for j in range(15, len(str(ctl[i])), -1):
            print(" ", end='')
        print("|" + str(tatl[i]), end='')
        for j in range(15, len(str(tatl[i])), -1):
            print(" ", end='')
        print("|" + str(wtl[i]), end='')
        for j in range(15, len(str(wtl[i])), -1):
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

    for i in range(0, gantt_tc):
        print("|" + gantt_t[i], end='')
        for j in range(15, len(str(gantt_t[i])), -1):
            print(" ", end='')
    print("|")
    for i in range(0, gantt_bc + 1):
        print(str(gantt_b[i]), end='')
        for j in range(16, len(str(gantt_b[i])), -1):
            print(" ", end='')
    print("")


def print_overall_stats():
    """Prints a summary of statistics across all processes
    """
    print("Total Turnaround Time: ", total_tat, "ms")
    print("Total Waiting Time: ", total_wt, "ms")
    print("Average Turnaround Time: ", ave_tat, "ms")
    print("Average Waiting Time: ", ave_wt, "ms")

# If this module is called as the main script, run the main method:
if __name__ == "__main__":
    main()