Example program output:

Enter number of process: 3
Process A
Enter arrival time: 15
Enter burst time: 40
Process B
Enter arrival time: 18
Enter burst time: 10
Process C
Enter arrival time: 5
Enter burst time: 2
|Processes      |Arrival Time   |Burst Time     |Completion Time|Turnaround Time|Waiting Time   |
|Process A      |15             |40             |55             |40             |0              |
|Process B      |18             |10             |65             |47             |37             |
|Process C      |5              |2              |7              |2              |0              |
====================
Gantt Chart:
|IDLE           |Process C      |IDLE           |Process A      |Process B      |
0               5               7               15              55              65
====================
Total Turnaround Time:  89 ms
Total Waiting Time:  37 ms
Average Turnaround Time:  29.666666666666668 ms
Average Waiting Time:  12.333333333333334 ms