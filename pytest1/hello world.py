# # age = 123
# # print('%06d'% age)
# float = 3.1415926
# print('%.1f'%float)
# name = 'gfg'
# age = 11
# print(f'我的名字是{name}，我的年纪是{age}')

# a = 5
# b = 2
# print(a / b)
# print('a / b')
# print(a // b)
# print('a // b')
# print(a % b)
# print(a ** b)
# print(8 // 2)
# print(8.0 // 2)
# print(2+5-1/2**2)

# name = input('请输入姓名：')
# print(name)

# print('xixi\thaha')
# print('xixi\nhaha')
# print('abc\rde')
# print('abc\\defg')
# print(r'abcd\\da\tda\rsd\nsa')

# grade = input('请输入成绩：')
# print(grade)
# if grade >99:
#     print('你真棒')
# if grade <61:
#     print('还要继续加油')
# if   61 < grade < 99:
#     print('继续保持')
# 以上是自己的想法，有错误(缺少单引号)

# grade = input('请输入成绩：')
# if grade == '100':
#     print('你真棒！')
# if grade == '60':
#     print('还要继续加油啊！')
# 以上是正确代码

# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
# print(s)
# 经典的从1加到100的总和计算f

# for i in range(1,6):
#     print(i)
# 包前不包后

# 运用for循环去计算1到100的总和
# s = 0
# for i in range(1,101):
#     s += i
# print(s)

# i = 1
# while i <= 5:
#     print(f'小红吃第{i}个苹果')
#     if i == 3:
#         print('小红吃饱了')
#         break
#     i += 1

# 零基础python的100道题目：第一题：编写一个程序，找到2000年至3200年(包括在内)中所有可被7整除但不能被5整除的所有数字，得到的数字按逗号分隔，打印在一行上
# l=[]
# for i in range(2000,3201):
#     if(i%7 == 0)and(i%5 != 0):
#         l.append(str(i))
# print(','.join(l))

# a = 'hello'
# print(a,type(a))
# a1 = a.encode('UTF-8')
# print(a1,type(a1))
