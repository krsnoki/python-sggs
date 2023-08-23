#write a program to print table from 2 to 10 using while and for loops and range function

for i in range(1,11):
    j = 1
    while j <= 10 :
        print("{0} x {1} = {2}\t".format(j, i,i*j), end = '\t')
        j += 1
    print(" ")
