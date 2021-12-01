# 461. Hamming Distance
def hammingDistance(x, y):
    x_bit = [0]
    y_bit = [0]
    for i in range(1,31):
        if x >= 2**i or y >= 2**i:
            x_bit.append(0)
            y_bit.append(0)
        else:
            break
    bit = len(x_bit)-1

    count = 0
    while bit >= 0:
        if x >= 2**bit:
            x_bit[len(x_bit)-1-bit] = 1
            x -= 2**bit
        if y >= 2**bit:
            y_bit[len(y_bit)-1-bit] = 1
            y -= 2**bit
        if x_bit[len(x_bit)-1-bit] != y_bit[len(y_bit)-1-bit]:
            count += 1
        bit -= 1

    return count
print(hammingDistance(8,7))