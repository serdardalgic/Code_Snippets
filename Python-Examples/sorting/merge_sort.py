def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    middle = len(unsorted_list) / 2
    left = unsorted_list[:middle]
    right = unsorted_list[middle:]
    print "divided into:", left, right
    left = merge_sort(left)
    right = merge_sort(right)
    print "--> input to merge:", left, right
    return merge(left, right)


def merge(left_sublist, right_sublist):
    result = []
    while len(left_sublist) > 0 or len(right_sublist) > 0:
        if len(left_sublist) > 0 and len(right_sublist) > 0:
            if left_sublist[0] < right_sublist[0]:
                result.append(left_sublist[0])
                left_sublist = left_sublist[1:]
            else:
                result.append(right_sublist[0])
                right_sublist = right_sublist[1:]
        elif len(left_sublist) > 0:
            result.extend(left_sublist)
            left_sublist = []
        elif len(right_sublist) > 0:
            result.extend(right_sublist)
            right_sublist = []

    print "<-- output of merge:", result
    return result
