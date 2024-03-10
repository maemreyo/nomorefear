def linear_search(arr, target):
    """
    Tìm kiếm tuần tự trong một mảng
    
    Complexities:
    - Time complexity:
        => Worst case: O(n)
        => Best case: O(1)
        => Average case: O(n)
    - Space complexity: O(1) => không có sự tăng thêm về không gian khi kích thước input arr tăng lên
    
    Parameters:
        arr (list): Input array
        target: Phần tử cần tìm kiếm
    
    Returns:
        int: Chỉ số của phần tử nếu được tìm thấy, -1 nếu không tìm thấy
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [4, 2, 7, 1, 9, 5]
target = 7
result = linear_search(arr, target)
if result != -1:
    print(f"Phần tử {target} được tìm thấy tại chỉ số {result}.")
else:
    print(f"Phần tử {target} không được tìm thấy trong mảng.")