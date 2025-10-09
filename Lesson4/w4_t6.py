def collatz_sequence(n):
    steps = 0
    sequence = [str(n)]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(str(n))
        steps += 1

    return sequence, steps

print("Program starting.")
num = int(input("Insert a positive integer: "))

if num < 1:
    print("Invalid input. Please enter a positive integer.")
else:
    seq, total_steps = collatz_sequence(num)
    print(" -> ".join(seq))
    print(f"Sequence had {total_steps} total steps.")
    print("\nProgram ending.")


