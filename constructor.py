# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:29:03 2020

@author: Preksha Sharma
"""

class Student:
    def _init_(self):
        print("Non parameterized constructor")
    def show(self,name):
        print("Hello",name)
student=Student()
student.show("jasper")