class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right)//2
            print(f"mid: {mid}")
            if arr[mid] > arr[mid +1]:
                if arr[mid] > arr[mid -1]:
                    return mid
                right = mid -1
                print(f"right : {right}")
            else:
                left = mid +1
                print(f"left : {left}")

        return left
            