def reverse(str):
    result = ""
    for i in range(len(str)):
        result.append(str[i])
        
# http://www.programcreek.com/2015/03/rotate-array-in-java/
# helpful:
# http://stackoverflow.com/questions/17911091/append-integer-to-beginning-of-list-in-python
def rotate(arr,k):
    if k < 1 or len(arr) < 2:
        return arr
        
    else:
        # if we don't iterate with a number, but with an array,
        # let's try a while loop
 
    while k > 0:
            last_ele = [arr[-1]] # http://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list-in-python
            # both: [-2:-1] gives you the last element.
            shortened_arr = arr[:-1] # ignore the last element by triming it off
            arr = last_ele + shortened_arr
            k = k-1
    return arr
