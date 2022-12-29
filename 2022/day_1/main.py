def readfile():
    with open("input.txt", "r") as fd:
        multiLines = fd.read()
        fd.close()
        return multiLines


def aux():
    multiLines = readfile()

    lines = multiLines.split('\n\n')

    vectors = [[ int(data) for data in vec.split('\n') ] for vec in lines]

    return [sum(vec) for vec in vectors]


def main():
    l = aux()

    print(max(l))
    l.sort(reverse=True)
    print(sum(l[:3]))


if __name__ == "__main__":
    main()