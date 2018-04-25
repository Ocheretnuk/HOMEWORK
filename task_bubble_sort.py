def bubble_sort(lst):
    l = len(lst) 
    for k in range(l):
        for j in range(l-k-1):
            if lst[j+1] < lst[j]:
                a = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = a

    return lst