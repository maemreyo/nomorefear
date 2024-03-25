def binary_search(arr, target):
    """Tìm kiếm nhị phân
    General:
    - Thuật toán tím kiềm được sử dụng trong sorted 1__array.

    Quick explanation:
    - Chia không gian tìm kiếm thành 2 nửa bằng cách tìm chỉ số ở giữa "mid"
    - So sánh phần tử ở giữa của không gian tìm kiếm với target
    - Nếu target === mid thì return
    - Nếu chưa tìm thấy target !== mid thì sang bước tìm không gian tìm kiếm tiếp theo:
        => Nếu target < mid => nửa bên trái sẽ được sử dụng cho lần tìm kiếm tiếp theo
        => Nếu target > mid => nửa bên phải sẽ được sử dụng cho lần tìm kiếm tiếp theo
    - Quá trình lặp đi lặp lại cho tới khi thấy target hoặc khi hết không gian tìm kiếm

    Pseudocode:
    ```
        BinarySearch(arr, target):
            left = 0
            right = length(arr) - 1

            while left <= right:
                mid = (left + right) / 2

                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1
    ```
    Notes:
    - Cấu trúc dữ liệu của mảng đầu vào phải được sắp xếp
    - Việc truy cập vào bất ký phần tử nào của cấu trúc dữ liệu đều mất thời gian không đổi

    Complexities:
    - Time complexity: O(log(n)) => mỗi lần lặp, không gian tìm kiếm bị chia đôi, loại bỏ 1 nửa phần tử
    - Space complexity: O(1) => không có sự gia tăng thêm về không gian khi input arr tăng lên
    Args:
        arr (list): Mảng đầu vào
        target (int): Phần tử cần tìm
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Nếu tìm thấy target
        if target == arr[mid]:
            return mid

        # Nếu target < mid => nửa bên trái sẽ được sử dụng cho lần tìm kiếm tiếp theo
        elif target < arr[mid]:
            right = mid - 1

        # Nếu target > mid => nửa bên phải sẽ được sử dụng cho lần tìm kiếm tiếp theo
        else:
            left = mid + 1

    # Trả về -1 nếu không tìm thấy target trong mảng
    return -1


# Ví dụ về cách sử dụng:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"{target} được tìm thấy tại vị trí {result}")
else:
    print(f"{target} không tồn tại trong mảng")
