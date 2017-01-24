#No. 03 - Maximum Sum of All Sub-arrays
"""
If we have a deep understanding of algorithm, we may solve this problem with dynamic programming.
If function f(i) stands for the maximum sum of a sum-array ended with the ith number,
 what it is to get is max[f(i)].
"""


a = list([1, -2, 3, 10, -4, 7, 2, -5])





for i in range(len(a) - 1):
    if(a[i] > 0):
        a[i+1] += a[i]

for i in range(len(a) - 1):
    if(a[i+1] > a[0]):
        a[0] = a[i+1]

print a[0]