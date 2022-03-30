from typing import List

nums = [1, 3, -1, -3, 5, 9, 3, 6, -3, 9, -9, 9, -5, 7, -5, 3, 2]
k = 4


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:

    z = 0
    sum_max = 0

    while z <= len(nums) - k:
        try:
            t=z
            sum_temp = 0
            while t < z+k:
                sum_temp += nums[t]
                t += 1
            if sum_temp > sum_max:
                sum_max = sum_temp
            z += 1
        except IndexError:
            break

    return sum_max


print(find_maximal_subarray_sum(nums, k))
