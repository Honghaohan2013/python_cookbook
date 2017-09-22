#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
python对象成员变量的命名规则:
    找到一个写的比较好的BLOG：http://blog.sina.com.cn/s/blog_62f28d560100xpva.html
1、公有成员：self.public_member，子类可以访问父类的成员
2、保护成员：self._protected_member，只有在本类或子类中才能访问
    而对于一个包来说，单下划线开头的成员为包内独有，虽然外部仍然可以调用，但是会有风险，同时运行类似from A import * 这样的命令不会导入单下划线开头的成员
3、私有成员：self.__private_member，只有在本类中才能访问，子类也不能访问，在包里的双下划线开头的变量，外部导入特性同上

而如果想用python中的保留字，如lambda来作为变量时，为了保证保留字的正常工作，可以将变量名后面加一个_，如：lambda_
"""

