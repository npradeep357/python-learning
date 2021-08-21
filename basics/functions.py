import math


def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean


print("mean of [1, 2, 3, 4, 5, 6, 6, 7, 8, 12]",
      "=", mean([1, 2, 3, 4, 5, 6, 6, 7, 8, 12]))


def sq_area(area):
    # can also use area * area
    return math.pow(area, 2)


print(sq_area(2.2))
