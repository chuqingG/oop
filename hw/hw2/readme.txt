实验要求：
作业题：
1. 编写一个函数， sum_of_all，至少接收两个位置参数，也可以采用以下形式调用
sum_of_all(1, 2, 3, 4, 5)  三个以上位置参数，返回所有数的数学和(15 = 1+2+3+4+5)
sum_of_all(1, 2, 3, 4, 5, block = 2)  三个以上位置参数，返回每组数的积的和，(19 = 1*2 + 3*4 + 5)，组的大小block默认为1，范围为{1,2}
sum_of_all(1, 2, 3, 4,  inverse = True) 三个以上位置参数，返回所有数的倒数的和，25/12(=1/1+1/2+1/3+1/4)，inverse默认为False
sum_of_all(1, 2, 3, 4,  block = 2, inverse = True) 先求每组数的积，再求每组结果的倒数和。7/12 (=1/2+1/12)

2. 编写一个基类Shape，和从Shape派生的类Circle和Square。Shape类拥有属性area和name，以及方法get_area()。Circle类代表圆形，拥有属性diameter, Square代表正方形，拥有属性side。Circle的构造函数形式为Circle( d = 2)，默认为单位圆, Square的构造函数为Square( s = 1)，默认为单位正方形。当建立一个Circle或者Square的实例p后，可以用p.get_area()来得到面积。在Circle和Square类中均不重新定义get_area方法。

提示：作业题2可以通过如下方式实现：基类定义area属性，初始化时赋初值0，派生类初始化的时候修改area属性，根据不同情形得出area值

作业要求：
以.zip文件格式提交，压缩包内含main.py(本次实验代码)及test.py(助教提供的测试代码)，下周(11.6)上课前提交到助教的qq邮箱:975215046。邮件主题请注明姓名+学号+作业2。

实验步骤：
1. 完成main.py
2. 在命令行中输入python test.py. 如果结果为

.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK

说明代码正确，否则请修改出错位置。
3. 将结果打包发送至助教邮箱，压缩包内需同时包含main.py和test.py。
