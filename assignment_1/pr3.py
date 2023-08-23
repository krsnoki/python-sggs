# find average of user given array

def average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)

arr = [int(x) for x in input("Enter array elements: ").split()]
print("Average of array is: ", average(arr))