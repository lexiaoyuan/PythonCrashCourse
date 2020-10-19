# Python Crash course笔记

---

## 1. 基础知识

### 1.1 字符串（" "、' '）相关

1. 全部大写

```python
name.upper()
```

2. 全部小写

```pyhon
name.lower()
```

3. **每个单词**首字母大写

```bash
name.title()
```

4. 删除开头的空白

```python
name.lstrip()
```

5. 删除末尾的空白

```python
name.rstrip()
```

6. 删除两端的空白

```python
name.strip()
```

7. 非字符串转为字符串

```python
str(age)
```

8. 分隔字符串

```python
name.split() # split()以空格为分隔符将字符串拆分成多个部分，并将其存到一个列表中
```

### 1.2 列表（[ , ])相关

1. 访问列表元素

```python
names[0] # 第一个元素
names[-1] # 第二个元素
```

2. 在列表末尾添加元素

```python
names.append('aaa')
```

3. 在列表中插入元素

```python
names.insert(1, 'aaa')
```

4. 从列表中删除元素

```python
del names[1]
```

5. 弹出列表中的元素

```python
names.pop() # 弹出列表末尾的元素
names.pop(3) # 弹出列表第4个元素
```

6. 根据值删除列表中的元素

```python
names.remove('aaa') # 只删除第一个指定的值
```

7. 对列表进行永久性排序

```python
# names中所有指都是小写或都是大写
names.sort() # 按字母顺序排序
names.sort(reverse=True) # 按字母顺序逆序
```

8. 对列表进行临时排序

```python
sorted(names) # 不影响原始列表
```

9. 倒着打印列表

```python
names.reverse()
```

10. 确定列表的长度

```python
len(names)
```

11. 遍历整个列表

```python
for name in names:
    print(name)
```

12. 创建数字列表

```python
for value in range(1, 6): # 生成1,2,3,4,5
    print(value)
list(range(1, 6)) # [1, 2, 3, 4, 5]
list(range(1, 11, 2)) # 步长为2，[1, 3, 5, 7, 9, 11]
```

13. 对数字列表进行统计

```python
min(digits) # 找最小值
max(digits) # 找最大值
sum(digits) # 求和
```

14. 列表解析

```python
squares = [value**2 for value in range(1, 11)]
```

15. 对列表切片

```python
names[1:4] # names[1]、[2]、[3] 第2,3,4个元素
names[:4] # names[0]、[1]、[2]、[3] 从开头开始
names[2:] # names[2]、[3]、[4]、... 从第3个元素到结尾
names[-3:] # 最后3个元素
```

16. 复制列表

```python
names2 = names[:] #复制之后，两者是互不影响的
names2 = names # 两者指向同一个列表，一个变，都变
```

### 1.3 元祖（( , )）相关

1. 定义元祖

```python
names = ('le', 'xiaoyuan')
```

2. 访问元祖中的元素

```python
names[0]
```

3. 遍历元祖中的元素

```python
for name in names:
    print(name)
```

4. 修改元祖变量

```python
names = ('le', 'xiaoyuan', 'beta') # 只能重新定义整个元祖，修改元祖变量，不能修改元祖中的元素
```

### 1.4 if语句

1. 条件测试

```python
# 在比较运算符两边各添加一个空格是一个良好的编码习惯
== # 相等
!= # 不等
< # 小于
> # 大于
<= # 小于等于
>= # 大于等于
and # 都满足才为True
or # 都不满足才为False
in # 判断特定值是否已在列表中
not int # 判断特定值是否不在列表中
True # 真
False # 假
```

2. if语句

```python
if conditional:
    do something
```

3. if-else 语句

```python
if conditional:
    do something
else:
    do other something
```

4. if-elif-else语句

```python
if conditional:
    do something
elif conditional_2:
    do something
else:
    do something
```

### 1.5  字典（{ ' ': ' ',  ' ': 5}）相关

1. 定义字典

```python
names = {'first': 'le', 'last': 'xiaoyuan', 'age': 21,} # 最后一个后面也可以加上逗号
# 在空字典中添加键值对
names = {}
names['fisrt'] = 'le'
names['last'] = 'xiaoyuan'
names['age'] = 21
```

2. 访问字典中的值

```python
names['first']
```

3. 添加键值对

```python
names['like'] = 'coding' # Python不关心键值对的添加顺序
```

4. 修改字典中的值

```python
names['last'] = 'xiaoyuanbeta'
```

5. 删除键值对

```python
del names['last'] # 永远删除
```

6. 遍历字典

```python
for k,v in names.items(): # items()返回键值对列表

for k in names.keys(): # keys()返回所有键的列表
    
for v in names.values(): # values()返回所有值的列表
```

7. 按顺序遍历字典中所有键

```python
for k in sorted(names.keys()):
```

8. 提取字典中所有不重复的值

```python
for v in set(names.values()): # set()创建一个集合，但每个元素都不重复
```

### 1.6 用户输入相关

1. 获取用户输入

```python
message = input("Input ...") # 等待用户输入，回车继续运行
```

2. 获取数值输入

```python
age = input("Input ...")
age = int(age) # int()将数字的字符转换为数值
```

3. 求模运算符（%）

```python
4 % 3 # 将两数相除并返回余数
```

### 1.7 while循环

1. 使用while循环

```python
while conditions:
    # do something
```

2. 使用break退出循环

```python
while True:
    # do something
    break
```

