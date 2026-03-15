nums = [4, 1, 3, 9, 2]

def ascending_order(nums):

    for number in range(len(nums)):
        for count in range(number + 1, len(nums)):
            if nums[number] > nums[count]:
                nums[number], nums[count] = nums[count], nums[number]
    return ascending_order


ascending_order(nums)
print(nums)


