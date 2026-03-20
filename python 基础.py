# 如何获取当前文件的目录
import os
import re

dice = os.getcwd()
print(dice)
# C:\Users\Administrator\PycharmProjects\pythonProject\day01\python 01基础
# 将以上目录导入demo1文件中
path = dice + '\\python 01基础'  # \转义字符
print(path)
file = open('demo1.txt', 'w', encoding='utf-8')
file.write(path)
file.close()

print("\"\"\"\"")
a = "12345dgsudfguwefgwe"
print(re.findall(r'[a-z]{2,3}', a)[0])
b = "1hdeg284384634wwe15240182330efedrffag"
# 从b中获取正真的电话号码
pattern = r'1[0-9]{10}'  # ^匹配字符串的开头，$匹配字符串的结尾，.匹配任意一个字符
print(re.findall(pattern, b)[0])
print(re.findall('wwe(.*?)ef', b)[0])
# （）相当于捕获组
print(re.search("wwe(?P<number>.*?)ef", b)[1])
print(re.search("wwe(?P<number>.*?)ef", b).group('number'))

a = '1323\nfrr\terft\ndheugfuefgeuf'
print('1323\nfrr\terft\ndheugfuefgeuf')
print(repr('1323\nfrr\terft\ndheugfuefgeuf'))
print(eval(repr(a)) == a)

import binascii
a = 'abcdefa123344454'
print(binascii.a2b_hex(a))


