"""Find quantiles

e.g. 1, 2, 3 -> 1, 2, 3
n_elems = 3
low_idx = 1
median_val = 2
e.g. 1, 2, 3, 4 -> 1.5, 2.5, 3.5
"""

def quartile(ordered_arr: list, ret_arr: list, stack: int) -> float:
    if stack > 1:
        return
    n_elems = len(ordered_arr)
    if stack == 0 and n_elems < 3:
        raise ValueError("Array must have at least 3 elements")
    low_idx = n_elems // 2
    if n_elems % 2 == 0:
        median_val = (ordered_arr[low_idx - 1] + ordered_arr[low_idx]) / 2
        ret_arr.append(median_val)
        stack += 1
        quartile(ordered_arr[:low_idx], ret_arr, stack)
        quartile(ordered_arr[low_idx:], ret_arr, stack)
    else:
        median_val = ordered_arr[low_idx]
        ret_arr.append(median_val)
        stack += 1
        quartile(ordered_arr[:low_idx], ret_arr, stack)
        quartile(ordered_arr[low_idx+1:], ret_arr, stack)

if __name__ == "__main__":
    ret_arr = []
    # input_list = [1, 5, 4]
    input_list = [3, 7, 8, 5, 12, 14, 21, 13, 18]
    sorted_list = sorted(input_list)
    quartile(sorted_list, ret_arr, 0)
    print(ret_arr[1])
    print(ret_arr[0])
    print(ret_arr[-1])