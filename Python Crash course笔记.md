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

### 1.3 元祖( , )相关

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



