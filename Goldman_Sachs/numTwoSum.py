def num_Two_Sum(a, k):
    count = 0
    for i in a:
        if k - i in a:
            count += 1
    return (int(count/2))


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(num_Two_Sum(a, 16))
temp = [3,1,3,4,3]
print(temp.index(3))


# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in nums:
#         print(i)
#         temp = nums
#         temp.remove(i)
#         print("remove",i,"is",temp,"nums",nums)
#         # if target - i in temp:
#         #     print("lalala")
#         #     return ([nums.index(i), temp.index(target - i)+1])
#
# print(twoSum([3,2,4], 6))