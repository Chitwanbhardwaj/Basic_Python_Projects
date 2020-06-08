def Binary_search(list,key):
    start = 0
    end = len(list)

    while start < end: 
        mid = (start + end)//2
        if list[mid] > key:
            end = mid
        elif list[mid] < key:
            start = mid+1
        else:
            return mid
    return -1

list = input("Enter the sorted list of numbers:- ") 
list = list.split()
list = [int(x) for x in list]
key = int(input("Enter the number you want to search for :- "))

index = Binary_search(list,key)
if index < 0:
    print("{} was not found".format(key))
else:
    print("{} was found at index {}".format(key, index))
