def m(n):
    result = 0
    for i in range(1, n + 1):
        result += (2 * i + 1) / (3 * i - 2)
    return result
 
def main():
    print(format("n", ">15s"), format("m(n)", ">15s"))
    print("-------------------------------------------")
    for n in range(1, 11):
        print(format(n, "15d"), format(m(n), "15.2f"))

main()