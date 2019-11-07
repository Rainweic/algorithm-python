def Union(a, b):
    '''
    将两个升序的数组a, b合并在一起成为升序数组c
    '''
    i, j = 0, 0
    c = []
    # 先进行a, b中元素对比 两两比较 小的放入c 
    # 总体上就是a, b中的元素(俩数组中长度一致的那部分)按从小到大放入c
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    print(c)
    # 将数组a, b中那个还有多余部分的数组的末尾插入c
    while i < len(a):
        c.append(a[i])
        i += 1
    print(c)
    while j < len(b):
        c.append(b[j])
        j += 1
    print(c)

a = [2,4,6,8,11,14,15]
b = [2,5,7,8,9,10,17]
Union(a, b)