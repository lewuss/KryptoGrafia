import sympy
import random

p = 58603
q = 35051
n = p * q
seed = sympy.prime(random.randint(1000, 2000))
xs = [(seed * seed) % n]
key = ''

for x in range(20000):
    xi = (xs[-1] * xs[-1]) % n
    xs.append(xi)
    key += str(xi % 2)

print(key)

print(f'Number of 1 in key - {key.count("1")}')
print(f'Number of 0 in key - {key.count("0")}')

for min_length in range(2, 29):
    current_char = '1'
    subseq_length = 0
    subseq_count = 0

    for i in range(1, len(key)):
        if key[i] == current_char:
            subseq_length += 1
        else:
            if subseq_length > min_length:
                subseq_count += 1
            subseq_length = 1

    if subseq_length >= min_length:
        subseq_count += 1

    print(f"Minimum length {min_length}: {subseq_count}")

splitted = [key[i:i + 4] for i in range(0, 5000 * 4, 4)]

import collections

freq = collections.Counter(splitted)
sum = 0
for element, count in freq.items():
    print(f"{element}: {count}")
    sum += count * count

print(f"Poker test {(16 / 5000) * sum - 5000}")
