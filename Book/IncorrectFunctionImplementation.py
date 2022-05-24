def m(n):
    return (2 * n + 1) / (3 * n - 2)
 
def main():
    print(format("n", ">15s"), format("m(n)", ">15s"))
    print("-------------------------------------------")
    for n in range(1, 11):
        result = 0;
        for i in range(1, n + 1):
            result += m(i)

        print(format(n, "15d"), format(result, "15.2f"))

main()