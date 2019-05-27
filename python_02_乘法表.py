
def fun():
    #  计算0-100之间的数字求和
    i = 0
    sum = 0
    while i <= 3:
        sum = sum + i
        print(i)
        i = i + 1
    print(sum)
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d =%d" %(col,row,col*row), end="\t")
            col += 1
        print("")
        row += 1

    #  打印一个乘法表
    row1 =1
    col1 =1
    for row1 in range (1,10):
        for col1 in range (1,row1+1):
            print("%d * %d =%d" % (col1, row1, col1 * row1), end="\t")
            col1 += 1

        print("")
        row1 += 1




