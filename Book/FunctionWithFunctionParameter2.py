def nextNum():
    n += 1
    return n;

def m(t, f):
    for i in range(len(t)):
        t[i] = f()

def main():
    list = [0] * 4
    m(list, nextNum)
    for i in range(4):
        print(list[i], end = " ")
    print()

main()