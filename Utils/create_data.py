# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 15:34
# @Author  : DannyDong
# @File    : create_data.py
# @describe: 生成数据

import random


# 生成学员姓名
def cr_student_name():
    last = random.randint(99, 1000)
    name = "UAT学员{}".format(last)
    return name


# 生成员工姓名
def cr_staff_name():
    last = random.randint(99, 1000)
    name = "UAT员工{}".format(last)
    return name


# 生成年龄
def cr_age():
    age = random.randint(1, 100)
    return age


# 生成课时数量
def cr_course_num():
    age = random.randint(10, 100)
    return age


# 生成电话号码
def cr_phone():
    last = random.randint(999999999, 10000000000)
    phone = "9{}".format(last)
    return phone


# 生成课程名称
def cr_course():
    last = random.randint(99, 1000)
    name = "UAT课程{}".format(last)
    return name


# 生成班级名称
def cr_class():
    last = random.randint(99, 1000)
    name = "UAT班级{}".format(last)
    return name


if __name__ == '__main__':
    print(cr_student_name())
    print(cr_staff_name())
    print(cr_course())
    print(cr_class())
    print(cr_phone())
    print(cr_age())
    print(cr_course_num())
