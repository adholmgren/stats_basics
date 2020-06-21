def dot(a, b):
    sum_val = 0.
    for elem1, elem2 in zip(a, b):
        sum_val += elem1*elem2

    return sum_val

size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))
weighted_sum = dot(numbers, weights) / sum(weights)

print(f"{weighted_sum:.1f}")