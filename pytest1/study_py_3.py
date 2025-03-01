# 3列表简介
# 3.1列表是什么
bicycles = ['anno','shwo','biya','bwm']
print(bicycles[0].title())    # 索引从0开始,而不是1   .title()方法是首字母大写
print(bicycles[-1])           # -1直接访问最后一个元素
messaage = "My bicycle is "+bicycles[0]+"."
print(messaage)
# 动手试一试
# 请尝试编写一些简短的程序来完成下面的练习，以获得一些使用Python列表的第一手经验。你可能需要为每章的练习创建一个文件夹，以整洁有序的方式存储为完成各章的练习而编写的程序。
# 3-1 姓名：姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
# 3-2 问候语：问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
# 3-3 自己的列表：自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”

# 3-1
names = ['yj','tj','ly','zw','fzl']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3-2
say = "hi,good moring "
print(say+names[0])
print(say+names[1])
print(say+names[2])
print(say+names[3])
print(say+names[4])

# 3.2修改,添加和删除元素
motorcycles = ['honos','biy','swws']
print(motorcycles)
motorcycles[0] = 'dada'     # 修改列表元素的值
print(motorcycles)
motorcycles.append('newend')    # 用.append()方法在列表的末尾添加新元素
print(motorcycles)
motorcycles.insert(1,'charu')   # .insert()插入新元素,
print(motorcycles)
# 删
del motorcycles[1]              # del 删除元素的值(输入元素位置)
print(motorcycles)
new_motorcycles = motorcycles.pop()     # 使用pop()方法删除列表元素的末尾值,并放到列表外,删除的元素用new_motorcycles接住然后输出
print(motorcycles)
print(new_motorcycles)
motorcycles.pop()
print(motorcycles)
two = motorcycles.pop(1)            # 除了del可以删除任意位置的元素外,pop()方法也可以,但要在括号内填写索引
print(motorcycles)
print(two)

cars = ['a','b','c','d']
cars.remove('b')        # 在不知道列表元素索引但知道名字时可以用remove()方法
print(cars)

# 3-4 嘉宾名单嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用
# 这个列表打印消息，邀请这些人来与你共进晚餐。
# 3-5 修改嘉宾名单修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
# 3-6 添加嘉宾添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
# 使用insert() 将一位新嘉宾添加到名单开头。
# 使用insert() 将另一位新嘉宾添加到名单中间。
# 使用append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
# 3-7 缩减名单缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
# 晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。

# 3-4
laddytion = ['anna','jack','ben']
print("\nWelcome! "+laddytion[0])
print("Welcome! "+laddytion[1])
print("Welcome! "+laddytion[2])
# 3-5
busy = laddytion.pop(1)
laddytion.insert(1,'bland')
print("Welcome! "+laddytion[0])
print("Welcome! "+laddytion[1])
print("Welcome! "+laddytion[2])
print(busy)
# 3-6
laddytion.insert(0,'rina')
laddytion.insert(2,'ling')
laddytion.append('jett')
print("I find bigger table,Welcome! "+laddytion[0])
print("I find bigger table,Welcome! "+laddytion[1])
print("I find bigger table,Welcome! "+laddytion[2])
print("I find bigger table,Welcome! "+laddytion[3])
print("I find bigger table,Welcome! "+laddytion[4])
print("I find bigger table,Welcome! "+laddytion[5])
# 3-7
name1 = laddytion.pop()
name2 = laddytion.pop()
name3 = laddytion.pop()
name4 = laddytion.pop()
print("I'm sorry "+name1)
print("I'm sorry "+name2)
print("I'm sorry "+name3)
print("I'm sorry "+name4)
print("Welcome again "+laddytion[0])
print("Welcome again "+laddytion[1])
del laddytion[1]
del laddytion[0]
print(laddytion)

# 3.3组织列表
car = ['bwn','dasd','xiaomi','byddd']
car.sort()      # sort（）方法的排列顺序是永久性的
print(car)
print(sorted(car))      # 而sorted（）函数的排列顺序是临时的
car.reverse()
print(car)      # reverse()方法是把列表的顺序倒过来 这也是永久性的，但再次调用该方法就可恢复原来的顺序
print(len(car))       # len()函数是获取列表的长度

# 3-8 放眼世界
# 放眼世界 ：想出至少5个你渴望去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
# 使用sorted() 按字母顺序打印这个列表，同时不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
# 3-9 晚餐嘉宾
# 晚餐嘉宾 ：在完成练习3-4~练习3-7时编写的程序之一中，使用len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
# 3-10 尝试使用各个函数
# 尝试使用各个函数 ：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列
# 表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。

# 3-8
country = ['Sweden','Chinese','Janpa','England','American']
print(country)
print(sorted(country))
print(country)
print(sorted(country,reverse=True))     # 这个好难！上网搜的
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
print('------------------------------------')    # 分割线，要不然看着眼睛要花了
country.sort()
print(country)
country.sort(reverse=True)
print(country)

# 3-9
print(len(country))

# 3-10
favourite = ['orange','banana','apple','andriod','pet']
del favourite[3]
print(favourite)
print(len(favourite))
print(sorted(favourite))

# 3.4使用列表时避免索引错误
# 3-11 有意引发错误
# 有意引发错误 ：如果你还没有在程序中遇到过索引错误，就尝试引发一个这种错误。在你的一个程序中，修改其中的索引，以引发索引错误。关闭程序前，务
# 必消除这个错误

# gfg = []
# print(gfg[-1])        # 索引错误

