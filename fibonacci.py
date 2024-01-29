def generate_fibonacci(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

def print_fibonacci(sequence):
    print("Fibonacci Sequence:")
    for num in sequence:
        print(num, end=" ")
    print()

# Specify the maximum value for Fibonacci numbers
max_value = 50

# Generate and print the Fibonacci sequence up to max_value
fibonacci_sequence = generate_fibonacci(max_value)
print_fibonacci(fibonacci_sequence)
