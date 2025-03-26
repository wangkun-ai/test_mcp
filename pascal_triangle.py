def generate_pascal_triangle(n):
    """生成杨辉三角
    
    Args:
        n (int): 要生成的行数
        
    Returns:
        list: 包含杨辉三角数字的二维列表
    """
    triangle = []
    
    for i in range(n):
        # 每一行都是一个列表
        row = []
        for j in range(i + 1):
            # 如果是每行的开始或结束，数字为1
            if j == 0 or j == i:
                row.append(1)
            else:
                # 其他位置的数字是上一行的两个数字之和
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    
    return triangle

def print_pascal_triangle(triangle):
    """打印杨辉三角，使其呈现三角形状
    
    Args:
        triangle (list): 杨辉三角的二维列表
    """
    # 获取最后一行的字符串长度，用于对齐
    max_width = len(' '.join(map(str, triangle[-1])))
    
    for row in triangle:
        # 将数字转换为字符串并用空格连接
        row_str = ' '.join(map(str, row))
        # 居中对齐打印
        print(row_str.center(max_width))

def main():
    # 获取用户输入的行数
    while True:
        try:
            n = int(input('请输入要生成的杨辉三角的行数（1-20）：'))
            if 1 <= n <= 20:
                break
            else:
                print('请输入1到20之间的数字！')
        except ValueError:
            print('请输入有效的数字！')
    
    # 生成并打印杨辉三角
    triangle = generate_pascal_triangle(n)
    print('\n生成的杨辉三角如下：\n')
    print_pascal_triangle(triangle)

if __name__ == '__main__':
    main()