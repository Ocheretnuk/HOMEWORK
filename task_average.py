def average(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    avr = round(sum/len(lst),3)

    return avr