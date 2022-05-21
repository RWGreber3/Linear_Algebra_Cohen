import copy

import numpy as np
import math


def factor_vector(vector):
    smallest_element = min(vector)
    possible_factors = []
    for i in range(smallest_element,1,-1):
        if smallest_element%i == 0:
            possible_factors.append(i)
    copy_possible_factors = copy.deepcopy(possible_factors)
    for i in copy_possible_factors:
        for j in vector:
            if j % i != 0:
                possible_factors.remove(i)
                break
    gcf = max(possible_factors)
    return_vector = []
    for i in vector:
        return_vector.append(i / gcf)
    return [gcf, return_vector]


a = [6,3,33,9]
b = [48,12,24,60]
c = [12,18,24]
d = [45,36,99,72,27]
print(factor_vector(a))
print(factor_vector(b))
print(factor_vector(c))
print(factor_vector(d))


