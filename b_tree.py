# Longest Increasing Subsequence
"""
Optimal Substructure:
Let arr[0..n-1] be the input array and L(i) be the length of the LIS ending at index i such that arr[i] is the last element of the LIS.
Then, L(i) can be recursively written as:
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
Thus, we see the LIS problem satisfies the optimal substructure property as the main problem can be solved using solutions to subproblems.
"""


list = [62,92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83, 22]
listlen = len(list)


memlist = [1]*listlen#memlist[i] means   the length of the LIS ending at index i


def lic(a, n):
    global memlist
    if n==1:
        return 1
    lic_ = 1

    for i in range(n - 1):
        if(memlist[i]> 1):
            subproblem_lis_length = memlist[i]
        else:
            subproblem_lis_length = lic(a, i+1)
        if(a[n-1] > a[i] and lic_ < subproblem_lis_length+1):
            lic_ = subproblem_lis_length + 1
            memlist[n-1]=lic_

    return lic_

print lic(list, listlen)
print memlist

