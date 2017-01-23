def insertion_sort(unsorted):
    for i,c in enumerate(unsorted):
        while i > 0:
            if c < unsorted[i-1]:
                # swap
                temp = unsorted[i-1]
                unsorted[i-1] = c
                unsorted[i] = temp
            i -= 1
    return unsorted
