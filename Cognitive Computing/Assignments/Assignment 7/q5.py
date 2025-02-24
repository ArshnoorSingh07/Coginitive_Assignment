def swap_set(s, elem1, elem2):
    s_list = list(s)
    i1, i2 = s_list.index(elem1), s_list.index(elem2)
    s_list[i1], s_list[i2] = s_list[i2], s_list[i1]
    return set(s_list)

# Example usage
sample_set = {"a", "b", "c", "d"}
print("Original Set:", sample_set)
print("Swapped Set:", swap_set(sample_set, "b", "d"))
