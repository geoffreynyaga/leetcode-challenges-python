def array_advance(A):
    furthest_reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx


# a = [3, 3, 1, 0, 2, 0]
b = [1, 0, 0, 2, 1, 1]
# x = array_advance(a)
x1 = array_advance(b)

# print(x)
print(x1)
