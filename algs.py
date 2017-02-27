def reverse(str):
    result = ""
    for i in range(len(str)):
        result.append(str[i])


# http://www.programcreek.com/2015/03/rotate-array-in-java/
def rotate(arr,k):
    if k == 0 or len(arr) < 2:
        return arr
    else:
        # if we don't iterate with a number, but with an array,
        # let's try a while loop
        while k > 0:
            tmp = arr[:-1]
            arr[:-1] = arr[0]
            arr[0] = tmp
            k = k+1
