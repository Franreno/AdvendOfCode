# A, X -> PEDRA (1 PT)
# B, Y -> PAPEL (2 PT)
# C, Z -> TESOURA (3 PT)

# GANHAR (6 PT)
# EMPATAR (3 PT)
# PEREDR (0 PT)

def readfile() -> str:
    with open("input.txt", "r") as fd:
        multiLines = fd.read()
        fd.close()
        return multiLines


def convert(data: str) -> tuple[str, int]:
    return (("A", 1) if data == "X" else ("B", 2) if data == "Y" else ("C", 3))


def hasWon(a: str, b: str):
    return ((a == "A" and b == "B") or (a == "B" and b == "C") or (a == "C" and b == "A"))


"""
PARTE 2
X -> TEM QUE PERDER
Y -> EMPATAR
Z -> GANHAR
"""

def needToWin(a: str):
    return (2 if a == "A" else 3 if a == "B" else 1)


def needToTie(a: str):
    return (1 if a == "A" else 2 if a == "B" else 3)


def needToLose(a: str):
    return (3 if a == "A" else 1 if a == "B" else 2)


def main():
    score1 = 0
    score2 = 0
    multilines = readfile().split('\n')

    plays = [[data for data in play.split()] for play in multilines]

    for play in plays:
        converted, value = convert(play[1])
        score1 += value + \
            (3 if play[0] == converted else 6 if hasWon(
                play[0], converted) else 0)

        score2 += (needToWin(play[0]) + 6 if converted == "C" else needToLose(
            play[0]) if converted == "A" else needToTie(play[0]) + 3)

    print(score1, score2)


if __name__ == "__main__":
    main()
