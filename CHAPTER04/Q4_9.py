def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 入力の個数を取得
N = int(input())

# 整数のリストを受け取る
numbers = []
for _ in range(N):
    d = int(input())
    numbers.append(d)

# マージソートを実行
sorted_numbers = merge_sort(numbers)

# 降順にソートされた整数をスペース区切りで出力
for num in sorted_numbers:
    print(num, end=" ")

