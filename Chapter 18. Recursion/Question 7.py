l = [2,9,[2,1,13,2],8,[2,6]]

flat = []



def flatten(l):

    for i in l:
        if type(i) == list:
            flatten(i)
        else:
            flat.append(i)


    return flat


print(flatten(l))

