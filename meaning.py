import math

meaning = 42
print('')

# if meaning > 10:
#     print('Right on!')
# else:
#     print('Not Today')

# Ternary Operator
print('Right on!') if meaning < 10 else print('Not today')
print(math.pi)
print(math.tan(90))

a = [1, 2, 3, 4, 5]
b = [4, 3, 3, 2, 1, 8, 7]


def merge_arrays(arrayA, arrayB):
    return sorted(set(arrayA + arrayB))


merged = merge_arrays(a, b)
print(merged)

c = sorted(set(a).union(set(b)))
print(c)

e = set().union(a, b)
print(e)

d = list(sorted(set().union(a, b)))
print(d)
