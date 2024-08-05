# Subtraction
448
My little brother is learning math, can you show him how to do some subtraction problems? Author: Connor Chang

# Attachments
server.py

# Walkthrough
Given Values
Start with 
𝑛 = 696969
Each step, reduce the current value by half, using the ceiling function.
Repeat until  𝑛 becomes 0 or less.

The while loop runs as long as n is non-zero.

From n00bz Official writeup
 If you always choose the ceil of the maximum value of the current array divided by two, you can divide the max value by half every time and you are garunteed to solve it in log2(696969) < 30.

# Flag
n00bz{1_sh0uld_t34ch_my_br0th3r_logs}