def array_sum(our_array, idx):
    if idx == len(our_array) - 1:
        return our_array[idx]

    return our_array[idx] + array_sum(our_array, idx + 1)


nums = [int(x) for x in input().split()]

print(array_sum(nums, 0))
