def construct_deconstruct(s):
    half = [s[:i] for i in range(1, len(s) + 1)]
    print(half + half[:-1][::-1])

construct_deconstruct('Привет')