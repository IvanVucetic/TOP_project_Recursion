def merge(a, b):
    list_ = []
    # until BOTH lists are empty:
    while (a != [] or b != []):
        # if both have elements left, compare those:
        if (a != [] and b != []):
            if a[0] <= b[0]:
                list_.append(a.pop(0))
            else:
                list_.append(b.pop(0))
        
        # once we added all from one list, add whats left from the other:
        elif (a == [] and b != []):
            list_.extend(b)
            del b[:]
        
        else:
            list_.extend(a)
            del a[:]
    
    return list_

# print merge([12, 14, 22],[5, 18])


def merge_sort(ary):
    if len(ary) == 1:
        return ary
    else:
        middle = len(ary) / 2
        left = merge_sort(ary[:middle])
        right = merge_sort(ary[middle:])
        return merge(left, right)


a = [12, 5, 6, 1, 3, 5, 22, 457, 88, 456, 23]
print merge_sort(a)