
process = int(input("Enter number of process: "))
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
for i in range(0, process):
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
atlsort.sort()
ind = 0
ganttct = 0
gantt_tc = 0
gantt_bc = 0
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
while True:
    for i in range(0, process):
        tatl[i] = ctl[i] - atl[i]
        wtl[i] = tatl[i] - btl[i]
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
    break
print("====================")
print("Gantt Chart:")
while True:
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
    break
print("====================")
total_tat = total_wt = ave_tat = ave_wt = 0
for i in range(0, process):
    total_tat = total_tat + tatl[i]
    total_wt = total_wt + wtl[i]
ave_tat = total_tat / process
ave_wt = total_wt / process
print("Total Turnaround Time: ", total_tat, "ms")
print("Total Waiting Time: ", total_wt, "ms")
print("Average Turnaround Time: ", ave_tat, "ms")
print("Average Waiting Time: ", ave_wt, "ms")
