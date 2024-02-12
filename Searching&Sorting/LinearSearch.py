# def search(arr, x):
 
#     for i in range(len(arr)):
 
#         if arr[i] == x:
#             return i
 
#     return -1

# arr= [10, 20, 80, 30, 60, 50,  110, 100, 130, 170]
# x = 110

# ans=search(arr,x)

# print(f"Element is present at index {ans}")

def search(arr, curr_index, key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)