import random
def maopao(data):
    for i in range(len(data)-1):
        for j in range(len(data) - i -1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

def select_sort(data):
    for i in range(len(data)-1):
        tmp = i
        for j in range(i+1,len(data)):
            if data[j] <data[tmp]:
                tmp = j
        data[i],data[tmp] = data[tmp],data[i]

def insert_sort(data):
    for i in range(1,len(data)):
        tmp = data[i]
        j = i - 1
        while j >=0:
            if tmp <data[j]:
                data[j+1] = data[j]
                j = j - 1
            else:
                break
        data[j+1] = tmp

def quick_sort(data,left,right):
    l = left
    r = right
    if l < r:
        tmp = data[l]
        while l < r:
            while l < r and data[r] > tmp:
                r -= 1
            while l < r and data[l] <tmp:
                l += 1
            data[l],data[r] = data[r],data[l]
        data[l] = tmp
        mid = l
        quick_sort(data,mid+1,right)
        quick_sort(data,left,mid-1)

def make_dui_sort(data,low,high):
    i = low
    j = 2*i+1
    tmp = data[i]
    while j <= high:
        if j < high and data[j+1] > data[j]:
                j = j+1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2*i+1
        else:
            break
    data[i] = tmp

def dui_sort(data):
    n = len(data)
    for i in range(n//2-1,-1,-1):
        make_dui_sort(data,i, n-1)
    for i in range(n):
        data[n-1-i],data[0] = data[0],data[n-1-i]
        make_dui_sort(data,0,n-i-2)

def merge(data,low,mid,high):
    i = low
    j = mid + 1
    li = []
    while i <= mid and j <= high:
        if data[i] <= data[j]:
            li.append(data[i])
            i += 1
        else:
            li.append(data[j])
            j += 1
    while i <= mid:
        li.append(data[i])
        i += 1
    while j <= high:
        li.append(data[j])
        j += 1
    data[low:high+1] = li

def mergesort(data,low,high):
    if low < high:
        mid = (low + high) // 2
        mergesort(data,low,mid)
        mergesort(data,mid+1,high)
        merge(data,low,mid,high)

def use_mergesort(data):
    mergesort(data,0,len(data)-1)


def shell_sort(data):
    flag = len(data) // 2
    while flag:
        for i in range(flag,len(data)):
            tmp = data[i]
            j = i - flag
            while j>=0 and data[j] > tmp:
                data[j + flag] = data[j]
                j = j - flag
            data[j + flag] = tmp
        flag //= 2
data = list(range(10))
random.shuffle(data)
shell_sort(data)
print(data)
