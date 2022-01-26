from pickle import NONE

pos= - 1
i = NONE
def search(a,n):
    f = 0
    l = len(a)-1

    while f <= l:
        m = (f+l) // 2

        if a[m] == n:
            globals() ["pos"] = m
            globals() ["i"] = a[m] 
            return True
        else:
            if a[m]<n:
                f = m+1
            else:
                l = m-1

    return False

a = [5,30,70,90]
n = 90

if search(a,n):
    print("Number Found",i,pos+1)
else:
    print("Number Not Found")
