n = int(input())
nums = list(map(int, input().split()))

def merge(arr, left, mid, right, comp):
    def compare(a, b):
        if comp:
            return a <= b
        else:
            return a > b

    result = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if compare(arr[i], arr[j]):
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1
    
    while i <= mid:
        result.append(arr[i])
        i += 1
    while j <= right:
        result.append(arr[j])
        j += 1
    
    for k in range(len(result)):
        arr[left + k] = result[k]


def merge_sort(nums, left, right, comp=True):
    if left < right:
        mid = (left + right) // 2
        merge_sort(nums, left, mid, comp)
        merge_sort(nums, mid + 1, right, comp)
        merge(nums, left, mid, right, comp)

merge_sort(nums, 0, n - 1)
print(*nums)
merge_sort(nums, 0, n - 1, False)
print(*nums)
