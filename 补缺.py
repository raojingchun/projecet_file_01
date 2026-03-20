# 3.查找字符串中相同字符的最后一个
# 正常查找e,会找到第一个
a = "abcdefer"
ret = a.find("e")
print(ret)
# 查最后一个e
a = "abcdefer"
s = a[::-1]
print(s)
ret = s.find("e")
print(ret)
