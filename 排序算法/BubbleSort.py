def BubbleSort(array):
    exchange = len(array) - 1   # 进行大小替换的位置
    while exchange != 0:
        bound = exchange    # 每一轮需要遍历的边界
        exchange = 0
        # 一轮循环中 大小换位 按从小到大顺序
        for idx in range(bound):
            if array[idx] > array[idx + 1]:
                temp = array[idx]
                array[idx] = array[idx+1]
                array[idx+1] = temp
                exchange = idx
    return array

a = [3,5,2,6,4,8]
print(BubbleSort(a))
