def f1(value):
    return 2 * value

def f2(value):
    return 3 * value

def m(t, f):
    for i in range(len(t)):
        t[i] = f(t[i])

def main():
    list1 = [1, 2, 3, 4]
    m(list1, f1)
    for i in range(0, 4):
        print(list1[i], end = " ")
    print()
  
    list2 = [1, 2, 3, 4]
    m(list2, f2)
    for i in range(0, 4):
        print(list2[i], end = " ")
    print()

main()