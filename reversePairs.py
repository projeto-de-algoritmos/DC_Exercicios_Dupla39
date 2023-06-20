
# Reverse Pairs
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort_and_count(nums, start, end):
            if start >= end:
                return 0

            mid = (start + end) // 2
            count = sort_and_count(nums, start, mid) + sort_and_count(nums, mid + 1, end)

            i, j = start, mid + 1
            merged = []
            while i <= mid and j <= end:
                if nums[i] > 2 * nums[j]:
                    count += mid - i + 1
                    j += 1
                else:
                    i += 1

            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    merged.append(nums[i])
                    i += 1
                else:
                    merged.append(nums[j])
                    j += 1

            merged.extend(nums[i:mid + 1])
            merged.extend(nums[j:end + 1])
            nums[start:end + 1] = merged

            return count

        return sort_and_count(nums, 0, len(nums) - 1)
