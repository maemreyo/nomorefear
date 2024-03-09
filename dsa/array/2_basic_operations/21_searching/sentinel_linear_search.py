def sentinel_linear_search(arr, target):
    """Tìm kiếm tuần tự với biến bảo vệ (sentinel)
    General:
    - Biến thể của Linear Search khi ta thêm biến bảo vệ (= target) vào cuối mảng => không cần phải kiểm tra điều kiện dừng (i < len(arr)) => giảm số lần so sánh trong vòng lặp

    Quick explanation:
    - Thêm phần tử target vào cuối mảng
    - Chạy vòng lặp
    - Khi tìm thấy, ta so sánh index của nó để xem `i < len(arr) - 1` hay không
        => Nếu true => trả về i
        => Nếu false => -1

    Notes:
    - Mặc dù trong worst case, độ phức tạp về thời gian của Linear Search và Sentinel Linear Search đều là O(n), nhưng SLS vẫn có ít số phép so sánh hơn.
    
    Args:
        arr (list): mảng đầu vào
        target: phần tử cần tìm kiếm

    Returns:
        int: chỉ số của phần tử nếu được tìm thấy, -1 nếu không tìm thấy phần tử cần tìm
    """
    # Thêm phần tử cần tìm vào cuối mảng
    arr.append(target)
    i = 0

    # Tìm kiếm phần tử cần tìm
    while arr[i] != target:
        i += 1

    # Nếu thấy thì xóa phần tử sentinel
    arr.pop()
    # Validate phần tử tìm thấy
    if i < len(arr) - 1 or arr[-1] == target:
        return i
    else:
        return -1

# Sử dụng ví dụ:
arr = [4, 2, 7, 1, 9, 5]
target = 7
result = sentinel_linear_search(arr, target)
if result != -1:
    print(f"Phần tử {target} được tìm thấy tại chỉ số {result}.")
else:
    print(f"Phần tử {target} không được tìm thấy trong mảng.")