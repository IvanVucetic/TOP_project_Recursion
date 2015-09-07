def merge(a, b):
    list_ = []
    for i in range(len(a if [a > b] else b)):
        if a[i] <= b[i]:
            list_.append(a[i])
            list_.append(b[i])
        else:
            list_.append(b[i])
            list_.append(a[i])
    return list_

# print merge(12,5)


def merge_sort(ary):
    if len(ary) == 1:
        return ary
    else:
        middle = len(ary) / 2
        left = merge_sort(ary[:middle])
        right = merge_sort(ary[middle:])
        return merge(left, right)

a = [12, 5, 6, 1, 3, 5]
b = [2]


print merge_sort(a)