#lst = [1,5,8,12,15,20,59]
#tar = 15
def bs(lst,tar):
    lw = 0 
    hg = len(lst) -1 

    while lw <= hg:
        mid = (lw + hg) // 2
        if lst[mid] == tar:
            return f"our value exist in this data :: {lst[mid]}"
        elif lst[mid] < tar:
            lw = mid + 1
        else : 
            hg = mid - 1 
    return -1 
  
#print(bs([1,5,8,12,15,20,59], 15))


#  lw , high , get mid     on recursive we now exclude loop 


def recbs(arr, tar,lw,hg):
    if lw > hg:
        return -1 
    mid = (lw + hg) // 2 

    if arr[mid] == tar:
        return mid
    elif arr[mid] < tar :
        return recbs(arr, tar, mid+1, hg)
    else :
        return recbs(arr, tar, lw, mid -1)



arr = [3,4,5,6,6,62]

def count_num(arr):
    count = 0
    for i in arr :
        count += 1

    return count 
#print(count_num(arr))

def rcount_num(arr, count=0):
    if arr != NULL:
        new_arr = arr.pop()
        return rcount_num(new_arr, count+=1)
    return   count


rcount_num()

    


