#!/usr/bin/env python                                                                                                                                                                                                                  
# -*- coding:utf-8 -*-

"""
允许给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证
"""

class Person(object):
    def __init__(self, first_name):
        self.first_name = first_name    ## first_name.setter()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value, str):
            raise TypeError('Expect a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class PersonWithNoDecorator(object):
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)
