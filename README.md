# 杨辉三角生成器

这是一个用Python编写的杨辉三角生成器。程序可以生成指定行数的杨辉三角，并以美观的格式显示。

## 什么是杨辉三角？

杨辉三角（也称为帕斯卡三角）是一个三角形数字阵列。在这个三角形中：
- 每行数字左右对称
- 每行开始和结束的数字都是1
- 中间的每个数字都是上一行中与之相邻的两个数字之和

例如：
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

## 使用方法

1. 确保您的系统已安装Python 3
2. 下载 `pascal_triangle.py` 文件
3. 在命令行中运行程序：
   ```bash
   python pascal_triangle.py
   ```
4. 根据提示输入想要生成的杨辉三角的行数（1-20）

## 功能特点

- 支持生成1-20行的杨辉三角
- 美观的三角形显示格式
- 包含输入验证
- 代码注释完善，易于理解

## 代码结构

程序包含三个主要函数：
- `generate_pascal_triangle(n)`: 生成杨辉三角的数据结构
- `print_pascal_triangle(triangle)`: 格式化打印杨辉三角
- `main()`: 程序入口，处理用户输入并调用其他函数