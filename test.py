n = raw_input()
n = int(n)

dic = {"+":0,"-":0,"*":1,"/":1,"(":2, ")":3}
exps = []

for i in range(n):
    rawdata = raw_input()
    rawdata = filter(None, rawdata)
    exps.append(rawdata)


def printexp(exp):
    tmpstack = []
    for i in range(len(exp)):
        if(exp[i]<= 'z' and exp[i] >= 'a'):
            print exp[i]
        elif(exp[i] == '('):
            tmpstack.append(exp[i])
        elif(exp[i] == ')'):
            while(len(tmpstack) and tmpstack[len(tmpstack) - 1] != '('):
                print tmpstack.pop()
            if (len(tmpstack)):
                tmpstack.pop()
        elif(len(tmpstack) == 0 or dic[exp[i]] > dic[tmpstack[len(tmpstack)-1]]):
            tmpstack.append(exp[i])
        else:
            while(len(tmpstack) and dic[exp[i]] <= dic[tmpstack[len(tmpstack)-1]]):
                if(dic[tmpstack[len(tmpstack)-1]] != '('):
                    print tmpstack.pop()
            tmpstack.append(exp[i])












for i in range(n):
    printexp(exps[i])



