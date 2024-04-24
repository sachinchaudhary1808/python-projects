def energy():
    MASS = int(input("m: "))
    cSquer = pow(300000000, 2)
    return MASS * cSquer


def main():
    E = energy()
    print(E)


main()
