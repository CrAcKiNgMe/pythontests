'''
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation). Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ). Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).

Input

t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
Text grouped in [ ] does not appear in the input file.

Output

The expressions in RPN form, one per line.
Example

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
'''
n = raw_input()
n = int(n)

dic = {"+":0,"-":0,"*":1,"/":1,"(":3, ")":3, "^":2}
exps = []

for i in range(n):
    rawdata = raw_input()
    rawdata = filter(None, rawdata)
    exps.append(rawdata)


def printexp(exp):
    tmpstack = []
    explist = []
    for i in range(len(exp)):
        if(exp[i]<= 'z' and exp[i] >= 'a'):
            explist.append(exp[i])
        elif(exp[i] == '('):
            tmpstack.append(exp[i])
        elif(exp[i] == ')'):
            while(len(tmpstack) and tmpstack[len(tmpstack) - 1] != '('):
                explist.append(tmpstack.pop())
            if (len(tmpstack)):
                tmpstack.pop()
        elif(len(tmpstack) == 0 or dic[exp[i]] > dic[tmpstack[len(tmpstack)-1]]):
            tmpstack.append(exp[i])
        else:
            while(len(tmpstack) and dic[exp[i]] <= dic[tmpstack[len(tmpstack)-1]]):
                if(tmpstack[len(tmpstack) - 1] != '('):
                    explist.append(tmpstack.pop())
                else:
                    break
            tmpstack.append(exp[i])

    print "".join(explist)












for i in range(n):
    printexp(exps[i])



