# 2、打印出100以内的斐波那契数列，使用2种方法实现
# 方法1
count = 100
nums = [1, 1]

for i in range(1, count):
    lastVal = nums[i - 1]
    curVal = lastVal + nums[i]
    if curVal >= 100:
        break
    nums.append(curVal)

print('100以内的斐波那契额数列：', nums)

# 方法2
nums = [1, 1]
lastVal1 = nums[0]
lastVal2 = nums[1]
while True:
    curVal = lastVal1 + lastVal2
    # print('lastVal1=', lastVal1, ' lastVal2=', lastVal2, 'curval', curVal)
    if curVal >= 100:
        break
    nums.append(curVal)
    lastVal2 = lastVal1
    lastVal1 = curVal
    # print('交换lastVal1=', lastVal1, ' lastVal2=', lastVal2, 'curval', curVal)
print('100以内的斐波那契额数列：', nums)

# 3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random

activateCode = set()
while True:
    code = random.randrange(10000, 10000000)
    activateCode.add(code)
    if len(activateCode) >= 200:
        break
print('激活码个数', len(activateCode), '激活码：', activateCode)
