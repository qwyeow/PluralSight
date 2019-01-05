import sys
from itertools import count, islice

# example of recamen series: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9]

def sequence():
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c    


def write_sequence(filename, num):
    with open(filename, "wt", encoding = "utf-8") as f:
        f.writelines(f"{r} \n" for r in islice(sequence(), num))

if __name__ == "__main__":
    write_sequence(filename = sys.argv[1],
                   num = int(sys.argv[2]))
