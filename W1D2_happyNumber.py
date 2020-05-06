from math import pow


def isHappy(n):
    s = set()

    while (n != 1):
        if n in s:
            # if n is already in SET => Endless Loop => False
            return False
        s.add(n)
        n = int(sum([pow(int(d), 2) for d in str(n)]))

    return True


def main():
    print(isHappy(2))


if __name__ == "__main__":
    main()
