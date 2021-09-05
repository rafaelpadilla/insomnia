def findMedianSortedArrays2(nums1, nums2):
    nums = sorted(nums1 + nums2)
    if len(nums) % 2 == 1:
        return nums[int(len(nums) / 2)]
    else:
        return (nums[int(len(nums) / 2) - 1] + nums[int(len(nums) / 2)]) / 2


def findMedianSortedArrays2(nums1, nums2):
    i, j = 0, 0
    new_array = []
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    total_len = len_nums1 + len_nums2
    median_index, last_digit_1, last_digit_2 = None, None, None

    if total_len % 2 == 1:
        median_index = int(total_len / 2)
    count_items = 0
    while True:
        if i < len_nums1 and j < len_nums2:
            if nums1[i] < nums2[j]:
                new_array.append(nums1[i])
                last_digit_1 = nums1[i]
                i += 1
            else:
                new_array.append(nums2[j])
                last_digit_1 = nums2[j]
                j += 1
        elif i < len_nums1:
            if median_index is None:
                return (last_digit_1 + nums2[0]) / 2
            for el in nums1[i:]:
                new_array.append(el)
            break
        else:
            if median_index is None:
                return (last_digit_1 + nums2[0]) / 2
            for el in nums2[j:]:
                new_array.append(el)
            break
    if median_index is not None:
        return new_array[median_index]


nums1 = [1, 3]
nums2 = [2]
# print(findMedianSortedArrays(nums1,nums2))

nums1 = [1, 2]
nums2 = [3, 4]
# print(findMedianSortedArrays(nums1,nums2))

nums1 = [0, 0]
nums2 = [0, 0]
# print(findMedianSortedArrays(nums1,nums2))

nums1 = []
nums2 = [2, 3]
print(findMedianSortedArrays(nums1, nums2))
