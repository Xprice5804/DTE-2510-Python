def reverseMultiTable(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            print(format(i * j, "<5d"), end = "")
        print()
            
reverseMultiTable(5)  
