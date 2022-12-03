# 文件拷贝2

## 【问题描述】

写一程序将一个文件fcopy.in拷贝至另一个文件fcopy.out, 其中在所拷贝的文件中, 多个连续空白符（包括空格符、制表符）只拷贝一个空格符， 其它字符不变。

## 【输入形式】

源文件名和目标文件名分别为fcopy.in和fcopy.out，程序将从当前目录下读取fcopy.in文件。

## 【输出形式】

将fcopy.in文件内容拷贝至当前目录下的fcopy.out文件中。在所拷贝的文件中, 多个连续空白符（包括空格符、制表符）只拷贝一个空格符，若非空白符之间有一个制表符，则该制表符也要替换为空格符，其它字符不变。

## 【输入样例】

假如文件fcopy.in中内容如下：

```
Alcatel        provides end-to-end solutions.
```

## 【输出样例】

输出文件fcopy.out中内容为：

```
Alcatel provides end-to-end solutions.
```

## 【样例说明】

将文件fcopy.in拷贝到fcopy.out，同时做适当的转换。