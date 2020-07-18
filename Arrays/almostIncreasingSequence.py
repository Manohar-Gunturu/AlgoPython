def almostIncreasingSequence(sequence):
    i = 0
    last = sequence[i]
    count = 0
    i = i + 1

    while i < len(sequence):

        if last > sequence[i]:
            count += 1
            # check if we can continue the sequence or start new one
            if len(sequence) > i + 1 and sequence[i + 1] >= last:
                pass
            else:
                last = sequence[i]
        else:
            last = sequence[i]

        if count > 1:
            return False

        i += 1

    return count <= 1


r = almostIncreasingSequence([1, 2, 1,  2])
print(r)
