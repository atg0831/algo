N = int(input())
search_list = list(map(int, input().split()))
M= int(input())
key_list = list(map(int, input().split()))

search_list.sort()

def binary_search(key):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        if search_list[mid] == key:
            print(1)
            return
        
        elif search_list[mid] < key:
            start = mid + 1
        
        else:
            end = mid - 1
    
    print(0)

for key in key_list:
    binary_search(key)
