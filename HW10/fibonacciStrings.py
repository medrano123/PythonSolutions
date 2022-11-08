def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    if (n >= 1):
        fibbonicci = str(fibonacci(n - 1)) + str(fibonacci(n - 2))
        return fibbonicci


def counter(sequence, p):
    i = 0
    sequence_count = 0
    # Search through the string till
    # we reach the end of it
    while (i < len(sequence)):
        current_position = sequence.find(p, i)

        if current_position != -1:
            i = current_position + 1
            sequence_count += 1

        if (current_position == -1):
            break
    return sequence_count


def main():
    sequence = fibonacci(30)
    p = str(1011)
    count = counter(sequence, p)
    print(count)


main()

