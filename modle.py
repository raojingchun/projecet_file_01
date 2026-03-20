# -*- coding: utf-8 -*-
# # 获取当前的文件的路径
# import copy
# import os
#
# # print(os.listdir())
# print(os.getcwd())
#
# # 原生字符和转义字符对比
# raw_str = r'C:\Users\Administrator\PycharmProjects\pythonProject\day01\扩展知识'
# return_str = 'C:\\Users\\Administrator\\PycharmProjects\\pythonProject\\day01\\扩展知识'
# print(raw_str)
# print(return_str)
#
# # unicode编码
# letter = '@'
# unic = ord(letter)
# print(unic)
# # \u102
#
# # 将名字变成unicode编码
# # unicode = r'\u' + hex(ord('孔'))[2:]  # \u5b54\u2e42\u34b
# # name_str = input(f'请输入一个名字：')
# # 方法一
# # name_ = ''
# # for name in name_str:
# #     name_ += r'\u'+hex(ord(name))[2:]
# # print(name_)
#
# # 方法2
# # name_list = []
# # for name in name_str:
# #     s = r'\u'+hex(ord(name))[2:]
# #     name_list.append(s)
# # print(''.join(name_list))
#
# # end_name = "".join([r'\u' + hex(ord(name))[2:] for name in name_str])
# # print(end_name)
#
# # print(unicode)
# # # print(int(hex(ord('孔'))[2:], 16)) # 0x234b
# #
# # print(ord('孔'))
# #
# #
# # # 字节编码介绍
# # s = '张三'
# # print(s.encode('utf8')) # 字节3个字节
# # print(s.encode('gbk')) # 2个字节
#
# # 字典介绍
# seq = [('苹果', 'apple'), ('香蕉', 'banana')]
# print(dict(seq))
# seq2 = [['苹果', 'apple1'], ['香蕉', 'banana1']]
# print(dict(seq2))
#
# dao = {'a': 1, 'b': 2, 'c': 5}
# # 在字典中新增一个元素
# s = {'d': 2}
# dao.update(s)
# print(dao)
#
# dao['e'] = 1
# print(dao)
#
# print(dao.fromkeys('a', 2))
# # 随机删除元素
# dao.popitem()
# print(dao)
# # 删除指定元素
# dao.pop('a')
# print(dao)
# # 删除指定元素
# del dao['b']
# print(dao)
#
# # 获取字典的键
# set = dict(seq)
# print(list(set.keys()))
# # 获取字典的值
# print(list(set.values()))
# # 获取字典的值和值
# print(list(set.items()))
#
# # 遍历访问字典的键值对
# for k in set.keys():
#     print(k, set[k])
#
# for k, v in set.items():
#     print(k, v)
#
# print(set)
# # set.clear()
# print(set)
#
# # 字典中的浅复制和深复制
# a = {'a': 2, 'b': 3, "c": 5}
# b = a.copy()
# b['e'] = 8
# print(a, b)
# print(id(a), id(b))  # 存储的位置不一样
#
# # a == b ?
# print(a == b)
#
# c = {"a": [1, 2, 3], 'b': [4, 5, 6]}
# e = copy.deepcopy(c)
# print(id(c), id(e))
# new = e['a'].append(4)
# print(e)
# print(c, e)
#
# # 字典按照值进行排序
# s1 = {'a': 2, 'f': 4, 'd': 8, 'e': 3}
# # 方法1
# s = sorted(s1.items(), key=lambda i: i[1], reverse=True)
# print(dict(s))


# d = {'a': 2, 'b': 4, 'c': 6}
#
# # 先把值排好：[2,4,6]
# vs = sorted(d.values())
#
# new_d = {}
# for v in vs:
#     for k in d:
#         if d[k] == v:
#             new_d[k] = v
#         else:
#             break
# print(new_d)

# def run(i):
#     s = []
#     for n in range(i):
#         n += 1
#         s.append(n)
#     print(s)
#     return ([3,4])
#
# b = run(2)


# print(b)
# print(type(b))
#
# b = [(2,3)]
# print(b)
# print(type(b))
import time

a = 1


def run():
    time.sleep(5)
    global a
    a = 2
    print(a)


def run1():
    print(a)


print(run())
run1()
print(a)