3. 在循环中使用continue

```python
while conditions:
    # do something
    continue
```

4. 使用while来处理列表和字典

> 不应再for循环中修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。

```python
names = ['le', 'xiao', 'yuan']
while names:
    # do something

while name in names:
    # do something
```

### 1.8 函数相关

1. 定义函数

```python
def function():
    # do something
function() # 调用函数
```

2. 向函数传递信息

```python
def function(arguments): # arguments可以为任意值
    # do something
function('name')
```

3. 位置实参

```python
def function(arguments, other):
    # do something
function('name', 21) # 按顺序关联
```

4. 关键字实参

```python
def function(arguments, other):
    # do something
function(other=21, arguments='name') # 指定关联
```

5. 默认值

```python
def function(arguments, other=21): # 默认值应当放在最后
    # do something
function('name') # other不指定则为默认值
function('name', 30) # other指定了则为指定的值
```

6. 返回值

```python
def function(arguments, other):
    # do something
    return arguments.title() + ':' + int(other) # 可以返回任何类型的值，包括列表和字典等复杂的数据结构
function('name', 21)
```

7. 传递列表

```python
def function(names):
    for name in names:
        # do something
function(['le', 'xiao', 'yuan']) # 将列表传递给函数后，函数对列表所做的修改是永久性的
```

8. 禁止函数修改列表

```python
def function(names[:]): # 向列表传递列表的副本而不是原件
    # do something
names = ['le', 'xiao', 'yuan']
function(names[:]) 
```

9. 传递任意数量的实参

```python
def function(arguments, *other): # *other可以接受任意数量的形参，会创建一个空元组，将接收到的值都存到元组中。必须放在最后面
    for other in others:
    	# do something
function('name', 'le', 'xiaoyuan')    
```

10. 使用任意数量的关键字实参

```python
def function(arguments, **other): # **other可以接受任意数量的键值对，会创建一个空字典
    for k, v in other.items():
        # do something
function('le', first='xiao', last='yuan')
```

11. 导入整个模块

```python
import module_name # 可以在程序中使用模块中的所有函数
module_name.function_name()
```

12. 导入特定的函数

```python
from module_name import function_1, function_2
function_1() # 调用时不需要通过 . 号
function_2('lexiaoyuan')
```

13. 给函数指定别名

```python
from module_name import function_1 as f1 # 将函数function_1()重命名为f1()
f1() # 使用function_1()的地方都可省略为f1()
```

14. 给模块指定别名

```python
import numpy as np # 给模块指定简短的别名
np.dot() # 函数内的名称不变，只是模块名更简洁
```

### 1.9 类

1. 创建类

```python
class ClassName():
    def __init__(self, name, age): # 该方法会自动运行，且self是必须的，并位于其它参数前
        self.name = name
        self.age = age
    def function(self):
        # ...
```

2. 根据类创建实例

```python
dog = ClassName('willie', 6) # 创建实例时，不需要传递self参数

# 访问属性
dog.name

# 调用方法
dog.function()
```

3. 给属性指定默认值

```python
class ClassName():
    def __init__(self, name, age): # 该方法会自动运行，且self是必须的，并位于其它参数前
        self.name = name
        self.age = age
        self.like = 'sit' # 指定初始值
    def function(self):
        # ...
```

4. 修改属性的值

```python
# 直接修改属性的值
dog.like = 'roll over'

# 通过方法修改属性的值
class ClassName():
    --snip--
    def function(self, like):
        self.like = like
dog.function('roll over') # 只需要传递like参数
```

5. 继承

```python
class SmallDog(Dog): # 父类必须在当前文件中，且位于自雷前面
    def __init__(self, name, age):
        super().__init__(self, name, age) # super()函数将父类和子类联系起来
```

6. 重写父类的方法

```python
class SamllDog(Dog):
    --snip--
    def function(self): # 和父类方法同名
        # ...
```

7. 导入类

```python
from car import Car # 从car模块导入Car类
my_car = Car()
```

### 1.10 文件

1. 读取整个文件

```python
with open(filename) as file_object: # open()打开文件
    contents = file_object.read()  # read()读取整个文件
    print(contents)
```

2. 逐行读取

```python
with open(filename) as file_object:
    for line in file_object:
        print(line)
```

3. 逐行读取并存储在列表中

```python
with open(filename) as file_object:
    lines = file_object.readlines() # readlines()从文件中读取每一行，并将其存储在一个列表中
```

4. 写入文件

```python
with open(filename, 'w') as file_object: # 'w'表示写入模式（会覆盖原文件内容）
    file_object.write("something") # write()将字符串写入文件
```

5. 附加到文件

```python
with open(filename, 'a') as file_object:
    file_object.write("something") # write()将字符串附加到末尾
```

6. try-except处理异常

```python
try:
    # do something
except Error: # Error要替换成具体的异常
    # do something
```

7. else代码块

```python
try: # 尝试执行try中的代码，可能引发异常
    # do something
except Error:
    # do something
else: # try代码块执行成功时才需要执行的代码放在else代码块中
    # do something
```

8. pass语句

```python
try:
    # do something
except Error:
    pass # pass让Python什么都不做
```

9. json模块

```python
import json
with open(filename, 'w') as file_object:
    json.dump(data, file_object) # json.dump()将数据存储到文件file_object中

with open(filename) as file_object:
	json.load(file_object) # json.load()加载filename中的数据
```