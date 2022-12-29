def readfile() -> str:
    with open("input.txt", "r") as fd:
        multiLines = fd.read()
        fd.close()
        return multiLines


def main():
    multiLines = readfile().split('\n')

    score = 0
    for line in multiLines:
        _len = len(line)
        lower = set(line[:_len//2])
        upper = set(line[_len//2:])
        # A: 65, Z: 90
        # a: 97, z: 122
        inter = ord(lower.intersection(upper).pop())
        score += (inter - 96 if inter >= 97 and inter <=
                122 else (inter - 64)+26)

    print(score)


if __name__ == "__main__":
    main()
