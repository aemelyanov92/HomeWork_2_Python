import random
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_nums = []
while nums:
    new_nums.append(nums.pop(random.randint(0, len(nums) - 1)))
    print(new_nums)


# Подскажите, пожалуйста другое, оптимальное решение, я не сообразил, как лучше