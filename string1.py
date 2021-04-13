# calculate and return lenth of string
def lenthst(st):
    count=0
    for i in st:
          count=count+1
    return count

# generate and return a string of a given length of a chosen character as input
def setlength(set,k):
    n = len(set)
    Rec(set, "", n, k)
def Rec(set, p, n, k):
    if (k == 0) :
        print(p)
        return
    for i in range(n):
        new = p + set[i]
        Rec(set, new, n, k - 1)