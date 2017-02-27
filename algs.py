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
            last_ele = arr[-2:-1] # -2 is second last, -1 is last
            arr = arr[:-1] # ignore the last element by triming it off
            arr.append(last_ele) # append puts stuff at FRONT

            k = k-1

    return arr

print (rotate([1,2,3,4],2))
