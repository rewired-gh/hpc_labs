import numpy as np

print(3)

def print_samples(a, b, c):
    print(a)
    print(b)

    arr = np.random.default_rng().uniform(low=0.0, high=100.0, size=a*b)

    for num in arr:
        print(np.around(num, 6))

    print(b)
    print(c)

    arr = np.random.default_rng().uniform(low=0.0, high=100.0, size=b*c)

    for num in arr:
        print(np.around(num, 6))

print_samples(1000, 3, 50)
print_samples(200, 400, 300)
print_samples(1024, 1024, 1024)

print()
