from math import sqrt

def std_dev(input_list):
    n_elem = len(input_list)
    list_sum = sum(input_list)
    sqr_list_sum = sum(map(lambda x: x**2, input_list))
    return sqrt(sqr_list_sum / n_elem - (list_sum / n_elem)**2)

