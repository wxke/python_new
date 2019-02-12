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

data = list(range(10000))

random.shuffle(data)
quick_sort(data,0,len(data)-1)
print(data)