def gen_3bit_tree(idx, vector):

    if idx >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[idx] = num
        gen_3bit_tree(idx + 1, vector)


n = int(input())

vector = [0] * n
gen_3bit_tree(0, vector)