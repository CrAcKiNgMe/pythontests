#PALIN - The Next Palindrome

groupstr = raw_input()
m = int(groupstr)
data = []
preset = []
postset = []
dict = {}
seq = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(seq)):
    dict[seq[i]] = 0


for i in range(m):
    n = int(raw_input())
    tmp = []
    tmppredic = {}
    tmppostdic = {}

    for i in range(len(seq)):
        tmppredic[seq[i]] = 0
    for i in range(len(seq)):
        tmppostdic[seq[i]] = 0

    for j  in range(n):
        word = raw_input()
        tmp.append(word)
        tmppredic[word[0]] += 1
        tmppostdic[word[len(word) -1]] -= 1
    data.append(tmp)
    preset.append(tmppredic)
    postset.append(tmppostdic)


for i in range(len(preset)):
    dicttmp1 = preset[i]
    dicttmp2 = postset[i]

    ndiffer = 0;

    for i in range(len(seq)):
        if( dicttmp1[seq[i]] > 0):
            ndiffer += dicttmp1[seq[i]] + dicttmp2[seq[i]]
        else:
            ndiffer -= dicttmp2[seq[i]]
    if(ndiffer > 2):
        print "The door cannot be opened."
    else:
        print "Ordering is possible."













