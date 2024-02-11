from functools import lru_cache
from math import sqrt
deret = [1, 2, 3]
suku1 = [3, 4, 7, 11, 18, 29]
suku2 = [2, 2, 4, 6, 10, 16, 26, 42]


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci_6 = fibonacci(6)
fibonacci_12 = fibonacci(12)
print(f"""
deret fibonaci:{deret}
bilangan ke-6:{fibonacci_6}
bilangan ke-12:{fibonacci_12}
""")


def generate_sequence_with_sum(n, data1, data2):
    sequence = [data1, data2]
    for i in range(2, n):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)
    for i in range(2, n):
        sum_result = sequence[i] + sequence[i - 1]
        print(
            f"Bilangan ke {i + 1}: {sequence[i]} + {sequence[i - 1]} = {sum_result}")


print(f"""
a.barisan:{suku1}
b.barisan:{suku2}
""")
print("lima suku berikutnya dari barisan a:")
generate_sequence_with_sum(11, 3, 4)
print("################################")
print("lima suku berikutnya dari barisan b:")
generate_sequence_with_sum(12, 2, 2)
