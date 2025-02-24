def swap_list(lst, idx1, idx2):
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp
    return lst

# Example usage
sample_list = [1, 2, 3, 4]
print("Original List:", sample_list)
print("Swapped List:", swap_list(sample_list, 1, 3))
