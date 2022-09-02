def insertationSort(arr):
    
    for i in range(1, len(arr)):
        
        key=arr[i]
        print(key)
        
        j=i-1
        print(j) 
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            print(arr)
            j-=1
            print(j)
        arr[j+1]=key
        print(arr)
arr=[12,11,13,5,6]
insertationSort(arr)
lst=[]
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i])
print(lst)