#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/7 0007 下午 3:32
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: 2-1.py

#@Software: PyCharm

class People:
    """People类，属性有：姓名、性别、年龄"""

    def __init__(self, name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def display(self):
        print(self.name,self.sex , self.age)

class Student(People):
    """基于People实现学生类Student，添加属性：学号、入学时间和入学成绩；"""

    def __init__(self, name, sex, age,id,time,score):
        super().__init__(name, sex, age)
        self.id=id
        self.time = time
        self.score = score

    def display(self):
        print(self.name,self.sex , self.age,self.id,self.time,self.score)

class Teacher(People):
    """基于People实现教师类Teacher，添加属性：职务、部门、工作时间；"""

    def __init__(self, name, sex, age,job,clazz,work_time):
        super().__init__(name, sex, age)
        self.clazz=clazz
        self.job = job
        self.work_time = work_time

    def display(self):
        print(self.name, self.sex, self.age, self.job, self.clazz, self.work_time)

class Graduate(Student):
    """基于Student实现究生类Graduate，添加属性：研究方向和导师"""

    def __init__(self, name, sex, age, id, time, score,dic,teacher):
        super().__init__(name, sex, age, id, time, score)
        self.dic = dic
        self.teacher = teacher

    def display(self):
        print(self.name, self.sex, self.age, self.id, self.time, self.score,self.dic,self.teacher)
def test():
    student = Student("高得健","男","20","20163437","2016","100")
    student.display()
    teacher = Teacher("老师","男","30","教授","信息科学与技术学院","10")
    teacher.display()
    graduate = Graduate("高得健","男","20","20163437","2016","100","人工智能","TeacherLi")
    graduate.display()
test()