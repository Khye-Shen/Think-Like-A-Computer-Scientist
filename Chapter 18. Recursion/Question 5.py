l = [2, 9, [1, 13], 8, 6]

flat = []

def removeNestings(l):

    for i in l:
        if type(i) == list:
            removeNestings(i)
        else:
            flat.append(i)


    return flat



def findMinRec(l, n):


    if n == 1:
        return l[0]

    return min(l[n - 1], findMinRec(l, n - 1))




print findMinRec(removeNestings(l), len(removeNestings(l)))



