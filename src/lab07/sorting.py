def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
 
    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums=list(nums)
    n=len(nums)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped=True
        if not swapped:
            break
    return nums

def insertion_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    nums=list(nums)
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums



def selection_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    nums=list(nums)
    for i in range(len(nums)-1):
        mn=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[mn]:
                mn=j
        nums[i],nums[mn]=nums[mn],nums[i]
    return nums













