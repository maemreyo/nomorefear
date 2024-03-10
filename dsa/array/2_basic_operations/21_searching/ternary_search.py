def ternary_search(arr: list, target):
    """Ternary search function
    General:
    - Tìm kiếm bậc ba là thuật toán chia để trị được sử dụng để tìm vị trí của một giá trị cụ thể trong một mảng nhất định
    - Chia mảng thành 3 phần và thực hiện đệ quy thao tác tìm kiếm trên phần thích hợp cho đến khi tìm thấy phần tử cần tìm
    - Mảng ban đầu phải được sắp xếp

    Quick Explanation:
    1. Khởi tạo
    - Bắt đầu khởi tạo với SORTED ARRAY
    - Đặt 2 pointers left và right, ban đầu trỏ đến phần tử đầu tiên và cuối cùng của mảng

    2. Chia mảng
    - Tính 2 điểm mid1 và mid2, chia không gian tìm kiếm thành 3 phần
        ==> [left, mid1], [mid1, mid2], [mid2, right]

    3. So sánh
    - Nếu target == mid1 or target == mid2, search successful => return mid1 or mid2
    - Nếu target < mid1 ===> right = mid1 - 1
    - Nếu target > mid2 ===> left = mid2 + 1
    - Nếu mid1 < target < mid2 ===> left = mid1 + 1 and right = mid2 - 1

    4. Lặp lại hoặc return
    - Lặp lại quá trình trên với không gian tìm kiếm đã giảm
    - Trả về index nếu thấy target hoặc -1 nếu không tìm thấy

    Pseudocode:
    ```
        sorted_array = [...]
        left = 0
        right = length(arr) - 1


        while left <= right:
            mid1 = left + (right - left) / 3
            mid2 = right - (right - left) / 3

            if target == mid1:
                return mid1
            elif target == mid2:
                return mid2

            if target < mid1:
                right = mid1 - 1
            elif target > mid2:
                left = mid2 + 1

            else:
                left = mid1 + 1
                right = mid2 - 1

        return -1
    ```
    Notes:

    Complexities:
    - Time complexity
        ===> Worst case: O(log3(n))
        ===> Best case: Θ(1)
        ===> Average case: Ω(1)
    - Space complexity: O(1) => không có sự gia tăng thêm về không gian khi input arr tăng lên
    
    Args:
        arr (list): mảng đầu vào
        target: phần tử cần tìm

    Returns:
        ==> -1 nếu không tìm thấy target
        ==> index (!= -1) nếu tìm thấy target
    """
    # * Khởi tạo 2 pointers trỏ tới đầu và cuối của mảng
    left = 0
    right = len(arr) - 1

    while left <= right:
        # * Tính toán 2 điểm mid để chia mảng thành 3 phần
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # * Nếu tìm thấy target tại mid1 or mid2 thì return
        if target == arr[mid1]:
            return mid1
        elif target == arr[mid2]:
            return mid2

        # * So sánh để giới hạn không gian tìm kiếm
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1

        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

# Ví dụ
arr = [1, 3, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17]
target = 15

index = ternary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")