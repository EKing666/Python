# 2-3 个性化消息： 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。
# 2-4 调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
# 2-5 名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
#  2-6 名言名言2:重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
# 2-7 剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来

# 2-3
name1 = 'anna'
print('Hello Eric,would you like to learn some Python today?')

# 2-4
name2 = 'frAnk'
print(name2.lower())
print(name2.upper())
print(name2.title())

# 2-5
print('napoleon said:"The real talent is resolute aspirations."')

# 2-6
famous_person = 'napoleon'
message = 'said:"The real talent is resolute aspirations."'
print((famous_person)+" "+(message))

# 2-7
name3 = '\tda\tshuai\tbi\njiu\tshi\two\t'
name3 = name3.lstrip()   # 剔除了开头的空白
name3 = name3.rstrip()   # 剔除了末尾的空白
name3 = name3.strip()    # 剔除了两边的空白
print(name3)

