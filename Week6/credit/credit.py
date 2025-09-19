nums = input("Number: ")
if not nums.isdigit() or len(nums) < 13 or len(nums) > 16:
    print("INVALID")
    exit()
n = len(nums)
total = 0
N = nums[::-1]
for i, c in enumerate(N):
    C = int(c)
    if i % 2 == 1:
        C *= 2
        if C > 9:
            C = C // 10 + C % 10
    total += C
if total % 10 != 0:
    print("AINVALID")
    exit()
if nums[:2] in ['34', '37'] and len(nums) == 15:
    print("AMEX")
elif nums[:2] in ['51', '52', '53', '54', '55'] and len(nums) == 16:
    print("MASTERCARD")
elif nums[0] == '4' and (len(nums) == 13 or len(nums) == 16):
    print("VISA")
else:
    print('INVALID')
